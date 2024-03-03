# https://en.wikipedia.org/wiki/Angle_of_attack
def coefficient_of_lift(angle_of_attack_degrees):
    if angle_of_attack_degrees < -5:
        return 0
    elif angle_of_attack_degrees > 10:
        return 1.5
    else:
        return 0.5 + 1 / 10 * angle_of_attack_degrees
