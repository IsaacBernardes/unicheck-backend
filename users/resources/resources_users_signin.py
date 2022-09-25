import psycopg2
import sanic.response

from utils.keycloack import KeycloackClient

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "06/09/2022"
__version__ = open("version").read()

api_results = {
    "success": {"status": 200, "message": "Operação realizada com sucesso"},
    "keyError": {"status": 400, "message": "Os dados fornecidos são insuficientes ou inválidos"},
    "dataError": {"status": 400, "message": "Erro ao realizar a operação no banco de dados"},
    "databaseError": {"status": 400, "message": "Erro no banco de dados"},
    "invalidToken": {"status": 401, "message": "O token do usuário não foi reconhecido"},
    "invalidUser": {"status": 401, "message": "O usuário informado não foi cadastrado"},
    "notAuthorized": {"status": 401, "message": "O usuário não possui acesso a esta funcionalidade"},
    "defaultError": {"status": 500, "message": "Erro interno da API"}
}


def signin_resolver(request, context=None):

    keycloack_client = KeycloackClient()
    keycloack_client.connect()
    situation = "defaultError"
    data = []

    try:

        body_request = {
            "username": request["body"]["email"],
            "password": request["body"]["password"],
            "grant_type": "password",
            "client_id": keycloack_client.client_id,
            "client_secret": keycloack_client.client_secret
        }

        signin_path = "/realms/$REALM/protocol/openid-connect/token"
        result = keycloack_client.post_encoded(signin_path, body_request)

        if result[0] == 200:
            situation = "success"
            data = result[1]
        else:
            situation = "invalidUser"

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

