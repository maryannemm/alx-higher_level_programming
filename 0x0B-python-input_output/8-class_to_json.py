#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary description of the object.
    """
    json_dict = {}
    
    for key, value in obj.__dict__.items():
        # Skip private attributes
        if not key.startswith("__"):
            # If the attribute is an instance of a Class, recursively call class_to_json
            if isinstance(value, type):
                json_dict[key] = class_to_json(value)
            else:
                json_dict[key] = value
    
    return json_dict

