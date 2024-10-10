from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()
servo = gpg.init_servo()
my_distance_sensor = gpg.init_distance_sensor()
servo.rotate_servo(94)


def main(speed):
    gpg.set_speed(speed)
    gpg.drive_cm(100)
    gpg.set_speed(300)
    gpg.drive_cm(100)

def obstacle_detection():
    if my_distance_sensor <= 200:
        gpg.stop()

if __name__ == main:
    SPEED = 150
    main(speed=SPEED)


