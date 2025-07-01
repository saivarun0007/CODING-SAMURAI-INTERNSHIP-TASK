## Autonomous Driving Simulation - AI Powered Application
Welcome to the Autonomous Driving Simulation - AI Powered Application developed using Python (Pygame) & AI!

This project is part of the **Coding Samurai Internship Program** and showcases a simulation of an AI-powered self-driving car navigating through a path by detecting pixel colors on a predefined track.

## 🎯 Project Overview
This simulation showcases:

✔ 🛣️ A realistic static track background
✔ 🚗 A self-driving car using raycasting logic
✔ 🧱 Defined virtual barriers
✔ 🎮 Minimalist controls for simplicity and clarity

## 🚗 Features

✔ 📷 Realistic visual track layout using image background
✔ 🚗 Single autonomous car with sensor-based decision logic
✔ 🧱 Barriers created from custom point maps
✔ 💡 Easily extendable to add sensor visuals or more cars
✔ 🔄 Smooth car rotation and movement
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

4. Watch the car drive autonomously across the map using simple AI logic!

 ## 📁 Folder Structure

Autonomous Driving Simulation/
│
├── Autonomous Driving Simulation_Main Program File.py   # Core simulation loop
├── track_barriers.py                                    # Barrier points defining the track limits
├── basic_car.py                                         # Basic car movement + raycasting
├── car/
│   └── car.png                                          # Image asset for the single car
└── track/
    └── track.png                                        # Background image for the simulation track

## 📌 Notes

Commented-out lines in the code allow you to toggle:

✔ Sensor ray visuals
✔ Wall barrier display
✔ You can modify the barrier points in track_barriers.py for a new layout
✔ This is a logic-based simulation, not machine learning

## 🎮 Controls

| Action              | Control          |
| ------------------- | -----------------|
| Toggle driving mode | 🖱️ Mouse Click   |
| Exit the simulation | ❌ Close Window  |

✔ Click anywhere on the window to start or stop the car.
✔ The car will navigate based on wall input from track_barriers.py.

## 📄 License
This project is developed solely for educational purposes under the Coding Samurai Internship Program.

## 🙏 Acknowledgements
- Developed by CHANDRUPATLA SAI VARUN

- Internship Project: Coding Samurai

- Simulation powered by Pygame