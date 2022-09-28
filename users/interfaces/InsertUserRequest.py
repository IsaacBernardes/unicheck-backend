from sanic_openapi import openapi

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "28/09/2022"
__version__ = open("version").read()


class InsertUserRequestBody:
    firstName = openapi.String(default="Isaac")
    lastName = openapi.String(default="Bernardes")
    email = openapi.String(default="isaac.bernardes@ufrpe.br")
    password = openapi.String(default="********")


class InsertUserRequestSuccessResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(None, default=[])
    version = openapi.String(default="1.0.0")


class InsertUserRequestErrorResponse:
    message = openapi.String(default="Ocorreu um erro ao finalizar a operação")
    data = openapi.Array(None, default=[])
    version = openapi.String(default="1.0.0")