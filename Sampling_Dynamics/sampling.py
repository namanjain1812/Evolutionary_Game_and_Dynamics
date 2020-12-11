import ternary
import numpy as np
    ## Boundary and Gridlines
scale =1
figure, tax = ternary.figure(scale=scale)

    # Draw Boundary and Gridlines
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=0.2, color="black")

    # Set Axis labels and Title
fontsize = 20
tax.set_title("Sampling Dynamics", fontsize=fontsize)

    # Remove default Matplotlib Axes
#tax.clear_matplotlib_ticks()

#ternary.plt.show()


def w(i,p,matrix):
    t=0
    u=0
    z=1
    if(i==0):
        for j in range(3):
            z=1
            for k in range(1,3):
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
                z*=u
            t+=z*p[j]
        return t
    if(i==1):
        for j in range(3):
            z=1
            for k in {0,2}:
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
                if(matrix[k][2]<matrix[1][j]):
                    if(matrix[k][2]==matrix[1][j]):
                        u+=p[2]/2.0
                    else:
                        u+=p[2]
                z*=u
            t+=z*p[j]
        return t
    if(i==2):
        for j in range(3):
            z=1
            for k in {0,1}:
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
                if(matrix[k][2]<matrix[2][j]):
                    if(matrix[k][2]==matrix[2][j]):
                        u+=p[2]/2.0
                    else:
                        u+=p[2]
                z*=u
            t+=z*p[j]
        return t



points=[]
i=0
h=0.0001
p_0=[0.2,0.4,0.4]
f=[0,0,0]
matrix=[[2,5,8],[1,4,7],[0,3,6]]

while(i<100000):
    f[0]=w(0,p_0,matrix)
    f[1]=w(1,p_0,matrix)
    f[2]=w(2,p_0,matrix)
    p_0[0]+=h*(f[0]- p_0[0])
    p_0[1]+=h*(f[1]- p_0[1])
    p_0[2]+=h*(f[2]- p_0[2])
    points.append(p_0[:])
    i+=1
    
#ternary.plot(points)
tax.plot(points, linewidth=2.0, label="Curve")
tax.ticks(axis='lbr', multiple=0.2, linewidth=1, tick_formats="%.1f")
tax.legend()
tax.show()


