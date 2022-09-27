from sanic_openapi import openapi

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "26/09/2022"
__version__ = open("version").read()


class Unity:
    id = openapi.Integer(default=1)
    name = openapi.String(default="Unidade")
    address = openapi.String(default="Rua unicheck, Recife, PE")
    schoolId = openapi.Integer(default=13)


class Member:
    userId = openapi.Integer(default=1)
    accepted = openapi.Boolean(default=True)
    occupationId = openapi.Integer(default=1)
    occupationAlias = openapi.Integer(default="GESTOR")


class ListUnitiesResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(Unity)
    version = openapi.String(default="1.0.0")


class ListUnityMembersResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(Member)
    version = openapi.String(default="1.0.0")


class InsertUnityRequestBody:
    name = openapi.String(default="Unidade")
    address = openapi.String(default="Rua unicheck, Recife, PE")
    schoolId = openapi.Integer(default=13)



