import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from angle_of_attack import coefficient_of_lift

sns.set_theme(style="darkgrid")

# make data
x = np.linspace(-15, 30, 100)
y = [coefficient_of_lift(angle) for angle in x]

sns.lineplot(x="angle of attack (degrees)", y="coefficient of lift", data={
             "angle of attack (degrees)": x, "coefficient of lift": y})

plt.savefig("plot_angle_of_attack.png")