from control.view import View
from webargs.flaskparser import parser
from marshmallow import ValidationError
from flask import request

from control.request_list import CREATE_USER, GET_USER, CHANGE_USER
from model.model import ListaUsers


class UserControl:
    @staticmethod
    def create_user():
        try:
            args = parser.parse(CREATE_USER, request)
        except ValidationError as err:
            return View.error(400, str(err))
        user = ListaUsers.create_user(CREATE_USER)
        result = [{'id_user': rst[0]} for rst in user]
        return View.success(result)

    @staticmethod
    def get_user():
        try:
            args = parser.parse(GET_USER, request)
            print(args)
        except ValidationError as err:
            return View.error(400, str(err))
        user = ListaUsers.get_user(args)
        result = [{'id_user': rst[0].id_user} for rst in user]
        return View.success(result)

    @staticmethod
    def delete_user():
        try:
            args = parser.parse(GET_USER, request)
        except ValidationError as err:
            return View.error(400, str(err))
        user = ListaUsers.delete_user(GET_USER)
        result = [{'id_user': rst[0]} for rst in user]
        return View.success(result)

    @staticmethod
    def change_user():
        try:
            args = parser.parse(CHANGE_USER, request)
        except ValidationError as err:
            return View.error(400, str(err))
        user = ListaUsers.change_user(CHANGE_USER)
        result = [{'id_user': rst[0]} for rst in user]
        return View.success(result)



