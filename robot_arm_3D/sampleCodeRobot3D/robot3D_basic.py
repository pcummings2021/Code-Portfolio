#!/usr/bin/env python
# coding: utf-8

# ![](https://github.com/eraldoribeiro/assignment_robotarm2D/blob/main/robotArm01.png?raw=1)
# *Figure 1*: A two-dimensional articulated arm. The articulated structure has 3 local coordinate frames each one centered at a joint. For each part, the local x-axis is aligned with the part.  
# 
# Consider the arm structure shown in Figure 1. Assume the following values for the arm configuration: 
# - The location of the first joint (i.e., the one that is attached to the ground support) is ${\bf p}_1 = \left(3,2\right)^\mathsf{T}$. 
# - The lengths of the parts are $L_1 = 5$ and  $L_2 = 8$.

# In[1]:


"""
Spheres and cylinders
"""
# (adapted from http://www.glowscript.org)
from vedo import *

#settings.default_backend = 'ipyvtk' # or 2d, ipyvtk, ipygany, panel, itk, or vtk


# In[2]:


# Color of robot arm
robotColor = "green"
jointColor = "white"


# In[3]:


def RotationMatrix(theta, axis_name):
    """ calculate single rotation of \(\theta\) matrix around x,y or z
        code from: https://programming-surgeon.com/en/euler-angle-python-en/
    input
        theta = rotation angle(degrees)
        axis_name = 'x', 'y' or 'z'
    output
        3x3 rotation matrix
    """

    c = np.cos(theta * np.pi / 180)
    s = np.sin(theta * np.pi / 180)
    if axis_name =='x':
        rotation_matrix = np.array([[1, 0,  0],
                                    [0, c, -s],
                                    [0, s,  c]])
    if axis_name =='y':
        rotation_matrix = np.array([[ c,  0, s],
                                    [ 0,  1, 0],
                                    [-s,  0, c]])
    elif axis_name =='z':
        rotation_matrix = np.array([[c, -s, 0],
                                    [s,  c, 0],
                                    [0,  0, 1]])
    return rotation_matrix


# In[4]:


def createCoordinateFrameMesh():
    """Returns the mesh representing a coordinate frame
    Args:
      No input args
    Returns:
      F: vedo.mesh object (arrows for axis)
      
    """     
    
    _shaft_radius = 0.05
    _head_radius = 0.10
    _alpha = 1
    
    
    # x-axis as an arrow  
    x_axisArrow = Arrow(
                        start_pt=(0, 0, 0),
                        end_pt=(1, 0, 0),
                        s=None,
                        shaft_radius=_shaft_radius,
                        head_radius=_head_radius,
                        head_length=None,
                        res=12,
                        c='red',
                        alpha=_alpha
    )

    # y-axis as an arrow  
    y_axisArrow = Arrow(
                        start_pt=(0, 0, 0),
                        end_pt=(0, 1, 0),
                        s=None,
                        shaft_radius=_shaft_radius,
                        head_radius=_head_radius,
                        head_length=None,
                        res=12,
                        c='green',
                        alpha=_alpha
    )

    # z-axis as an arrow  
    z_axisArrow = Arrow(
                        start_pt=(0, 0, 0),
                        end_pt=(0, 0, 1),
                        s=None,
                        shaft_radius=_shaft_radius,
                        head_radius=_head_radius,
                        head_length=None,
                        res=12,
                        c='blue',
                        alpha=_alpha
    )
    
    originDot = Sphere(pos=[0,0,0], 
                       c="black", 
                       r=0.10)


    # Combine the axes together to form a frame
    F = x_axisArrow + y_axisArrow + z_axisArrow + originDot
    
    
    return F


# In[5]:


def getLocalFrameMatrix(R_ij, t_ij): 
    """Returns the matrix representing the local frame
    Args:
      R_ij: rotation of Frame j w.r.t. Frame i 
      t_ij: translation of Frame j w.r.t. Frame i 
    Returns:
      T_ij: Matrix of Frame j w.r.t. Frame i. 
      
    """             
    # Rigid-body transformation [ R t ]
    T_ij = np.block([[R_ij,                t_ij],
                     [np.zeros((1, 3)),       1]])
    print('\n')
    print('T_ij = ', np.array2string(T_ij, prefix='        '))
    
    return T_ij


# In[6]:


