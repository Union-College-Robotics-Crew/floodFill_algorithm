# Floodfill
This is a python implementation of the flood-fill algorithm. The aim of this program is to solve a 16x16 maze using this algorithm.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Project Status](#project-status)

## General Info
The program builds a 16x16 grid, with each cell containing a flood value. The flood value for each cell corresponds to number of moves it will take our robot to get to the center from that point. The four cells in the middle have a flood value of 0, and are designated as our center. Each cell also has positional value which allows the program to track the robots position in the maze. The robot will attempt to solve the maze by repeatedly moving toward the neighboring cell with the lowest flood value. As the robot encounters walls blocking the neighboring cells, it will update the flood values accordingly. The program will continue to run until the robot reaches the center. The API used is from the Micro Mouse Simulator (mms) which allowed us to simulate our robot. For informaton on mms, refer to, https://github.com/mackorone/mms. 

## Technolgies
* Python 3.9
* Micro Mouse Simulator API

## Setup
To simulate this program, download and install mms from https://github.com/mackorone/mms.
Once downloaded, click the "+" in the top right corner to add floodfill.py to your run command.

### Mac Run Command
![Screen Shot 2021-11-06 at 1 06 04 PM](https://user-images.githubusercontent.com/83914041/140617919-a00036db-5c58-4c58-8d47-fa31309c3859.png)

### Windows Run Command
Replace "Main.py" with "floodfill.py"
![Screen Shot 2021-11-06 at 1 10 18 PM](https://user-images.githubusercontent.com/83914041/140617994-cf3a6edc-fbda-4f34-bcca-1b8a9c0331c6.png)

## Project Status
The program currently works, and is able to consistently solve our mazes. However, we are still in the process of optimizing our code to run more efficently.



