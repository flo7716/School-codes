#Hector Lamalle et Florian André
#IPSA
#Projet Gopigo

import turtle
import math
from easygopigo3 import EasyGoPiGo3
import time

gpg = EasyGoPiGo3()
servo = gpg.init_servo()
my_distance_sensor = gpg.init_distance_sensor()
servo.rotate_servo(94)
gpg.close_left_eye()
gpg.close_right_eye()

compteur = 0
position_x = 0
position_y = 0
orientation = 0
X = []
Y = []

def alarm():
    gpg.stop()
    while True:
        gpg.open_left_eye()
        gpg.open_right_eye()
        time.sleep(0.1)
        gpg.close_left_eye()
        gpg.close_right_eye()
        time.sleep(0.1)


def filtre(dist, angl):
    indices_a_supprimer = []

    for i in range(0, len(dist)-1):
        if abs(dist[i+1] - dist[i]) > 20 or dist[i] > 80:
            indices_a_supprimer.append(i)

    for index in reversed(indices_a_supprimer):
        dist.pop(index)
        angl.pop(index)

    if abs(dist[-1] - dist[-2]) > 20 or dist[-1] > 80:
        dist.pop(-1)
        angl.pop(-1)

    return dist, angl


def scan(posi_x, posi_y, orientation):
    x1 = 0
    x2 = 0
    gpg.open_left_eye()
    gpg.open_right_eye()
    distances = []
    angles_deg = []
    x = []
    y = []
    dist_cote = 0
    servo.rotate_servo(10)
    time.sleep(0.2)

    for n in range(30, 150, 2):
        servo.rotate_servo(n)
        correct_angl = n - 4    #check si c'est pas -13
        
        distances.append(round((my_distance_sensor.read_mm()*0.1),3))
        angles_deg.append(correct_angl)
        time.sleep(0.2)
        
    print(distances)
    print(angles_deg)
    correct_distances, correct_angles = filtre(distances, angles_deg)
    print(correct_distances)
    print(correct_angles)
    gpg.close_left_eye()
    gpg.close_right_eye()
    
    for n in correct_angles:
        n = math.degrees(n)

    for dist, angle_deg in zip(correct_distances, correct_angles):
        angle_rad = math.radians(angle_deg)
        if orientation == 0:
            x.append(posi_x + ((dist*10) * math.cos(angle_rad)))
            y.append(posi_y + ((dist*10) * math.sin(angle_rad)))
        elif orientation == -90:
            x.append(posi_x - ((dist*10) * math.sin(angle_rad)))
            y.append(posi_y + ((dist*10) * math.cos(angle_rad)))
        elif orientation == -180:
            x.append(posi_x - ((dist*10) * math.cos(angle_rad)))
            y.append(posi_y - ((dist*10) * math.sin(angle_rad)))
        else:
            x.append(posi_x + ((dist*10) * math.sin(angle_rad)))
            y.append(posi_y - ((dist*10) * math.cos(angle_rad)))
    
    dist_cote = correct_distances[0] * math.cos(correct_angles[0])

    print("Distance cote: ", dist_cote)

    maximum_distance = correct_distances[0] * math.sin(correct_angles[0])
    for dist, angle_deg in zip(correct_distances, correct_angles):
        if (dist * math.sin(angle_deg)) > maximum_distance:
            maximum_distance = (dist * math.sin(angle_deg))

    x1 = correct_distances[0] * math.cos(correct_angles[0])
    x2 = correct_distances[-1] * math.cos(correct_angles[-1])

    moitie_dist = (abs(x1-x2))/2
    print("moitie_dist: ", moitie_dist)

    return x, y, dist_cote, moitie_dist, maximum_distance



def mouvement(position_x, position_y, anc_orientation, distance_cote, moitie_distance, maximum_distance):
    a = 20
    b = 0
    gpg.turn_degrees(94)
    servo.rotate_servo(94)
    time.sleep(1)
    if my_distance_sensor.read_mm() < (abs(distance_cote*10) + 200):
        alarm()
    else:
        gpg.drive_cm(distance_cote + 30)  # voir la taille entre centre roue et sensor

    servo.rotate_servo(178)
    while my_distance_sensor.read_mm() < ((moitie_distance * 2) + (maximum_distance * 2)):
        gpg.drive_cm(5)
        a += 5
        b += 1
        if b > 6:
            alarm()

    gpg.turn_degrees(-94)
    servo.rotate_servo(94)
    gpg.drive_cm(moitie_distance + maximum_distance)
    gpg.turn_degrees(-94)

    if anc_orientation == 0:
        nv_orientation = 90
        nv_pos_x = position_x + (distance_cote*10 + a*10)
        nv_pos_y = position_y + maximum_distance*10 + moitie_distance*10

    elif anc_orientation == -90:
        nv_orientation = -180
        nv_pos_x = position_x - (maximum_distance*10 + moitie_distance*10)
        nv_pos_y = position_y + (distance_cote*10 + a*10)

    elif anc_orientation == -180:
        nv_orientation = -270
        nv_pos_x = position_x - (distance_cote*10 + a*10)
        nv_pos_y = position_y - (maximum_distance*10 + moitie_distance*10)

    else:
        nv_orientation = 0
        nv_pos_x = position_x + (maximum_distance*10 + moitie_distance*10)
        nv_pos_y = position_y - (distance_cote*10 + a*10)

    return nv_pos_x, nv_pos_y, nv_orientation


def afficher(X, Y):
    for x, y in zip(X, Y):
        turtle.goto(x, y)
        turtle.dot()


while my_distance_sensor.read_mm() > 205:
    gpg.forward()
gpg.stop()

while compteur < 4:
    x, y, distance_cote, moitie_distance, maximum_distance = scan(position_x, position_y, orientation)
    X.extend(x)
    Y.extend(y)

    position_x, position_y, orientation = mouvement(position_x, position_y, orientation, distance_cote, moitie_distance, maximum_distance)
    compteur += 1

afficher(X, Y)
turtle.done()


