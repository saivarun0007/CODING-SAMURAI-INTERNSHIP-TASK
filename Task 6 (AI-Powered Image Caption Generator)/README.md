# 📝 AI Image Caption Generator & Editor

This project is a **Streamlit web application** that lets users **upload and edit images**, and then generates **AI-powered captions** using the **BLIP (Bootstrapped Language-Image Pretraining)** model from Hugging Face.

---

## 🚀 Features

- Upload any image (JPG, PNG, WEBP)
- Rotate, crop, flip, adjust brightness and contrast
- Automatically generate intelligent captions using a vision-language model
- Generate multiple caption variants
- View model details, image stats, and pixel distribution
- Download edited images and captions

---

## 📦 Built With

- 🧠 [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) model (via Hugging Face Transformers)
- 🔥 PyTorch
- 🖼️ Pillow
- 📊 Matplotlib
- 🧪 NumPy
- 🌐 Streamlit

---

## ✅ Requirements

Install these dependencies:

```bash
✔ pip install streamlit 
✔ pip install torch 
✔ pip install torchvision 
✔ pip install transformers 
✔ pip install Pillow 
✔ pip install matplotlib 
✔ pip install numpy 
```

---

## 🖥️ How to Run this Program

=> Open CMD or PowerShell 
(Press Windows + R, type cmd, and press Enter).

=> Go to your project folder
(cd "C:\Users\Name\Folder\AI-Powered Image Caption Generator-main").

=> Run the app using Streamlit
(streamlit run app.py).

=> 🌐 Your app will open in the browser at:
(http://localhost:8501).

---

## 🧠 About the Model

✔ Model: BLIP (Salesforce/blip-image-captioning-base)
✔ Framework: PyTorch
✔ Trained for: Image captioning
✔ Device: Automatically uses GPU if available, else CPU

---

## 📂 Project Structure

Image-Caption-Generator-main/
│
├── main_file.py                        # Main Streamlit application
├── README.md                    # Project overview and usage guide
├── LICENSE                      # Open-source MIT license
│
├── .streamlit/                  # (Optional) Streamlit configuration
    └── config.toml              # Theme and layout settings

---

## 🔒 License

This project is for educational and personal portfolio use.