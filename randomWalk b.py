import matplotlib.pyplot as plt
import numpy as np
from random import choice
class RandomWalk:
    def __init__(self,num_points=50):
        self.num_points=num_points
        self.x_values=[np.random.randint(0,50)]
        self.y_values=[np.random.randint(0,50)]
    def fill(self):
        while len(self.x_values)<self.num_points:
            x_direction=choice([-1,1])
            x_distance=choice([0,0.5,1,1.5,2])
            x_step=x_direction*x_distance
            y_direction=choice([-1,1])
            y_distance=choice([0,0.5,1,1.5,2])
            y_step=y_direction*y_distance
            if x_step==0 and y_step==0:
                continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw=RandomWalk()
rw.fill()
plt.plot(rw.x_values[0],rw.y_values[0],"rv-")
plt.plot(rw.x_values[-1],rw.y_values[-1],"yv-")
plt.plot(rw.x_values[1:49],rw.y_values[1:49],"bo-")
plt.show()