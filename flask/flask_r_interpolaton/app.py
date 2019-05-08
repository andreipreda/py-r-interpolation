import os
from pathlib import Path
from flask import Flask, current_app, jsonify, request
from flask_cors import CORS
from mongoengine import connect, MongoEngineConnectionError
import namesgenerator
from model import Doc
from app_logic import random_df, call_r


def create_app(config=None):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    mongo_host = os.environ.get('MONGO_HOST', default='mongodb://127.0.0.1:27017')

    try:
        connect(db='pyr',
                host=mongo_host)
    except MongoEngineConnectionError as exc:
        raise exc

    @app.route('/api/python')
    def test():
        """Random pandas df"""
        df = random_df()
        return jsonify({'py': df.to_json()}), 200

    @app.route('/api/r')
    def from_r():
        """Dataframe from an R tibble using rpy2"""
        df = call_r(Path(current_app.config['R_LOCATION'], 'rapp.r'))
        return jsonify({'r': df.to_json()}), 200

    """MONGO IO API SIMULATION"""
    @app.route('/api/add', methods=['POST'])
    def add_doc():
        try:
            d = Doc(title=namesgenerator.get_random_name())
            d.save()

            return d.to_json(), 201

        except Exception as ex:
            raise ex

    @app.route('/api/remove', methods=['DELETE'])
    def remove_doc():
        id = request.args.get('id')
        try:
            d = Doc.objects.get(id=id)
            if d:
                d.delete()

            return jsonify({'ok': 1}), 200

        except Exception as ex:
            raise ex

    return app
