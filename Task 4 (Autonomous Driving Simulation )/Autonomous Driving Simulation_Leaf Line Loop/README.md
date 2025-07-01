## Autonomous Driving Simulation - AI Powered Application
Welcome to the Autonomous Driving Simulation - AI Powered Application developed using Python (Pygame) & AI!

This project is part of the **Coding Samurai Internship Program** and showcases a simulation of an AI-powered self-driving car navigating through a path by detecting pixel colors on a predefined track.

## 🎯 Project Overview
This simulation showcases an AI-controlled car driving on a predefined track while avoiding boundaries using virtual sensors and basic decision-making logic.

This version includes:

✔ 🏁 Realistic racetrack background
✔ 💡 Visual ray-based sensors
✔ ✨ Car trail effect
✔ 🛡️ Toggleable structural overlays (rays + barriers)

## 🚗 Features

✔ 🛣️ Realistic test track (image background)
✔ 🚗 Car with sensor rays to detect barriers
✔ 📏 Raycasting and collision avoidance
✔ ✨ Car trail with fading effect
✔ 🎮 Mouse toggle for drive & sensor structure display
✔ 📐 Structured barrier collision detection

## 🛠 Requirements
Ensure you have the following installed:

Python 3.x (preferably 3.9+)

Required Python libraries:
    pip install pygame

## 📌 Notes

✔ This is a non-ML simulation based on logic and vector math.
✔ Car sensors use rays to detect distances from barriers.
✔ Trails fade dynamically to visualize past movement.
✔ This version is a more immersive upgrade over the ellipse-track version.

## 🚀 Quick Start
1. Clone or download the repository.

2. Place your track and car image files in the correct folders (track/ and car(s)/).

3. Run the program:
    python Autonomous Driving Simulation_Main Program File.py

4. Watch the car drive autonomously across the map using simple AI logic!

 ## 📁 Folder Structure
Autonomous Driving Simulation/
│
├── Autonomous Driving Simulation_Main Program File.py   # Main game loop & logic
├── test_track_barriers.py                               # Track barrier structure (walls)
├── improved_car.py                                      # Car class with improved sensor logic
├── car/
│   └── car.png                                          # Image asset for the car
└── track/
    └── test_track.png                                   # Background image for the simulation


## 🎮 Controls

| Action                          | Control                |
| ------------------------------- | -----------------------|
| Toggle autonomous driving       | 🖱️ Left Mouse Click    |
| Toggle rays + barrier structure | 🖱️ Right Mouse Click   |
| Exit the simulation             | ❌ Close Window        |

✔ Left click anywhere to start/stop the car.

✔ Right click to toggle sensor rays and visible barriers.


## 📄 License
This project is developed solely for educational purposes under the Coding Samurai Internship Program.

## 🙏 Acknowledgements
- Developed by CHANDRUPATLA SAI VARUN

- Internship Project: Coding Samurai

- Simulation powered by Pygame