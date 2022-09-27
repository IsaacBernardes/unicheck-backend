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
    "notFound": {"status": 404, "message": "A unidade não foi encontrada"},
    "alreadyExists": {"status": 412, "message": "A unidade já foi cadastrado"},
    "defaultError": {"status": 500, "message": "Erro interno da API"}
}


def listunitymembers_resolver(request, context=None):
    conn = Connection()
    cnx = conn.init_connection()
    cursor = cnx.cursor()
    situation = "defaultError"
    data = []

    try:
        # TODO: VALIDATE TOKEN
        is_support = True
        user_id = ""

        if not is_support:
            values = {
                "id_user": "",  # TODO: PREENCHER COM ID DO TOKEN OBTID
                "id_unity": request["params"]["id"]
            }

            query = """SELECT id FROM public."unity_users" uu
                       WHERE uu."id_user" = %(id_user)s
                       AND uu."id_unity" = %(id_unity)s
                       AND uu."id_occupation" = 1
                       AND uu."accepted" IS TRUE;"""

            cursor.execute(query, values)
            result = cursor.fetchall()

            if result is None or len(result) == 0:
                situation = "notAuthorized"
                return

        values = {
            "id_unity": request["params"]["id"]
        }

        query = """SELECT json_agg(dt) FROM (
                        SELECT uu."id_user" as "userId",
                               uu."accepted" as "accepted",
                               o."id" as "occupationId",
                               o."alias" as "occupationAlias"
                        FROM public."unity_users" uu, public."occupation" o
                        WHERE o."id" = uu."id_occupation"
                        AND uu."id_unity" = %(id_unity)s
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
