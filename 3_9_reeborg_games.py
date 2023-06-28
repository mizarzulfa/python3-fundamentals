# SAMPLE ONLY -don't run


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def anjay():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


counter = 6
while counter > 0:
    anjay()
    counter -= 1
