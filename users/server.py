import os
import sanic
from sanic import Sanic
from sanic_openapi import openapi, openapi3_blueprint

from resources.resources_users_listusers import listusers_resolver
from interfaces.ListUsersRequest import ListUsersRequestSuccessResponse, ListUsersRequestErrorResponse
from resources.resources_users_insertuser import insertuser_resolver
from interfaces.InsertUserRequest import InsertUserRequestBody, InsertUserRequestSuccessResponse, InsertUserRequestErrorResponse


__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "05/09/2022"
__version__ = open("version").read()


app = Sanic("UserApp")
app.blueprint(openapi3_blueprint)


@app.get("/api/users")
@openapi.summary("List Users")
@openapi.description("Route destined to list users according user's permissions")
@openapi.parameter("Authentication", str, location="header", required=True)
@openapi.parameter("name", str, location="query", required=False)
@openapi.parameter("profile", int, location="query", required=False)
@openapi.response(200, {"application/json": ListUsersRequestSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": ListUsersRequestErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": ListUsersRequestErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": ListUsersRequestErrorResponse}, "Internal server error")
async def list_users(request: sanic.Request):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": request.query_args
        }
        return listusers_resolver(req)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.put("/api/users")
@openapi.summary("Insert User")
@openapi.description("Route destined to add a new user to the system")
@openapi.parameter("Authentication", str, location="header", required=True)
@openapi.body({"application/json": InsertUserRequestBody}, required=True)
@openapi.response(200, {"application/json": InsertUserRequestSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": InsertUserRequestErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": InsertUserRequestErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": InsertUserRequestErrorResponse}, "Internal server error")
async def insert_user(request: sanic.Request):

    try:
        req = {
            "headers": request.headers,
            "body": request.body,
            "params": {}
        }
        return insertuser_resolver(req)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


if __name__ == "__main__":
    host = os.getenv("SERVER_HOST", "0.0.0.0")
    port = int(os.getenv("SERVER_PORT", "8090"))
    dev = not (os.getenv("PROD", "true") in ["true", "True", "TRUE", "1"])
    app.run(host=host, port=port, dev=dev)
