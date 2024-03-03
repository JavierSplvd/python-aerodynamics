import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from lift import get_lift

sns.set_theme(style="darkgrid")

# make data
air_density = 1.225  # kg/m^3
wing_area = 16.2  # m^2, Cessna 172

velocity_km_h = np.linspace(87, 226, 100)  # km/h
velocity = velocity_km_h * 1000 / 3600  # m/s
lift_kg_A = [get_lift(air_density, v, wing_area, 0.5) /
             9.8 for v in velocity]  # N
lift_kg_B = [get_lift(air_density, v, wing_area, 1) /
             9.8 for v in velocity]  # N
lift_kg_C = [get_lift(air_density, v, wing_area, 1.5) /
             9.8 for v in velocity]  # N

sns.lineplot(
    x="velocity (m/s)",
    y="lift (kg)",
    data={"velocity (m/s)": velocity, "lift (kg)": lift_kg_A},
    label="Lift (kg) for C_L = 0.5"
)
sns.lineplot(
    x="velocity (m/s)",
    y="lift (kg)",
    data={"velocity (m/s)": velocity, "lift (kg)": lift_kg_B},
    label="Lift (kg) for C_L = 1"
)
sns.lineplot(
    x="velocity (m/s)",
    y="lift (kg)",
    data={"velocity (m/s)": velocity, "lift (kg)": lift_kg_C},
    label="Lift (kg) for C_L = 1.5"
)


plt.savefig("plot_lift.png")
