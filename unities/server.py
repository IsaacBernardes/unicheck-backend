import sanic
from sanic import Sanic
from sanic_openapi import openapi, openapi2_blueprint

from utils.environments import Environment
from resources.resources_unities_listunities import listunities_resolver
from resources.resources_unities_createunity import createunity_resolver
from resources.resources_unities_updateunity import updateunity_resolver
from resources.resources_unities_deleteunity import deleteunity_resolver
from resources.resources_unities_listunitymembers import listunitymembers_resolver
from resources.resources_unities_listinvites import listinvites_resolver
from resources.resources_unities_createinivite import createinvite_resolver
from resources.resources_unities_updateinvite import updateinvite_resolver
from resources.resources_unities_deleteinvite import deleteinvite_resolver
from resources.resources_unities_answerinvite import answerinvite_resolver
from interfaces.DefaultResponses import DefaultSuccessResponse, DefaultErrorResponse
from interfaces.InivitesRequests import InsertInviteRequestBody, UpdateInviteRequestBody, AnswerInviteRequestBody, ListInvitesResponse
from interfaces.UnityRequests import ListUnitiesResponse, ListUnityMembersResponse, InsertUnityRequestBody


__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "27/09/2022"
__version__ = open("version").read()


app = Sanic("UnityApp")
app.blueprint(openapi2_blueprint)


@app.get("/api/unities")
@openapi.summary("List unities")
@openapi.description("Route destined to list unities")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.parameter("userId", int, location="query", required=False)
@openapi.response(200, {"application/json": ListUnitiesResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def list_unities(request: sanic.Request):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": build_query_params(request.query_args)
        }
        status_code, result = listunities_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.post("/api/unities")
@openapi.summary("Insert unity")
@openapi.description("Route destined to create unities")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.body({"application/json": InsertUnityRequestBody}, required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def insert_unity(request: sanic.Request):
    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {}
        }
        status_code, result = createunity_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.put("/api/unities/<unity_id:int>")
@openapi.summary("Update unity")
@openapi.description("Route destined to update unities")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.body({"application/json": InsertUnityRequestBody}, required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def update_unity(request: sanic.Request, unity_id: int):
    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {
                "id": unity_id
            }
        }
        status_code, result = updateunity_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.delete("/api/unities/<unity_id:int>")
@openapi.summary("Delete unity")
@openapi.description("Route destined to delete unities")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def delete_unity(request: sanic.Request, unity_id: int):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": {
                "id": unity_id
            }
        }
        status_code, result = deleteunity_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.get("/api/unities/<unity_id:int>/members")
@openapi.summary("List unity members")
@openapi.description("Route destined to list unity members")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.response(200, {"application/json": ListUnityMembersResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def list_unity_members(request: sanic.Request, unity_id: int):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": {
                "id": unity_id
            }
        }
        status_code, result = listunitymembers_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.post("/api/unities/<unity_id:int>/invites")
@openapi.summary("Create an invite")
@openapi.description("Route destined to create an unity invite")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.body({"application/json": InsertInviteRequestBody}, required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def insert_invite(request: sanic.Request, unity_id: int):
    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {
                "id": unity_id
            }
        }
        status_code, result = createinvite_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.put("/api/unities/<unity_id:int>/invites/<user_id>")
@openapi.summary("Update an invite")
@openapi.description("Route destined to update an unity invite")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.body({"application/json": UpdateInviteRequestBody}, required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def update_invite(request: sanic.Request, unity_id: int, user_id: str):
    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {
                "id": unity_id,
                "userId": user_id
            }
        }
        status_code, result = updateinvite_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.delete("/api/unities/<unity_id:int>/invites/<user_id>")
@openapi.summary("Delete an invite")
@openapi.description("Route destined to delete an unity invite")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def delete_invite(request: sanic.Request, unity_id: int, user_id: str):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": {
                "id": unity_id,
                "userId": user_id
            }
        }
        status_code, result = deleteinvite_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.get("/api/invites")
@openapi.summary("List user's invites")
@openapi.description("Route destined to list user's invite")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.response(200, {"application/json": ListInvitesResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def answer_invite(request: sanic.Request):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": {}
        }
        status_code, result = listinvites_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.put("/api/invites/<unity_id>")
@openapi.summary("Answer an invite")
@openapi.description("Route destined to answer an unity invite")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.body({"application/json": AnswerInviteRequestBody}, required=True)
@openapi.response(200, {"application/json": DefaultSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": DefaultErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": DefaultErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": DefaultErrorResponse}, "Internal server error")
async def answer_invite(request: sanic.Request, unity_id: int):
    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {
                "unityId": unity_id
            }
        }
        status_code, result = answerinvite_resolver(req)
        return sanic.response.json(body=result, status=status_code)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


def build_query_params(params_list):
    result = {}
    for param in params_list:
        result[param[0]] = param[1]
    return result


if __name__ == "__main__":
    environ = Environment()

    host = environ.get("SERVER_HOST")
    port = environ.get("SERVER_PORT")
    dev = not environ.get("PROD")
    app.run(host=host, port=port, dev=dev)
