import db
from pprint import pprint

def get_characters():
    return db.get_characters()

def get_resource():
    return db.get_resource()

def sort_by_id():
    dbdict = db.get_characters()
    sorted_dict = dict(sorted(dbdict.items(), key=lambda item: item[1]['id']))
    char_list = []
    for c in sorted_dict.keys():
        char_list.append(c)
    return char_list

def sort_by_type():
    dbdict = db.get_characters()
    sorted_dict = dict(sorted(dbdict.items(), key=lambda item: item[1]['type']))
    char_list = []
    for c in sorted_dict.keys():
        char_list.append(c)
    return char_list

def sort_by_name(chars):
    chars.sort()
    return chars
        
def get_char_id(char):
    dic = db.get_characters()
    return dic[char]["id"]

def get_character(char):
    dic = db.get_characters()
    return dic[char]