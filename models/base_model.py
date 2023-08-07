#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):

        dateformat = '%Y-%m-%dT%H:%M:%S.%f'
        kwargs.pop('__class__', None)

        if ('id' in kwargs):
            self.id = str(kwargs['id'])
        else:
            self.id = str(uuid.uuid4())

        if ('created_at' not in kwargs):
            self.created_at = datetime.now().isoformat()
        else:
            creation_date = kwargs.get('created_at')
            self.created_at = datetime.strptime(creation_date, dateformat)

        if ('updated_at' not in kwargs):
            self.updated_at = datetime.now().isoformat()
        else:
            updatedate = kwargs.get('updated_at')
            self.updated_at = datetime.strptime(updatedate, dateformat)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        instance_dict = self.__dict__
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict

