# Inverse Kinematics
1. [Introduction](#introduction)
2. [Algorithm](#algorithm)
3. [The code](#the-code)
4. [Change log](#change-log)

## Introduction
Kinematics is the study of motion without considering the cause of the motion, such as forces and torques. Inverse kinematics (IK) is the use of kinematic equations to determine the motion of a robot to reach a desired position. For example, to perform automated apple picking, a robotic arm needs precise motion from an initial position to a desired position between apples and manufacturing machines. The grasping end of a robot arm is designated as the end-effector. The robot configuration is a list of segments positions that are within the position limits of the robot model and do not violate any constraints the robot has.

Given the desired robot’s end-effector positions, inverse kinematics can determine an appropriate segment configuration for which the end-effectors move to the target pose.

Addapted from [MathWorks](https://fr.mathworks.com/discovery/inverse-kinematics.html)

## Algorithm
For each Segment of the Tentacle do :
* make Segment point towards the target
* set Point a so that Point b is on the target
* set Point b based on Point a
* set Point a to be the target for next segment

In the end, if there is a base, shift the hole Tentacle back to its base and proceed to the next frame of animation.

## The code
All the code is written using the [Engine](engine.py) library and a personnal [Vector](vector.py) class. The [Tentacle](tentacle.py) object is basically an array of [Segment](segment.py). The [Ball](ball.py) object is just a fancy target for the tentacle class. As always, the [main](main.py) file contains the core draw loop.

## Change log
1.  v0.1 : a first [Segment](segment.py) follows the mouse
2.  v1.0 : [Tentacle](tentacle.py) class
3.  v1.1 : implementation of a [ball](ball.py) object
4.  v2.0 : use of the [Engine](engine.py) renderer
5.  v2.1 : refractor
