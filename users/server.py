import sanic
from sanic import Sanic
from sanic_openapi import openapi, openapi3_blueprint

from resources.resources_users_finduser import finduser_resolver
from resources.resources_users_signin import signin_resolver
from resources.resources_users_signup import signup_resolver
from resources.resources_users_validatetoken import validatetoken_resolver
from interfaces.ListUsersRequest import ListUsersRequestSuccessResponse, ListUsersRequestErrorResponse
from interfaces.InsertUserRequest import InsertUserRequestBody, InsertUserRequestSuccessResponse, InsertUserRequestErrorResponse
from interfaces.SigninRequest import SigninRequestBody, SigninRequestSuccessResponse, SigninRequestErrorResponse
from utils.environments import Environment


__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "22/09/2022"
__version__ = open("version").read()


app = Sanic("UserApp")
app.blueprint(openapi3_blueprint)


# @app.get("/api/users")
# @openapi.summary("List Users")
# @openapi.description("Route destined to list users according user's permissions")
# @openapi.parameter("Authentication", str, location="header", required=True)
# @openapi.parameter("name", str, location="query", required=False)
# @openapi.parameter("profile", int, location="query", required=False)
# @openapi.response(200, {"application/json": ListUsersRequestSuccessResponse}, "Operation completed successfully")
# @openapi.response(400, {"application/json": ListUsersRequestErrorResponse}, "There was a problem with the data provided")
# @openapi.response(401, {"application/json": ListUsersRequestErrorResponse}, "User is not authenticated or does not have access to this functionality")
# @openapi.response(500, {"application/json": ListUsersRequestErrorResponse}, "Internal server error")
# async def list_users(request: sanic.Request):
#     try:
#         req = {
#             "headers": request.headers,
#             "body": {},
#             "params": request.query_args
#         }
#         return listusers_resolver(req)
#     except Exception as ex:
#         print(ex)
#         return sanic.response.json(body={
#             "message": "Erro ao receber a requisição",
#             "version": __version__,
#             "data": []
#         }, status=500)


@app.get("/api/users/find")
@openapi.summary("Find Users by E-mail")
@openapi.description("Route destined to list users by e-mail")
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.parameter("email", str, location="query", required=True)
# @openapi.response(200, {"application/json": ListUsersRequestSuccessResponse}, "Operation completed successfully")
# @openapi.response(400, {"application/json": ListUsersRequestErrorResponse}, "There was a problem with the data provided")
# @openapi.response(401, {"application/json": ListUsersRequestErrorResponse}, "User is not authenticated or does not have access to this functionality")
# @openapi.response(500, {"application/json": ListUsersRequestErrorResponse}, "Internal server error")
async def find_user(request: sanic.Request):
    try:
        req = {
            "headers": request.headers,
            "body": {},
            "params": request.query_args
        }
        return finduser_resolver(req)
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
@openapi.parameter("Authorization", str, location="header", required=True)
@openapi.body({"application/json": InsertUserRequestBody}, required=True)
@openapi.response(200, {"application/json": InsertUserRequestSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": InsertUserRequestErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": InsertUserRequestErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(412, {"application/json": InsertUserRequestErrorResponse}, "User email already exists")
@openapi.response(500, {"application/json": InsertUserRequestErrorResponse}, "Internal server error")
async def insert_user(request: sanic.Request):

    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {}
        }
        return signup_resolver(req)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.post("/api/users/signin")
@openapi.summary("Sing in")
@openapi.description("Route destined authenticate yourself")
@openapi.body({"application/json": SigninRequestBody}, required=True)
@openapi.response(200, {"application/json": SigninRequestSuccessResponse}, "Operation completed successfully")
@openapi.response(400, {"application/json": SigninRequestErrorResponse}, "There was a problem with the data provided")
@openapi.response(401, {"application/json": SigninRequestErrorResponse}, "User is not authenticated or does not have access to this functionality")
@openapi.response(500, {"application/json": SigninRequestErrorResponse}, "Internal server error")
async def insert_user(request: sanic.Request):

    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {}
        }
        return signin_resolver(req)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


@app.post("/api/users/validatetoken")
@openapi.summary("Validate token")
@openapi.description("Verify if user token is valid")
@openapi.parameter("Authorization", str, location="header", required=True)
async def validate_token(request: sanic.Request):

    try:
        req = {
            "headers": request.headers,
            "body": request.json,
            "params": {}
        }
        return validatetoken_resolver(req)
    except Exception as ex:
        print(ex)
        return sanic.response.json(body={
            "message": "Erro ao receber a requisição",
            "version": __version__,
            "data": []
        }, status=500)


if __name__ == "__main__":
    environ = Environment()

    host = environ.get("SERVER_HOST")
    port = environ.get("SERVER_PORT")
    dev = not environ.get("PROD")
    app.run(host=host, port=port, dev=dev)
