import logging

from flask import request


def controller_api(app):
    def api_get_link():
        link = request.get_json().get('hash')
        if link is None:
            return {"ERROR": "Пустая ссылка."}
        result = app.get_long_link(link)
        return {"response": result}
    return api_get_link
