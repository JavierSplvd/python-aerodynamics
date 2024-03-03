"""
L {\displaystyle L} is the lift force
ρ {\displaystyle \rho } is the air density
v {\displaystyle v} is the velocity or true airspeed
S {\displaystyle S} is the planform (projected) wing area
C L {\displaystyle C_{L}} is the lift coefficient at the desired angle of attack, Mach number, and Reynolds number[94]
"""
def get_lift(air_density, velocity, wing_area, lift_coefficient):
    return 0.5 * air_density * velocity ** 2 * wing_area * lift_coefficient