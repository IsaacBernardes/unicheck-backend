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
    "alreadyExists": {"status": 412, "message": "A unidade já foi cadastrado"},
    "defaultError": {"status": 500, "message": "Erro interno da API"}
}


def listinvites_resolver(request, context=None):
    conn = Connection()
    cnx = conn.init_connection()
    cursor = cnx.cursor()
    situation = "defaultError"
    data = []

    try:
        # TODO: VALIDATE TOKEN
        id_user = ""

        values = {
            "id_user": id_user
        }

        query = """SELECT json_agg(dt) FROM (
                            SELECT u."id" as "unityId",
                                   u."name" as "unityName",
                                   uu."accepted" as "accepted",
                                   o."id" as "occupationId",
                                   o."alias" as "occupationAlias"
                            FROM public."unity" u, public."unity_users" uu, public."occupation" o
                            WHERE u."id" = uu."id_unity"
                            AND o."id" = uu."id_occupation"
                            AND uu."id_user" = %(id_user)s
                       )dt;"""

        cursor.execute(query, values)
        result = cursor.fetchone()
        situation = "success"

        if result is not None and len(result) > 0 and result[0] is not None:
            data = result[0]

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
