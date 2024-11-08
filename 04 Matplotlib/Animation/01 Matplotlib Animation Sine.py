import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # Update the data
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)
plt.show()