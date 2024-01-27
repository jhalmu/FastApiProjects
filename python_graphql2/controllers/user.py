import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL
from type.user import Mutation, Query

from conn.db import conn
from models.index import users

user = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

user.add_route("/graphql", graphql_app)
