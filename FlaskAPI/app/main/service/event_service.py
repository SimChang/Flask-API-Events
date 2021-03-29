import datetime

from app.main import db
from app.main.model.event import Event


def save_new_event(data):
    """Saves a new event if not existing already

    Args:
        data (dict): A dict of the event's data

    Returns:
        dict: The response object to send back
    """

    event = Event.objects(name=data["name"]).first()
    if not event:
        new_event = Event(
            **{atr: value for atr, value in data.items()}
        )
        new_event.save()
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Event already exists. Please choose another name.'
        }
        return response_object, 409







