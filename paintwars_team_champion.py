def get_team_name() : 
	return " Professor X"
def step(roboId,sensors) : 
	translation = 1 
	rotation = 0
	if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
		rotation = 0.5  # rotation vers la droite
	elif sensors["sensor_front_right"]["distance"] < 1:
		rotation = -0.5  # rotation vers la gauche

	return translation, rotation


