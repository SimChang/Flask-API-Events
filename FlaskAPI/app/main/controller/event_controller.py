from flask import request
from flask_restplus import Resource

from ..util.dto import EventDto
from ..service.event_service import save_new_event, get_events

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


@api.route('/list_events')
class EventGet(Resource):
    @api.doc('list of events with optional filters')
    @api.marshal_list_with(_event, envelope='data')
    def get(self):
        """Gets existing events according to filters"""
        filters = dict()
        filters["name"] = request.args.get('name')
        filters["name_exact"] = request.args.get('name_exact')
        filters["start_min"] = request.args.get('start_min')
        filters["start_max"] = request.args.get('start_max')
        filters["stop_min"] = request.args.get('stop_min')
        filters["stop_max"] = request.args.get('stop_max')
        filters["tags"] = request.args.get('tags')

        # Removing keys with None values
        filters = {k: v for k, v in filters.items() if (v is not None and v != "")}

        return get_events(filters)
