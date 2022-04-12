def avoider(sensors):
    translation = (1) * sensors["sensor_front"]["distance_to_wall"]
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"]
    return translation,rotation