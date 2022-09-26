from sanic_openapi import openapi

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "05/09/2022"
__version__ = open("version").read()


class ListUsersRequestResponseData:
    id = openapi.String(default="aaaa-bbbb-cccc-dddd")
    createdTimestamp = openapi.Integer(default=1664082051627)
    enabled = openapi.Boolean(default=True)
    firstName = openapi.String(default="Isaac")
    lastName = openapi.String(default="Bernardes")
    email = openapi.String(default="isaac.bernardes@ufrpe.br")
    emailVerified = openapi.Boolean(default=True)


class ListUsersRequestSuccessResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(ListUsersRequestResponseData)
    version = openapi.String(default="1.0.0")


class ListUsersRequestErrorResponse:
    message = openapi.String(default="Ocorreu um erro ao finalizar a operação")
    data = openapi.Array(None, default=[])
    version = openapi.String(default="1.0.0")
