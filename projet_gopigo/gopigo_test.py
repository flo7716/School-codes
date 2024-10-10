from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()
servo = gpg.init_servo()
my_distance_sensor = gpg.init_distance_sensor()
servo.rotate_servo(94)
gpg.close_left_eye()
gpg.close_right_eye()


def main(speed):
    gpg.set_speed(300)
    gpg.drive_cm(100)



if __name__ == main:
    SPEED = 150
    main(speed=SPEED)


