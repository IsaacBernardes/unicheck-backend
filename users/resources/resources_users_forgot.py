import psycopg2
import sanic.response

from utils.keycloack import KeycloackClient

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "25/09/2022"
__version__ = open("version").read()

api_results = {
    "success": {"status": 200, "message": "Operação realizada com sucesso"},
    "keyError": {"status": 400, "message": "Os dados fornecidos são insuficientes ou inválidos"},
    "dataError": {"status": 400, "message": "Erro ao realizar a operação no banco de dados"},
    "databaseError": {"status": 400, "message": "Erro no banco de dados"},
    "invalidToken": {"status": 401, "message": "O token do usuário não foi reconhecido"},
    "notAuthorized": {"status": 401, "message": "O usuário não possui acesso a esta funcionalidade"},
    "notFound": {"status": 404, "message": "O usuário não foi encontrado"},
    "alreadyExists": {"status": 412, "message": "O usuário já foi cadastrado"},
    "defaultError": {"status": 500, "message": "Erro interno da API"}
}


def forgot_resolver(request, context=None):

    keycloack_client = KeycloackClient()
    keycloack_client.connect()
    situation = "defaultError"
    data = []

    try:

        email = request["body"]["email"]

        find_user_path = "/admin/realms/$REALM/users?&exact=true&email="+email
        status_code, users = keycloack_client.get(find_user_path)

        if status_code != 200 or len(users) == 0:
            situation = "notFound"
            return

        req = ["UPDATE_PASSWORD"]
        update_path = "/admin/realms/$REALM/users/" + users[0]["id"] + "/execute-actions-email"
        result = keycloack_client.put(update_path, req)

        if result[0] == 204:
            situation = "success"
        else:
            situation = "defaultError"

    except KeyError as ex:
        print("Key error: " + str(ex))
        situation = "keyError"
    except (psycopg2.IntegrityError, psycopg2.DataError, psycopg2.NotSupportedError) as ex:
        print("Data error: " + str(ex))
        situation = "dataError"
    except (psycopg2.DatabaseError, psycopg2.Error) as ex:
        print("Database error: " + str(ex))
        situation = "databaseError"
    except Exception as ex:
        print("Default error: " + str(ex))
        situation = "defaultError"

    finally:
        keycloack_client.disconnect()
        return sanic.response.json(body={
            "message": api_results[situation]["message"],
            "data": data,
            "version": __version__,
        }, status=api_results[situation]["status"])

