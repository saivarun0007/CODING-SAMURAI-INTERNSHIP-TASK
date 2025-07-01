## Autonomous Driving Simulation - AI Powered Application
Welcome to the Autonomous Driving Simulation - AI Powered Application developed using Python (Pygame) & AI!

This project is part of the **Coding Samurai Internship Program** and showcases a simulation of an AI-powered self-driving car navigating through a path by detecting pixel colors on a predefined track.

## 🎯 Project Overview
This simulation demonstrates the core logic of autonomous driving using:

✔ Ellipse-shaped racetrack
✔ Inner and outer boundary constraints
✔ Path-following algorithm
✔ Sensor-like raycasting for obstacle detection

Real-time vehicle movement

## 🚗 Features

✔ 🚗 Simulated car movement
✔ 📏 Raycasting sensors to detect surroundings
✔ 🧠 Decision-making based on environmental input
✔ 🎮 Toggle driving mode with mouse click
✔ 🧱 Inner and outer track boundaries
✔ 🛣️ Visual path drawing for reference

## 🛠 Requirements
Ensure you have the following installed:

Python 3.x (preferably 3.9+)

Required Python libraries:
    pip install pygame

## 🚀 Quick Start
1. Clone or download the repository.

2. Place your tack and car image files in the correct folders (track/ and car(s)/).

3. Run the program:
    python Autonomous Driving Simulation_Main Program File.py

4. Watch the car drive autonomously across the map using simple AI logic!

 ## 📁 Project Structure

Autonomous Driving Simulation/
│
├── Autonomous Driving Simulation_Main Program File.py   # Main game loop & logic
├── ellipse_path.py                                      # Contains path, inner, outer track points
├── basic_car.py                                         # Car class with sensor and movement logic
└── car/
    └── car.png                                          # Image asset for the car

## 📌 Notes
The simulation is educational and for portfolio use only.
Car movement logic is built using simple vector math and sensor-based decision making.
This project does not use machine learning.

## 🎮 Controls
| Action                    | Control           |     
| ------------------------- | ------------------|  
| Toggle autonomous driving | 🖱️ Mouse Click   |
| Exit the simulation       | ❌ Window Close  |

✔ Click anywhere on the simulation window to start/stop the self-driving behavior.
✔ Close the window to exit the simulation.

## 📄 License
This project is developed solely for educational purposes under the Coding Samurai Internship Program.

## 🙏 Acknowledgements
- Developed by CHANDRUPATLA SAI VARUN

- Internship Project: Coding Samurai

- Simulation powered by Pygame & AI 
