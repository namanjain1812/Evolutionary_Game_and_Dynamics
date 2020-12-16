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
    ax.plot(cartesian_points[:,0],cartesian_points[:,1],cartesian_points[:,2],c=c)


def w(i,p,matrix):
    t=0
    u=0
    z=1
    if(i==0):
        for j in range(4):
            z=1
            for k in range(1,4):
                u=0
                if(matrix[k][0]<=matrix[0][j]):
                    if(matrix[k][0]==matrix[0][j]):
                        u+=p[0]/2.0
                    else:
                        u+=p[0]
                if(matrix[k][1]<=matrix[0][j]):
                    if(matrix[k][1]==matrix[0][j]):
                        u+=p[1]/2.0
                    else:
                        u+=p[1]
                if(matrix[k][2]<matrix[0][j]):
                    if(matrix[k][2]==matrix[0][j]):
                        u+=p[2]/2.0
                    else:
                        u+=p[2]
                if(matrix[k][3]<matrix[0][j]):
                    if(matrix[k][3]==matrix[0][j]):
                        u+=p[3]/2.0
                    else:
                        u+=p[3]
                z*=u
            t+=z*p[j]
        return t
    if(i==1):
        for j in range(4):
            z=1
            for k in {0,2,3}:
                u=0
                if(matrix[k][0]<=matrix[1][j]):
                    if(matrix[k][0]==matrix[1][j]):
                        u+=p[0]/2.0
                    else:
                        u+=p[0]
                if(matrix[k][1]<=matrix[1][j]):
                    if(matrix[k][1]==matrix[1][j]):
                        u+=p[1]/2.0
                    else:
                        u+=p[1]
                if(matrix[k][2]<=matrix[1][j]):
                    if(matrix[k][2]==matrix[1][j]):
                        u+=p[2]/2.0
                    else:
                        u+=p[2]
                if(matrix[k][3]<=matrix[1][j]):
                    if(matrix[k][3]==matrix[1][j]):
                        u+=p[3]/2.0
                    else:
                        u+=p[3]
                z*=u
            t+=z*p[j]
        return t
    if(i==2):
        for j in range(4):
            z=1
            for k in {0,1,3}:
                u=0
                if(matrix[k][0]<=matrix[2][j]):
                    if(matrix[k][0]==matrix[2][j]):
                        u+=p[0]/2.0
                    else:
                        u+=p[0]
                if(matrix[k][1]<=matrix[2][j]):
                    if(matrix[k][1]==matrix[2][j]):
                        u+=p[1]/2.0
                    else:
                        u+=p[1]
                if(matrix[k][2]<=matrix[2][j]):
                    if(matrix[k][2]==matrix[2][j]):
                        u+=p[2]/2.0
                    else:
                        u+=p[2]
                if(matrix[k][3]<=matrix[2][j]):
                    if(matrix[k][3]==matrix[2][j]):
                        u+=p[3]/2.0
                    else:
                        u+=p[3]
                z*=u
            t+=z*p[j]
        return t
    if(i==3):
        for j in range(4):
            z=1
            for k in {0,1,2}:
                u=0
                if(matrix[k][0]<=matrix[3][j]):
                    if(matrix[k][0]==matrix[3][j]):
                        u+=p[0]/2.0
                    else:
                        u+=p[0]
                if(matrix[k][1]<=matrix[3][j]):
                    if(matrix[k][1]==matrix[3][j]):
                        u+=p[1]/2.0
                    else:
                        u+=p[1]
                if(matrix[k][2]<=matrix[3][j]):
                    if(matrix[k][2]==matrix[3][j]):
                        u+=p[2]/2.0
                    else:
                        u+=p[2]
                if(matrix[k][3]<=matrix[3][j]):
                    if(matrix[k][3]==matrix[3][j]):
                        u+=p[3]/2.0
                    else:
                        u+=p[3]
                z*=u
            t+=z*p[j]
        return t



def plot(p_0):
    points=[]
    i=0
    h=0.0001
    f=[0,0,0,0]
    matrix=[[4.5,2.5,2.5,0.5],[5.5,3.5,1.5,-0.5],[4,3.5,2,1.5],[5,4.5,1,0.5]]
    points.append(p_0[:])
    while(i<100000):
        f[0]=w(0,p_0,matrix)
        f[1]=w(1,p_0,matrix)
        f[2]=w(2,p_0,matrix)
        f[3]=w(3,p_0,matrix)
        p_0[0]+=h*(f[0]- p_0[0])
        p_0[1]+=h*(f[1]- p_0[1])
        p_0[2]+=h*(f[2]- p_0[2])
        p_0[3]+=h*(f[3]- p_0[3])
        points.append(p_0[:])
        i+=1
    return points

p_1=[0.1,0.1,0.1,0.7]
p_2=[0.1,0.1,0.7,0.1]
p_3=[0.1,0.7,0.1,0.1]
p_4=[0.7,0.1,0.1,0.1]
fig = plt.figure()
ax = Axes3D(fig) #Create a 3D plot in most recent version of matplot

plot_ax() #call function to draw tetrahedral outline

label_points() #label the vertices

#plot_3d_tern(plot(p_0),'b') #call function to plot df1
plot_3d_tern(plot(p_1),'r')
plot_3d_tern(plot(p_2),'g')
plot_3d_tern(plot(p_3),'y')
plot_3d_tern(plot(p_4),'c')
plt.show()
