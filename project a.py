
import math 
import matplotlib.pyplot as plt

def equationroots(x, y, z): 

    discri = y * y - 4 * x * z
    sqrtval = math.sqrt(abs(discri)) 

    if discri > 0:
        return ((-y + sqrtval)/(2 * x), (-y - sqrtval)/(2 * x))

    elif discri == 0:
        return (-y / (2 * x)) 
    else:
        print("Something went wrong")
        return -1


M = 20; V_0 = 2; R = 50; H = 2; B = 0.01; G = 9.8

R *= 1000
V_0 *= 1000
H *= 1000

x = (G * R * R) / (2 * V_0 * V_0)
y = (-1 * R)
z = ((G * R * R) / (2 * V_0 * V_0)) + H

tan_TH = equationroots(x, y, z)

theta1r = math.atan(tan_TH[0])
theta1 = math.degrees(math.atan(tan_TH[0]))
theta2r = math.atan(tan_TH[1])
theta2 = math.degrees(math.atan(tan_TH[1]))

print("A) Theta can have two values:", theta1, "&", theta2)

curx = 0
cury = 0
T = 0
X_1 = []
Y_1 = []
while(curx < R):
    X_1.append(curx)
    Y_1.append(cury)
    T += 0.1
    curx = T * V_0 * math.cos(theta1r)
    cury = T * V_0 * math.sin(theta1r) - 0.5 * G * T * T

plt.plot(X_1, Y_1, label = "line 1")

curx = 0
cury = 0
T = 0
X_2 = []
Y_2 = []
while(curx < R):
    X_2.append(curx)
    Y_2.append(cury)
    T += 0.1
    curx = T * V_0 * math.cos(theta2r)
    cury = T * V_0 * math.sin(theta2r) - 0.5 * G * T * T

plt.plot(X_2, Y_2, label = "line 2")

plt.ylabel("y (m)")
plt.xlabel("x (m)")
plt.show()

