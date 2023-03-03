# Parker Cummings
# CSE 4280 Computer Graphics Algorithms
# Dr. Ribeiro
# Transforming Point Clouds


import numpy as np
from vedo import *


# Creates the transition matrix from frame 1 w.r.t global frame 0
def frame_01(translation):
    # cos and sin functions use radians
    c = np.cos(45 * (np.pi / 180))
    s = np.sin(45 * (np.pi / 180))

    # creates transition matrix for a rotation about the z-axis
    t_01 = np.array([[c, -s, 0, translation[0]],
                     [s, c, 0, translation[1]],
                     [0, 0, 1, translation[2]],
                     [0, 0, 0, 1]])

    # returns transition matrix
    return t_01


# creates a transition matrix from local frame 2 w.r.t frame 1
def frame_12(translation):
    c = np.cos(40 * (np.pi / 180))
    s = np.sin(40 * (np.pi / 180))

    # creates transition matrix with rotation about the y-axis
    t_12 = np.array([[c, 0, s, translation[0]],
                     [0, 1, 0, translation[1]],
                     [-s, 0, c, translation[2]],
                     [0, 0, 0, 1]])

    # returns transition matrix
    return t_12


# creates transition matrix from frame 3 w.r.t frame 2
def frame_23(translation):
    c = np.cos(30 * (np.pi / 180))
    s = np.sin(30 * (np.pi / 180))

    # creates transition matrix with rotation about the y-axis
    t_23 = np.array([[c, 0, s, translation[0]],
                     [0, 1, 0, translation[1]],
                     [-s, 0, c, translation[2]],
                     [0, 0, 0, 1]])

    # returns transition matrix
    return t_23


# creates transition matrix from frame 4 w.r.t frame 3
def frame_34(translation):
    c = np.cos(15 * (np.pi / 180))
    s = np.sin(15 * (np.pi / 180))

    # creates transition matrix with rotation about the y-axis
    t_34 = np.array([[c, 0, s, translation[0]],
                     [0, 1, 0, translation[1]],
                     [-s, 0, c, translation[2]],
                     [0, 0, 0, 1]])

    # returns transition matrix
    return t_34


def main():
    # creating initial base and joint of arm
    joint0 = Sphere(r=0.5)
    arm_base = Cylinder(r=1.0, height=1.5, pos=(0, 0, 0))

    p1 = [10, 5, 0.75]  # first translation
    p1_ = [10, 5, 1.5]  # same frame, but sets sphere slightly above

    # creating transition matrices for the two meshes from frame 1 w.r.t frame 0
    T_01_base = frame_01(p1)
    T_01_joint = frame_01(p1_)

    # applying transformations
    arm_base.apply_transform(T_01_base)
    joint0.apply_transform(T_01_joint)

    link1 = Cylinder(r=0.5, height=8)  # Main arm link
    joint1 = Sphere(r=0.5)  # first arm joint

    p2 = [0, 0, 0]  # this frame does not translate w.r.t frame 1, only rotate

    # creating transition matrices for the meshes from frame 2 w.r.t frame 1
    T_12_link = frame_12(p2)
    T_12_joint = frame_12(p2)

    # because the vedo Cylinder object rotates from its center, it must be translated
    T_half_12 = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 4 + 0.25],  # translated half its length up the z-axis
                          [0, 0, 0, 1]])

    # forward kinematics, creating transition matrix for frame 2 w.r.t global frame 0
    T_02_link = T_01_joint @ T_12_link @ T_half_12
    T_half_12[2][3] = 8.25  # the sphere must be moved up the arm so it appears at the top
    T_02_joint = T_01_joint @ T_12_joint @ T_half_12

    # after transition matrices are created, the transformations are applied
    link1.apply_transform(T_02_link)
    joint1.apply_transform(T_02_joint)

    link2 = Cylinder(r=0.5, height=5)  # second arm link
    joint2 = Sphere(r=0.5)  # second arm joint

    p3 = [0, 0, 4] # new frame 3 will be translated 4 units on the z-axis w.r.t frame 2

    # creating transition matrices for the meshes from frame 3 w.r.t frame 2
    T_23_link = frame_23(p3)
    T_23_joint = frame_23([0, 0, 0])

    # because the vedo Cylinder object rotates from its center, it must be translated
    T_half_23 = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 2.5 + 0.25],  # half its length up the z-axis
                          [0, 0, 0, 1]])

    # forward kinematics, creating transition matrix for frame 3 w.r.t global frame 0
    T_03_link = T_02_link @ T_23_link @ T_half_23
    T_half_23[2][3] = 5.25
    T_03_joint = T_02_joint @ T_23_joint @ T_half_23

    # applying transformations to the meshes
    link2.apply_transform(T_03_link)
    joint2.apply_transform(T_03_joint)

    link3 = Cylinder(r=0.5, height=3)  # third arm link
    joint3 = Sphere(r=0.25)  # end effector

    p4 = [0, 0, 2.5]  # new frame 4 will be translated 0.5*(L4) on the z-axis w.r.t frame 3

    # creating transition matrices for the meshes from frame 4 w.r.t frame 3
    T_34_link = frame_34(p4)
    T_34_joint = frame_34([0, 0, 0])

    # because the vedo Cylinder object rotates from its center, it must be translated
    T_half_34 = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 1.5 + 0.125],  # half its length up the z-axis
                          [0, 0, 0, 1]])

    # forward kinematics, creating transition matrix for frame 4 w.r.t global frame 0
    T_04_link = T_03_link @ T_34_link @ T_half_34
    T_half_34[2][3] = 3.125
    T_04_joint = T_03_joint @ T_34_joint @ T_half_34

    # applying transformations to the meshes
    link3.apply_transform(T_04_link)
    joint3.apply_transform(T_04_joint)

    # creating x, y, and z-axis and sets the min and max ranges
    axes = Axes(xrange=(0, 20), yrange=(-2, 6), zrange=(0, 6))

    # creating vedo plotter
    plt = Plotter(size=(2100, 1200))
    plt.show(arm_base, joint0, link1, joint1, link2, joint2,
             link3, joint3, axes, viewup="z")


if __name__ == "__main__":
    main()
