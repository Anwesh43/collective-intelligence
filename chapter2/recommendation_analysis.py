from recommendations import *
import matplotlib.pyplot as plt
print critics['Lisa Rose']['Snakes on a Plane']
x = []
y_snakes_on_plane = []
index = 1
for k,v in critics.items():
    x.append(index)
    y_snakes_on_plane.append(v['Snakes on a Plane'])
    index = index+1
plt.plot(x,y_snakes_on_plane)
plt.show()
