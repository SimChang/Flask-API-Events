from flask import request
from flask_restplus import Resource

from ..util.dto import EventDto
from ..service.event_service import save_new_event

api = EventDto.api
_event = EventDto.event


@api.route('/add_event')
class EventAdd(Resource):
    @api.doc('create a new event')
    @api.expect(_event, validate=True)
    def post(self):
        """Creates a new Event"""
        data = request.json
        return save_new_event(data)
