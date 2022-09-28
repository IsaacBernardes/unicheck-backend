from sanic_openapi import openapi

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "26/09/2022"
__version__ = open("version").read()


class DefaultSuccessResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(None, default=[])
    version = openapi.String(default="1.0.0")


class DefaultErrorResponse:
    message = openapi.String(default="Ocorreu um erro ao finalizar a operação")
    data = openapi.Array(None, default=[])
    version = openapi.String(default="1.0.0")