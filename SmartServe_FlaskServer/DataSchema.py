
def makeSchema(recieved_array):
    
    key_names={"screen_size", "4g", "5g", "rear_camera_mp", "front_camera_mp",
                    "internal_memory", "ram", "battery", "weight", "release_year", "days_used","normalized_new_price"}

    dict_schema = {key: value for key, value in zip(key_names, recieved_array)}
    
    return dict_schema