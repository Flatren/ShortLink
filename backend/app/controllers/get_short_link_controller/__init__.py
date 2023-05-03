import logging

from flask import request


def controller_api(app):
    def api_get_short_link():
        link = request.get_json().get('link')
        if link is None or link == "":
            return {"ERROR": "Пустая ссылка."}
        return {"response": app.get_short_link(link)}

    return api_get_short_link