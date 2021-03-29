from flask_restplus import Namespace, fields


class EventDto:
    api = Namespace('event', description='event related operations')
    event = api.model('user', {
        'name': fields.String(required=True, description='event name'),
        'start': fields.String(required=True, description='event start date'),
        'stop': fields.String(description='event stop date'),
        'tags': fields.List(fields.String, description='tags associated with the event')
    })
