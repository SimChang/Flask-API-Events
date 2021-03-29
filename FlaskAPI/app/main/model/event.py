import datetime

from .. import db


class Event(db.DynamicDocument):
    """
        Event model for storing event related documents
        The model is dynamic, it supports and saves attributes different from the listed ones
    """

    name = db.StringField(required=True, unique=True, max_length=100)
    start = db.DateTimeField(required=True, default=datetime.datetime.utcnow)
    stop = db.DateTimeField()
    tags = db.ListField(db.StringField(max_lenght=30))

    def __repr__(self):
        return "Event: '{}'".format(self.name)
