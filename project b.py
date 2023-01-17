import numpy as np
import matplotlib.pyplot as plt

def hdiff_finder(ang, flag):
    M = 20       
    g = 9.8         
    V = 2000         
    Cd = 0.01      
    dt = 0.5         

    t = [0]                         
    vx = [V*np.cos(ang/180*np.pi)]  
    vy = [V*np.sin(ang/180*np.pi)]
    x = [0]                 
    y = [0]

    drag=Cd*V                     

    ax = [-(drag*np.cos(ang/180*np.pi))/M ]          
    ay = [-g-(drag*np.sin(ang/180*np.pi)/M) ]

    dt = 0.2

    counter = 0
    while (y[counter] >= 0):                   
        t.append(t[counter]+dt)                 
        
        
        vx.append(vx[counter]+dt*ax[counter]) 
        vy.append(vy[counter]+dt*ay[counter])

        x.append(x[counter]+dt*vx[counter])
        y.append(y[counter]+dt*vy[counter]) 
        if(abs(x[counter]+dt*vx[counter] - 50000) < 200 and flag == False):
            return float(abs(y[counter]+dt*vy[counter] - 2000))
        elif(abs(x[counter]+dt*vx[counter] - 50000) < 200):
            break
   

        vel = np.sqrt(vx[counter+1]**2 + vy[counter+1]**2)  
        drag = Cd*vel                                 
        ax.append(-(drag*np.cos(ang/180*np.pi))/M)     
        ay.append(-g-(drag*np.sin(ang/180*np.pi)/M))
        
        counter = counter +1

    if(flag):
        plt.plot(x, y, 'ro')
        plt.ylabel("y (m)")
        plt.xlabel("x (m)")
        plt.show()
    
    return 2000

CNT = 5000
mnDiff = 2000
curDegree = 0
for i in range(1, CNT + 1):
    tmpDiff = hdiff_finder(i * (90/CNT), False)
    if(tmpDiff < mnDiff):
        curDegree = (i * (90/CNT))
        mnDiff = tmpDiff
print("With precison of", mnDiff, ", We have Theta is equal to :", curDegree)
hdiff_finder(curDegree, True)
