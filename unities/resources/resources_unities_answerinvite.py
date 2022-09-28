import psycopg2
from utils.database import Connection

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
    "notFound": {"status": 404, "message": "O convite não foi encontrado"},
    "alreadyExists": {"status": 412, "message": "A unidade já foi cadastrado"},
    "defaultError": {"status": 500, "message": "Erro interno da API"}
}


def answerinvite_resolver(request, context=None):
    conn = Connection()
    cnx = conn.init_connection()
    cursor = cnx.cursor()
    situation = "defaultError"
    data = []

    try:
        # TODO: VALIDATE TOKEN
        id_user = ""

        values = {
            "id_user": id_user,
            "id_unity": request["params"]["unityId"],
            "answer": request["body"]["answer"]
        }

        if values["answer"] is True:

            query = """UPDATE public."unity_users" 
                       SET "accepted" = TRUE
                       WHERE "id_user" = %(id_user)s
                       AND "id_unity" = %(id_unity)s;"""

        else:

            query = """DELETE FROM public."unity_users"
                       WHERE "id_user" = %(id_user)s
                       AND "id_unity" = %(id_unity)s;"""

        cursor.execute(query, values)
        affected_rows = cursor.rowcount

        if affected_rows > 0:
            situation = "success"
            cnx.commit()
        else:
            situation = "alreadyExists"

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
        cnx.close()
        return api_results[situation]["status"], {
            "message": api_results[situation]["message"],
            "data": data,
            "version": __version__,
        }
