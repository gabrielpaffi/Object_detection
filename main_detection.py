import detection_function
import armmovement

coordonnees_camera = [0, 0, 0, 0]
coordonnees_camera = detection_function.yolod()
xcentre_camera = coordonnees_camera[1][1]
ycentre_camera = coordonnees_camera[1][2]
xlongueur_camera = coordonnees_camera[1][3]
ylongueur_camera = coordonnees_camera[1][4]

print(xcentre_camera) ## xcentre
print(ycentre_camera) ## ycentre
print(xlongueur_camera) ## largeur
print(ylongueur_camera) ## hauteur


## changement de repère camera -> repère bras
## armmovement.ArmMovement(b[1][1], b[1][2])