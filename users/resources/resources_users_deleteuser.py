import psycopg2
import sanic.response

from utils.keycloack import KeycloackClient
from resources.resources_users_validatetoken import validatetoken_resolver

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
    "defaultError": {"status": 500, "message": "Erro interno da API"}
}


def deleteuser_resolver(request, context=None):

    keycloack_client = KeycloackClient()
    keycloack_client.connect()
    situation = "defaultError"
    data = []

    try:

        status_code, user_info = keycloack_client.verify_token(token=request["headers"]["Authorization"])

        if status_code != 200:
            situation = "invalidToken"
            return

        update_path = "/admin/realms/$REALM/users/" + user_info["sub"]
        result = keycloack_client.delete(update_path)

        if result[0] == 204:
            situation = "success"
        else:
            situation = "notFound"

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

