import ternary
import numpy as np
    ## Boundary and Gridlines
scale =1
figure, tax = ternary.figure(scale=scale)

    # Draw Boundary and Gridlines
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=0.2, color="black")
fontsize = 20

def diffe(list1,list2):
    list3=[0,0,0,0]
    for i in range(4):
        list3[i]=list1[i]-list2[i]
    return list3

def plot(p_0):
    points=[]
    i=0
    h=0.005
    e_0=[1,0,0,0]
    e_1=[0,1,0,0]
    e_2=[0,0,1,0]
    e_3=[0,0,0,1]
    matrix=[[-1,-1,-10,1000],[-1.5,-1,-1,1000],[2.4,0.5,0,-1000],[0,0,0,0]]
    points.append(p_0[:])
    while(i<500000):
        f=np.dot(matrix,p_0)
        p_0[0]+=h*(p_0[0]*np.dot(diffe(e_0,p_0),f))
        p_0[1]+=h*(p_0[1]*np.dot(diffe(e_1,p_0),f))
        p_0[2]+=h*(p_0[2]*np.dot(diffe(e_2,p_0),f))
        p_0[3]+=h*(p_0[3]*np.dot(diffe(e_3,p_0),f))
        points.append(p_0[:4])
        i+=1
    return points

p_0=[0.3,0.2,0.4,0.1]
p_1=[0.299,0.201,0.4,0.1]
tax.plot(plot(p_0), linewidth=1.0, label="Curve 1")
tax.plot(plot(p_1), linewidth=1.0, label="Curve 2")
tax.ticks(axis='lbr', multiple=0.2, linewidth=1, tick_formats="%.1f")
tax.legend()
tax.show()


