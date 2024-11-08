import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

x = np.linspace(-2, 2, 100)

fig, ax = plt.subplots()
line, = ax.plot(x, f(x))
def animate(i):
    line.set_ydata(f(x + i/10) )
    return line,

ax.grid(True)
ani = FuncAnimation(fig, animate, frames=100, interval=20, blit=True)
#ani.save('d:/Programming/Python for Physicist/04 Matplotlib/Animation/sine_wave_animation.gif', writer='imagemagick')
plt.show()