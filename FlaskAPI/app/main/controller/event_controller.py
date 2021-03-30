from flask import request
from flask_restplus import Resource, fields, reqparse

from ..util.dto import EventDto
from ..service.event_service import save_new_event, get_events, remove_events

api = EventDto.api
_event = EventDto.event

name_field = api.model('names', {
    'name_list': fields.List(fields.String, description='names of events to delete')
})

get_parser = api.parser()
get_parser.add_argument('name', help='string')
get_parser.add_argument('name_exact', help="True or False, False will act like 'contain'")
get_parser.add_argument('start_min', help='date string with format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20')
get_parser.add_argument('start_max', help='date string with format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20')
get_parser.add_argument('stop_min', help='date string with format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20')
get_parser.add_argument('stop_max', help='date string with format %Y-%m-%d %H:%M, ex: 2010-01-20 5:20')
get_parser.add_argument('tags', help='strings separated with commas')


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
    @api.expect(get_parser)
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


@api.route('/remove_events')
class EventRemove(Resource):
    @api.doc('remove events with corresponding names')
    @api.expect(name_field)
    def delete(self):
        """Delete events with corresponding names"""
        data = request.json

        return remove_events(data["name_list"])

