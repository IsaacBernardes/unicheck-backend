from sanic_openapi import openapi

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "05/09/2022"
__version__ = open("version").read()


class ListUsersRequestResponseData:
    id = openapi.Integer(default=1)
    name = openapi.String(default="Isaac Bernardes")
    user = openapi.String(default="isaac.bernardes")
    createdAt = openapi.DateTime()


class ListUsersRequestSuccessResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(ListUsersRequestResponseData)
    version = openapi.String(default="1.0.0")


class ListUsersRequestErrorResponse:
    message = openapi.String(default="Ocorreu um erro ao finalizar a operação")
    data = openapi.Array(None, default=[])
    version = openapi.String(default="1.0.0")
