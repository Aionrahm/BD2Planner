import json_reader as jr

characters_db = ".db/characters.json"
resource_db = ".db/resource.json"

def get_characters():
    return jr.load_json(characters_db)

def get_resource():
    return jr.load_json(resource_db)

def post_characters():
    pass

def post_resource():
    pass