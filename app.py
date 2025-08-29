from flask import Flask, render_template as render # type: ignore
from module.body import body
from bp.crud_no_db import bp as main_bp
from bp.postgres_bp import psql_bp
app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(psql_bp)

@app.route("/")
def index():
  return body("HOME", render("index.html"))

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
