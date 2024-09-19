# Description of this program:
 *  This program uses common algorithms and linear algebra found in Computer Graphics Algorithms. The program uses numpy and vedo, a 
 *  popular Python computer graphics library, to generate a 3D animated robot arm. This arm has multiple different joints with each
 *  section of the arm being placed on a different plane, and the connection being calculated through transition matrices between
 *  the different planes. Each plane needs to be created through a transition matrix from the previous plane so each plane is created
 *  with respect to the previous.