from flask import Blueprint, request, redirect # type: ignore
from flask import render_template as render # type: ignore
from module.body import body

psql_bp = Blueprint("postgres_bp", __name__, url_prefix="/postgres")

@psql_bp.route("/install")
def install_postgres():
  return body("Postgres 설치", render("postgres/install.html"))

@psql_bp.route("/datatype")
def datatype_postgres():
  return body("Postgres 데이터 타입", render("postgres/datatype.html"))

@psql_bp.route("/crud")
def crud_postgres():
  return body("Postgres CRUD", render("postgres/crud.html"))