import logging
import json
from flask import request, Flask
from app import App
import os

app_flask = Flask(__name__)
"""print(os.environ["DBNAME"])
print(os.environ["HOST"])
print(os.environ["USER"])
print(os.environ["PASSWORD"])
print(os.environ["PORT"])
"""
app = App(dbname=os.environ["DBNAME"],
          host=os.environ["HOST"],
          user=os.environ["USER"],
          password=os.environ["PASSWORD"],
          port=os.environ["PORT"])


@app_flask.route("/api/get_short_link", methods=['POST'])
def api_get_short_link():
    link = request.get_json().get('link')
    app_flask.logger.log(level=logging.INFO, msg=str(request.args))
    if link is None or link == "":
        return {"ERROR": "Пустая ссылка."}
    return {"response": app.get_short_link(link)}


@app_flask.route("/api/get_link", methods=['POST'])
def api_get_link():
    link = request.get_json().get('hash')
    app_flask.logger.log(level=logging.INFO, msg=str(request.args))
    if link is None:
        return {"ERROR": "Пустая ссылка."}
    result = app.get_long_link(link)
    return {"response": result}


app_flask.run(host='0.0.0.0', port=int(os.environ["PORT_EXEC"]))
