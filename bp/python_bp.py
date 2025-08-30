from flask import Blueprint, request, redirect # type: ignore
from flask import render_template as render # type: ignore
from module.body import body

python_bp = Blueprint("python_bp", __name__, url_prefix="/python")

@python_bp.route("/install-flask")
def install_python():
  return body("Python 설치", render("python/00_python_flask_install.html"))

@python_bp.route("/datatype")
def datatype_python():
  return body("Python 데이터 타입", render("python/01_datatype.html"))

@python_bp.route("/print-format")
def print_format_python():
  return body("Python 출력 포맷", render("python/02_print_format.html"))

@python_bp.route("/loop")
def loop_python():
  return body("Python 반복문", render("python/03_loop.html"))

@python_bp.route("/def")
def def_python():
  return body("Python 함수", render("python/04_def_file.html"))

@python_bp.route("/class-module")
def class_python():
  return body("Python 클래스", render("python/05_class_module.html"))

@python_bp.route("/try-except")
def try_except_python():
  return body("Python 예외 처리", render("python/06_try_except.html"))

@python_bp.route("/library")
def library_python():
  return body("Python 라이브러리", render("python/07_py_library.html"))

@python_bp.route("/closer-decorator")
def closer_decorator_python():
  return body("Python 클로저와 데코레이터", render("python/08_closer_decorator.html"))

@python_bp.route("/regexp")
def regexp_python():
  return body("Python 정규 표현식", render("python/09_regexp.html"))
