from json import load, dump, JSONDecodeError
import datetime

class FileStorage:
    __file_path='file.json'
    __objects={}

    def all(self):
        return (FileStorage.__objects)
        
    def new(self, obj):
        inst = obj.__class__.__name__
        idO = obj.id
        key = str(inst)+ '.' + str(idO)
        FileStorage.__objects[key] = obj

    def date_serialization(self, obj):
        if isinstance(obj.created_at, datetime) and isinstance(obj.updated_at, datetime):
            return (obj.isoformat())
        else:
            return obj.__dict__

    def save(self):
        insstances = FileStorage.__objects
        insstances_dict = {key: insstances[key].to_dict() for key in insstances.keys()}
        with open(FileStorage.__file_path, "w") as file:
            dump(insstances_dict, file)


    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                inst = load(file)
                from models.base_model import BaseModel
                for key, value in inst.items():
                    class_name, obj_id = key.split('.')
                    inst[key]['__class__'] = class_name
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
