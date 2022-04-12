# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Marwan TRAGHA
#  Prénom Nom: Koceila KEMICHE

def get_team_name():
    return "Picasso" # à compléter (comme vous voulez)

def step(robotId, sensors):

	translation = 1
	rotation = 0

	# Si on croise un ennemi proche on le suit (1)
	if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
		return follow()
	
	# On se déplace de façon à remplir le maximum de surface en évitant les murs et les alliés (2)
	if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1 : 
		rotation = 1 # rotation vers la droite
	elif sensors["sensor_front_right"]["distance"] < 1:
		rotation = -1 # rotation vers la gauche

	return translation, rotation

def follow():
	return 1, 0


"""
Idée de stratégie : 

On se déplace de façon à remplir le maximum de surface. Quand on rencontre un robot adverse on le suit de façon à peindre juste derrière lui.

ToDo : 
- (1) : Continuer à suivre un robot ennemi même s'il n'est pas devant nous (genre sur les côtés)
- (2) : Se déplacer dans la direction opposée si on croise un obstacle (allié ou mur)

Améliorations : 
- On peut séparer les robots en deux équipes. Des traqueurs qui suivront les adversaires et des remplisseurs qui optimise juste leurs déplacements pour remplir le maximum de surface.
- Si on se rend compte que l'on est suivi par un robot, on se replace derrière lui.
"""

"""
Exemple de comportement : 

if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        rotation = 0.5  # rotation vers la droite
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.5  # rotation vers la gauche

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

    return translation, rotation
"""
