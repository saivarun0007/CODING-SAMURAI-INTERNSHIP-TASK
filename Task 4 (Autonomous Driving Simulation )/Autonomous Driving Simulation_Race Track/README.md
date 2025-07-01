## Autonomous Driving Simulation - AI Powered Application (Dual Car Race Track Edition)
Welcome to the Autonomous Driving Simulation - AI Powered Application developed using Python (Pygame) & AI!

This project is part of the **Coding Samurai Internship Program** and showcases a simulation of an AI-powered self-driving car navigating through a path by detecting pixel colors on a predefined track.

## 🎯 Project Overview
This version pushes the boundaries of basic autonomous simulations by introducing:

✔ 🏁 A realistic racetrack
✔ 🚗🚗 Two AI-driven cars that avoid both walls and each other
✔ 🔍 Raycasting sensor-based navigation
✔ 🎛️ Toggleable structure view (sensors + barriers)

## 🚗 Features
✔ 🛣️ Realistic racetrack (image background)
✔ 🚗 Car 1 with sensor detection and obstacle avoidance
✔ 🚙 Car 2 that tracks and responds to Car 1's position
✔ 🧱 Car-to-car and wall collision logic
✔ 🔭 Toggleable ray visuals and boundary structure
✔ 💻 Pygame-based simulation, runs in real time
✔ 100% Python-based lightweight application

## 🛠 Requirements
Ensure you have the following installed:

Python 3.x (preferably 3.9+)

Required Python libraries:
    pip install pygame

## 🚀 Quick Start
1. Clone or download the repository.

2. Place your track and car image files in the correct folders (track/ and car(s)/).

3. Run the program:
    python Autonomous Driving Simulation_Main Program File.py

4.  Use the right mouse button & Watch the car drive autonomously across the track using simple AI logic!

 ## 📁 Folder Structure

Autonomous Driving Simulation/
│
├── Autonomous Driving Simulation_Main Program File.py   # Main simulation code
├── race_track_barriers.py                               # Track boundaries
├── improved_car.py                                      # Car class with AI & raycasting
├── cars/
│   ├── car1.png                                         # First car sprite
│   └── car2.png                                         # Second car sprite
└── track/
    └── race_track.png                                   # Background image for the racetrack


## 📌 Notes

✔ This simulation does not use machine learning.
✔ AI logic is rule-based with directional vector updates and raycasting.
✔ Car 2 behaves based on Car 1’s current position — simulating reactive driving.

## 🎮 Controls

| Action                          | Control                |
| ------------------------------- | -----------------------|
| Toggle autonomous driving       | 🖱️ Left Mouse Click    |
| Toggle rays + barrier structure | 🖱️ Right Mouse Click   |
| Exit the simulation             | ❌ Close Window        |

✔ Click anywhere with left mouse button to start or stop the simulation.
✔ Use the right mouse button to toggle sensor rays and track structures.

## 📄 License
This project is developed solely for educational purposes under the Coding Samurai Internship Program.

## 🙏 Acknowledgements
- Developed by CHANDRUPATLA SAI VARUN

- Internship Project: Coding Samurai

- Simulation powered by Pygame