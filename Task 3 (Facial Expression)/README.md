# Real-Time Emotion Detection using DeepFace

This project performs real-time emotion detection using your webcam, leveraging the powerful `DeepFace` library. The detected emotion is displayed live on the video stream.

---

## ✅ Features

* Real-time emotion recognition
* Displays dominant emotion on the video frame
* Smooth quitting options:

  * Press `ESC` to exit
  * Press `Q` or `q` to exit
  * Close the window using the window close (X) button

---

## 🛠️ Requirements

### Python Version

* **Python 3.9.x**
  *(Note: DeepFace and TensorFlow versions used here work best with Python 3.9)*

### Required Python Modules

The following Python modules are required:

* opencv-python
* deepface
* tensorflow-cpu==2.10.1 *(recommended for Windows to avoid GPU DLL issues)*

You can install all required packages using:

### `requirements.txt` content:

```bash
opencv-python
deepface
tensorflow-cpu==2.10.1
```

---

## ⚠ Important Note (Model Download)

* **On the first run**, DeepFace will automatically download its pre-trained model files into a folder called:

```
C:\Users\<YourUsername>\.deepface\
```

* You can move this entire `.deepface` folder into your project directory to make your project fully portable. 

* Once moved, the code automatically uses the local `.deepface` folder.

* If models are not found locally, DeepFace will download them again automatically.

---

## 🚀 How to Run

1️⃣ Clone or copy the project folder.

2️⃣ Ensure that Python 3.9 is installed and the required modules are installed.

3️⃣ Make sure your webcam is connected and accessible.

---

## 📂 Project Structure Example

```
Emotion-Detection-Project/
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- .deepface/  (downloaded models folder)
```

---

## 🙏 Credits

* DeepFace: [https://github.com/serengil/deepface](https://github.com/serengil/deepface)
* OpenCV

---

## 🔒 License

This project is for educational and personal portfolio use.
