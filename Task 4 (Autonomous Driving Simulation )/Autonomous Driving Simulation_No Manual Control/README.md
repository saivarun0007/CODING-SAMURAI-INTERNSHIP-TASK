## Autonomous Driving Simulation - AI Powered Application
Welcome to the Autonomous Driving Simulation - AI Powered Application developed using Python (Pygame) & AI!

This project is part of the **Coding Samurai Internship Program** and showcases a simulation of an AI-powered self-driving car navigating through a path by detecting pixel colors on a predefined map.

## 🚗 Features
✔ Real-time simulation of self-driving logic
✔ Camera-based path detection using pixel color (green sensor)
✔ Directional control (turning logic for up, right, down)
✔ Map-following behavior based on road pixels
✔ Smooth Pygame window rendering
✔ Adjustable speed and frame rate
✔ Minimalist and clean UI layout
✔ 100% Python-based lightweight application

## 🛠 Requirements
Ensure you have the following installed:

Python 3.x (preferably 3.9+)

Required Python libraries:
    pip install pygame

## 🚀 Quick Start
1. Clone or download the repository.

2. Place your map and car image files in the correct folders (maps/ and cars/).

3. Run the program:
    python Autonomous Driving Simulation_Main Program File.py

4. Watch the car drive autonomously across the map using simple AI logic!

 ## 📁 Folder Structure
Autonomous-Driving-Simulation/
├── Autonomous Driving Simulation_Main Program File.py  # Main simulation script
├── maps/
│   └── map6.png                                        # Road map used for navigation
├── cars/
│   └── car6.png                                        # Car image asset
├── README.md                                           # Documentation
└── LICENSE                                             # License file

## 🤖 How It Works
The car uses a simulated green pixel sensor placed in front of it. Based on pixel color at key points (up, down, right), it makes navigation decisions.

1. Turns right if the front path is blocked and right is available.

2. Turns down if right is blocked and downward is open.

3. Rotates the car image accordingly to match the turning direction.

4. Continues moving forward if the path ahead is open (white path represented by RGB (255, 255, 255)).

## 🎮 Controls
There are no manual controls. The simulation runs automatically based on the AI logic and predefined map.

## 📄 License
This project is developed solely for educational purposes under the Coding Samurai Internship Program.

## 🙏 Acknowledgements
- Developed by CHANDRUPATLA SAI VARUN

- Internship Project: Coding Samurai

- Simulation powered by Pygame