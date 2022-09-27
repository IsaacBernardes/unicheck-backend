from sanic_openapi import openapi

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "26/09/2022"
__version__ = open("version").read()


class Invite:
    unityId = openapi.Integer(default=2)
    unityName = openapi.String(default="Unidade")
    occupationId = openapi.Integer(default=3)
    accepted = openapi.Boolean(default=True)


class ListInvitesResponse:
    message = openapi.String(default="Operação realizada com sucesso")
    data = openapi.Array(Invite)
    version = openapi.String(default="1.0.0")


class InsertInviteRequestBody:
    userId = openapi.String(default="aaa-bbb-ccc")
    occupationId = openapi.Integer(default=1)


class UpdateInviteRequestBody:
    occupationId = openapi.Integer(default=1)


class AnswerInviteRequestBody:
    answer = openapi.Boolean(default=True)


