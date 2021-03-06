import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
from itertools import combinations
import pandas as pd

def plot_ax():               #plot tetrahedral outline
    verts=[[0,0,0],
     [1,0,0],
     [0.5,np.sqrt(3)/2,0],
     [0.5,0.28867513, 0.81649658]]
    lines=combinations(verts,2)
    for x in lines:
        line=np.transpose(np.array(x))
        ax.plot3D(line[0],line[1],line[2],c='0')

def label_points():  #create labels of each vertices of the simplex
    a=(np.array([1,0,0,0])) # Barycentric coordinates of vertices (A or c1)
    b=(np.array([0,1,0,0])) # Barycentric coordinates of vertices (B or c2)
    c=(np.array([0,0,1,0])) # Barycentric coordinates of vertices (C or c3)
    d=(np.array([0,0,0,1])) # Barycentric coordinates of vertices (D or c3)
    labels=['a','b','c','d']
    cartesian_points=get_cartesian_array_from_barycentric([a,b,c,d])
    for point,label in zip(cartesian_points,labels):
        if 'a' in label:
            ax.text(point[0],point[1]-0.075,point[2], label, size=16)
        elif 'b' in label:
            ax.text(point[0]+0.02,point[1]-0.02,point[2], label, size=16)
        else:
            ax.text(point[0],point[1],point[2], label, size=16)

def get_cartesian_array_from_barycentric(b):      #tranform from "barycentric" composition space to cartesian coordinates
    verts=[[0,0,0],
         [1,0,0],
         [0.5,np.sqrt(3)/2,0],
         [0.5,0.28867513, 0.81649658]]

    #create transformation array vis https://en.wikipedia.org/wiki/Barycentric_coordinate_system
    t = np.transpose(np.array(verts))        
    t_array=np.array([t.dot(x) for x in b]) #apply transform to all points

    return t_array

def plot_3d_tern(df,c='1'): #use function "get_cartesian_array_from_barycentric" to plot the scatter points
#args are b=dataframe to plot and c=scatter point color
    bary_arr=df
    cartesian_points=get_cartesian_array_from_barycentric(bary_arr)
    ax.scatter(cartesian_points[:,0],cartesian_points[:,1],cartesian_points[:,2],c=c)

def max(f):
    if((f[0]>=f[1]) and (f[0]>=f[2]) and f[0]>=f[3]):
        return f[0]
    elif((f[1]>=f[0]) and (f[1]>=f[2]) and f[1]>=f[3]):
        return f[1]
    elif((f[2]>=f[0]) and (f[2]>=f[1]) and f[2]>=f[3]):
        return f[2]
    elif((f[3]>=f[0]) and (f[3]>=f[1]) and f[3]>=f[2]):
        return f[3]
   
points=[]
i=0
h=0.005
p_0=[1,0,0,0]
matrix=[[4.5,2.5,2.5,0.5],[5.5,3.5,1.5,-0.5],[4,3.5,2,1.5],[5,4.5,1,0.5]]
points.append(p_0[:])
while(i<1000):
    f=np.dot(matrix,p_0)
    if(max(f)==f[0]):
        p_0[0]+=h*(1-p_0[0])
        p_0[1]+=-h*p_0[1]
        p_0[2]+=-h*p_0[2]
        p_0[3]+=-h*p_0[3]
        
        points.append(p_0[:])
        i+=1
        continue
    if(max(f)==f[1]):
        p_0[1]+=h*(1-p_0[1])
        p_0[0]+=-h*p_0[0]
        p_0[2]+=-h*p_0[2]
        p_0[3]+=-h*p_0[3]
        points.append(p_0[:])
        #print(points)
        i+=1
        continue
    if(max(f)==f[2]):
        p_0[2]+= h*(1-p_0[2])
        p_0[1]+= -h*p_0[1]
        p_0[0]+= -h*p_0[0]
        p_0[3]+=-h*p_0[3]
        #print(p_0)
        points.append(p_0[:])
        i+=1
        continue
    if(max(f)==f[3]):
        p_0[3]+= h*(1-p_0[3])
        p_0[1]+= -h*p_0[1]
        p_0[0]+= -h*p_0[0]
        p_0[2]+=-h*p_0[2]
        points.append(p_0[:])
        i+=1


fig = plt.figure()
ax = Axes3D(fig) #Create a 3D plot in most recent version of matplot

plot_ax() #call function to draw tetrahedral outline

label_points() #label the vertices

plot_3d_tern(points,'b') #call function to plot df1

plt.show()
