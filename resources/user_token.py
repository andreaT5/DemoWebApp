from flask import request, jsonify
from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.user import User

class TokenResource(Resource):

    def post(self, email, password):
        #data_generator = request.get_json()
        email = email
        password = password

        user = User.get_by_email(email)

        if not user or not User.verify_password(password, user.password):
            return {'message': 'logindata data_generator is incorrect'}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(identity=user.id)

        #return {'access_token': access_token, 'refresh_token': refresh_token}, HTTPStatus.OK
        return jsonify(access_token=access_token, refresh_token=refresh_token), HTTPStatus.OK


class RefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=False)

        return {'access_token': access_token}, HTTPStatus.OK