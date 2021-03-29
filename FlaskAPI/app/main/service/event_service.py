import datetime
import json

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
            **{atr: value for atr, value in data.items() if value != ""}
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


def get_events(filters):
    """ Returns events with filters

    Args:
        filters (dict): A dict of the filters
            name (str): str contained in the name, or full name depending on name_exact (default is full)
            name_exact (str): name is exact (True) or partial (False)
            start_min (datetime): filters start date before start_min
            start_max (datetime): filters start date after start_max
            stop_min (datetime): filters stop date before stop_min
            stop_max (datetime): filters stop date after stop_max
            tags (list of str): tags associated with the events

    Returns:
        list: A list of events passing the filters

    """

    query_filters = dict()

    if "name" in filters:
        if "name_exact" in filters:
            if filters["name_exact"] == "False":
                query_filters["name"] = {"$regex": filters["name"], '$options': 'i'}
            else:
                query_filters["name"] = filters["name"]
        else:
            """ Default behaviour """
            query_filters["name"] = filters["name"]

    if any([True for element in ["start_min", "start_max"] if element in filters]):
        query_filters["start"] = dict()
        if "start_min" in filters:
            query_filters["start"]["$gte"] = datetime.datetime.strptime(filters["start_min"], '%Y-%m-%d %H:%M')
        if "start_max" in filters:
            query_filters["start"]["$lte"] = datetime.datetime.strptime(filters["start_max"], '%Y-%m-%d %H:%M')

    if any([True for element in ["stop_min", "stop_max"] if element in filters]):
        query_filters["stop"] = dict()
        if "stop_min" in filters:
            query_filters["stop"]["$gte"] = datetime.datetime.strptime(filters["stop_min"], '%Y-%m-%d %H:%M')
        if "stop_max" in filters:
            query_filters["stop"]["$lte"] = datetime.datetime.strptime(filters["stop_max"], '%Y-%m-%d %H:%M')

    if "tags" in filters:
        tags_list = list(filters["tags"].split(","))
        query_filters["tags"] = {"$all": tags_list}

    pipeline = [
        {
            "$match": query_filters
        },
        {
            "$project": {"array": True,
                         "name": "$name",
                         "start": {
                             "$dateToString": {
                                 "format": "%Y-%m-%d %H:%M",
                                 "date": "$start"
                             }
                         },
                         "stop": {
                             "$dateToString": {
                                 "format": "%Y-%m-%d %H:%M",
                                 "date": "$start"
                             }
                         },
                         "tags": "$tags",
                         "_id": 0
                         }
        }
    ]

    query = list(Event.objects(__raw__=query_filters).aggregate(*pipeline))

    return json.loads(json.JSONEncoder().encode(query))





