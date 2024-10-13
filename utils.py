import json, os

class File:
    __file_name = "data.json"
    @classmethod
    def save(cls, new_json_dict):
        with open(cls.__file_name, "w") as opened_file:
            json_object =  json.dumps(new_json_dict)
            opened_file.write(json_object)
            return new_json_dict
        
    
    @classmethod
    def read(cls):
        if os.path.exists(cls.__file_name):
            with open(cls.__file_name, "r") as opened_file:
                return json.load(opened_file)
        else:
            return cls.save({})
        
        
            