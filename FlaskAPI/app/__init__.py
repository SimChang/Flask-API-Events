import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api
from flask import Blueprint

from .main.controller.event_controller import api as event_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask API for events management',
          version='1.0',
          description='A Flask API for events management'
          )

api.add_namespace(event_ns, path='/event')
