# Rapport de projet

## Groupe
* Marwan TRAGHA
* Koceila KEMICHE

## Description des choix importants d'implémentation

Nous avons, au cours de ce projet, implémenté différents comportements permettant de visiter au mieux une arène découpée en cases.
Nos comportements suivent une architecture de subsomption.

Comportement principal : 
* comportement_traqueur : Nos robots se déplacent de façon à recouvrir le maximum de surface. Lorsqu'un robot rencontre un ennemi il le poursuit pour recouvrir la surface derrière lui.
Les priorités sont définies comme suit : 

- Si un ennemi nous suit on se retourne de façon à se placer derrière lui -> On essaye ici de contrer les comportements similaires au nôtre. Cette priorité est la plus élevée car on veut limiter au maximum la surface que l'on couvre lorsque l'on est suivi.

- Si on croise un allié on l'évite en prenant une direction aléatoire -> L'aléatoire permet de limiter les comportements pré-définis pour ne pas avoir de "tendance de déplacements" et donc couvrir un maximum de surface. 
Cette priorité est assez élevée, cela nous permet de sortir des situations de blocage entrainées par un comportement traqueur. Ainsi, si un robot croise un allié bloqué, ce dernier va choisir une direction aléatoire et donc sortir de son blocage.

- Si on croise un ennemi on le suit -> On couvre ainsi la surface derrière un ennemi. En théorie on a donc k robots de plus que l'adversaire (k étant le nombre de robots suivis, un robot suivi ne marquera qu'un point pour son équipe). 
De plus on peut tirer avantage du comportement adverse, le robot traqueur suivra exactement le même comportement que sa proie. Exemple : Si la stratégie adverse consiste à explorer les chemins difficilement accessibles, notre robot traqueur explorera ses chemins.

- Si on croise un chemin on l'emprunte -> Cela permet de couvrir un maximum de surface en accédant à des zones difficilement atteignables.
Pour entrer dans un chemin, on procède comme suit :

METTRE PHOTO PAINT

- Sinon on évite -> Comportement de Braitenberg pour éviter les murs.

Autres comportements :
* comportement_traqueur_explorateur : 
Nos robots sont répartis de la façon suivante : 6 traqueurs, 2 explorateurs. 
Les traqueurs sont plus simples que dans comportement_traqueur, ils évitent les alliés et les murs et suivent les ennemis.
Les explorateurs doivent emprunter les chemins qu'ils trouvent pour couvrir un maximum de surface.
Après avoir commencé à tester ce comportement, nous avons trouvé qu'il était plus judicieux de ne pas réserver des places à des explorateurs mais plutôt d'ajouter leur comportement aux traqueurs. 

* comportement_traqueur_sauveteur : 
Nos robots sont répartis de la façon suivante : 6 traqueurs, 2 sauveteurs. 
Les traqueurs suivent comportement_traqueur_explorateur à la seule différence qu'ils utilisent leur capteur arrière pour repérer un allié. Si un allié se positionne derrière eux, ils reculent. Cela permet de sortir des situations de blocage.
Les sauveteurs eux suivent leurs alliés, et se positionne derrière pour les tracter hors des attroupements.
Ce comportement s'est révélé être assez difficile à implémenter. Nous avons donc préféré augmenter la priorité d'éviter les alliés tout en augmentant le nombre de capteurs les détectant (en ajoutant les capteurs gauche et droite).

## Description des résultats

Nous avons testé comportement_traqueur contre le comportement Champion de base.
Les tests se sont effectués sur chaque arène (de 0 à 5), 10 fois par arène.

Histogrammes résultats : 

### Arène 0 : 

PHOTO HISTOGRAMME

### Arène 1 : 

PHOTO HISTOGRAMME

### Arène 2 : 

PHOTO HISTOGRAMME

### Arène 3 : 

PHOTO HISTOGRAMME

### Arène 4 :

PHOTO HISTOGRAMME

### Arène 5 : 

PHOTO HISTOGRAMME

## Conclusion

Au cours de ce projet nous nous sommes rendus compte que les comportements trop compliqués (type comportement_traqueur_sauveteur) était difficile à mettre en place et pas forcément performants.
Comme les robots n'ont aucune connaissance préalable sur l'arène, les comportements adverses, etc... il est vite apparu qu'une stratégie simple mais polyvalente était la meilleure solution.
Selon nous, comportement_traqueur répond très bien à cette idée. 
En effet l'idée globale est très simple, repasser derrière ses ennemis pour les empêcher de marquer des points.
La polyvalence vient de la traque (adoption du comportement adverse) mais aussi des améliorations apportées :
- Se protéger contre une stratégie du même type (qui est notre principal point faible)
- Éviter les alliés aléatoirement pour couvrir un maximum de surface
- Entrer dans les chemins pour marquer des points dans des zones difficilements atteignables

Nous allons maintenant voir si cette idée plutôt théorique se vérifie face aux comportements de nos camarades.