plt = Plotter()
axes = Axes(xrange=(0,20), yrange=(-2,6), zrange=(0,6))

L1 = 5   # Length of link 1
L2 = 8   # Length of link 2

phi1 = 15     # Rotation angle of part 1 in degrees
phi2 = -30    # Rotation angle of part 2 in degrees
phi3 = 0      # Rotation angle of the end-effector in degrees


# ### Construct a local frame and its local transformation matrix
# Construct the matrix representing Frame ${\mathcal F}\{1\}$. All local frames are initially represented w.r.t. to their previous frame, i.e., The matrix of Frame ${\mathcal F}\{i\}$ is written w.r.t. Frame ${\mathcal F}\{i-1\}$. In the case of Frame ${\mathcal F}\{1\}$, we write it w.r.t. Frame ${\mathcal F}\{0\}$, which is the global or world frame. 

# In[7]:


# Construct the matrix for Frame 1 (written w.r.t. to Frame 0, which is the previous frame)
# Frame 1 is the base of the arm.  

R_01 = RotationMatrix(phi1, axis_name = 'z')   # Rotation matrix
p1   = np.array([[3],[2], [0.0]])              # Frame's origin (w.r.t. previous frame)
t_01 = p1                                      # Translation vector

# Matrix of Frame 1 w.r.t. Frame 0 (i.e., the world frame)
T_01 = getLocalFrameMatrix(R_01, t_01)

# Create the coordinate frame mesh and transform
Frame1Arrows = createCoordinateFrameMesh()

# Now, let's create a cylinder and add it to the local coordinate frame
link1_mesh = Cylinder(r=0.4, 
                      height=L1, 
                      pos = (L1/2,0,0),
                      c="yellow", 
                      alpha=.8, 
                      axis=(1,0,0)
                      )

Frame1 = Frame1Arrows + link1_mesh


Frame1.apply_transform(T_01)  
#plt.show(Frame1, 
#         axes, 
#         viewup="z").close()


# ### Construct a local frame and its local transformation matrix
# Construct the matrix representing Frame ${\mathcal F}\{2\}$, written w.r.t. 
# Frame ${\mathcal F}\{1\}$. 

# In[8]:


# Frame 2 (w.r.t. to Frame 1)

R_12 = RotationMatrix(phi2, axis_name = 'z')   # Rotation matrix
p2   = np.array([[L1],[0.0], [0.0]])           # Frame's origin (w.r.t. previous frame)
t_12 = p2                                      # Translation vector

# Matrix of Frame 2 w.r.t. Frame 1 
T_12 = getLocalFrameMatrix(R_12, t_12)

# Matrix of Frame 2 w.r.t. Frame 0 (i.e., the world frame)
T_02 = T_01 @ T_12

# Create the coordinate frame mesh and transform
Frame2Arrows = createCoordinateFrameMesh()

# Now, let's create a cylinder and add it to the local coordinate frame
link2_mesh = Cylinder(r=0.4, 
                      height=L2, 
                      pos = (L2/2,0,0),
                      c="yellow", 
                      alpha=.8, 
                      axis=(1,0,0)
                      )

Frame2 = Frame2Arrows + link2_mesh


Frame2.apply_transform(T_02)  
#plt.show([Frame1, Frame2], 
#         axes, 
#         viewup="z").close()


# ### Construct a local frame and its local transformation matrix
# Construct the matrix representing Frame ${\mathcal F}\{3\}$, written w.r.t. 
# Frame ${\mathcal F}\{2\}$. In this case, there is no rotation between the frames (see diagram in Figure 1). 

# In[9]:


# Frame 3 (w.r.t. to Frame 2)

R_23 = RotationMatrix(phi3, axis_name = 'z')   # Rotation matrix
p3   = np.array([[L2],[0.0], [0.0]])           # Frame's origin (w.r.t. previous frame)
t_23 = p3                                      # Translation vector

# Matrix of Frame 3 w.r.t. Frame 2 
T_23 = getLocalFrameMatrix(R_23, t_23)

# Matrix of Frame 3 w.r.t. Frame 0 (i.e., the world frame)
T_03 = T_01 @ T_12 @ T_23

# Create the coordinate frame mesh and transform
Frame3 = createCoordinateFrameMesh()

Frame3.apply_transform(T_03)  
plt.show([Frame1, Frame2, Frame3], 
         axes, 
         viewup="z").interactive()

plt.close()

# In[ ]:




