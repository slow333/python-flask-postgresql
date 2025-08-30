from flask import Flask, render_template as render # type: ignore
from module.body import body
from bp.crud_no_db import bp as crud_no_db_bp
from bp.crud_db import bp as crud_db_bp
from bp.postgres_bp import psql_bp
from bp.python_bp import python_bp
from bp.db_bp import db_bp

app = Flask(__name__)

app.register_blueprint(crud_no_db_bp)
# app.register_blueprint(crud_db_bp)
app.register_blueprint(psql_bp)
app.register_blueprint(python_bp)
app.register_blueprint(db_bp)

@app.route("/")
def index():
  return body("HOME", render("index.html"))

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
