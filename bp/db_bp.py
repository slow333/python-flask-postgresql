from flask import Blueprint, request, redirect # type: ignore
from flask import render_template as render # type: ignore
from module.body import body

db_bp = Blueprint("db_bp", __name__, url_prefix="/sqlalchemy")

@db_bp.route("/setup")
def db_setup():
  return body("DB 설정", render("db/db_setup.html"))

@db_bp.route("/core-crud")
def core_crud_db():
  return body("Core CRUD", render("db/core_crud.html"))

