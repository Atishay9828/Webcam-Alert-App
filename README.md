# 🚀 Smart Webcam Motion Alert System
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)

A real-time, Python-powered webcam security application that utilizes computer vision to detect motion and automatically sends email alerts with captured images.

Built by Atishay Jain.

## 1. Methodology

┌────────────────────────────┐
│ Webcam Video Feed          │
│ (Continuous Capture)       │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ Frame Pre-processing &     │
│ Background Registration    │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ Absolute Difference &      │
│ Gaussian Blur (OpenCV)     │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┴───────────────────────────┐
│ Contour Detection & Thresholding                       │
│ (Check if contour area > 5000 pixels)                  │
└─────────┬────────────────────────────┬─────────────────┘
          │ (Motion Detected)          │ (No Motion)
          ↓                            ↓
┌────────────────────────────┐ ┌────────────────────────────┐
│ Save Frame locally         │ │ Ignore / Continue Loop     │
│ (Draw Bounding Box)        │ │                            │
└─────────┬──────────────────┘ └────────────────────────────┘
          ↓
┌────────────────────────────┴───────────────────────────┐
│ Asynchronous Email Alert                               │
│ (Spawns a background thread on object exit)            │
└─────────┬──────────────────────────────────────────────┘
          ↓
┌────────────────────────────┐
│ Auto-cleanup               │
│ (Deletes temp images)      │
└────────────────────────────┘

The methodology follows a robust frame-differencing pipeline. The system registers the initial frame as a background and compares subsequent frames against it. Once it detects a contour larger than a specified threshold, it records the object. When the object exits the frame, a background thread is initiated to email the best frame to the user, while another thread cleans up the temporary image cache.

## 2. Description & Overview

This system monitors an environment through your webcam and processes the visual data to provide security insights. 

It automatically detects:
- **Motion presence** (Object entry and exit)
- **Object localization** (Drawing bounding boxes around the moving entity)

The system works locally and operates asynchronously so that the camera feed is never interrupted while sending email notifications.

### Core Components & Features
* 🧠 **OpenCV Vision Pipeline**: Uses frame differencing, Gaussian blur, and contour tracking to isolate motion reliably.
* 📧 **Asynchronous Email Alerts**: Spawns Python `Thread` objects to send an email with a secure SSL connection using `smtplib` and `EmailMessage` without lagging the camera.
* 🧹 **Auto-Cleaning Image Cache**: Periodically clears out old capture frames using `glob` and `os` commands so local storage isn't cluttered.
* 🎥 **Streamlit Viewer (Bonus)**: Includes a simplified Streamlit web-app version (`simple.py`) with real-time timestamp and day overlays on the video feed.

## 3. Visuals & Screenshots

*(Placeholder for future screenshots - Add a GIF of the Streamlit app or the OpenCV bounding box here)*

## 4. Input / Output & Processing

### Input
- **Video Source**: Standard internal or external webcam (via `cv2.VideoCapture(0)`).

### Output
- **Local GUI**: Real-time bounding box projection on moving subjects via OpenCV window.
- **Email Notification**: Sends an email to the configured address (e.g., `Subject: New object detected`) with an attached `.png` image of the motion.

## 5. Execution Environment & Setup

- **Language**: Python 3.x
- **Computer Vision**: OpenCV (`cv2`)
- **Web App UI**: Streamlit
- **Standard Libraries**: `threading`, `glob`, `os`, `time`, `smtplib`, `imghdr`

### 🛠️ Local Setup

1. **Install Requirements**:
   Ensure you have the required packages installed:
   ```bash
   pip install opencv-python streamlit
   ```

2. **Configure Environment Variables**:
   In `emailing.py`, ensure your environment variable for the email app password is set, or replace the `os.getenv` line directly:
   ```python
   password = os.getenv("Password of mail ..") # Or insert your App Password directly
   ```

3. **Run the Primary Security Script**:
   ```bash
   python main.py
   ```
   Press `q` on the video window to quit and trigger a final cleanup.

4. **Run the Streamlit Web Viewer (Optional)**:
   ```bash
   streamlit run simple.py
   ```

## 6. Results Summary

### Key Outcomes
- Consistently identifies human or large object motion with minimal false positives.
- The use of threading ensures that the heavy I/O bound task of sending emails does not freeze the main thread responsible for the camera loop.
- Automatically handles the management of image attachments, preventing storage bloat over long monitoring periods.

## 7. Key Observations

- Registering the initial frame as a static background requires the camera to be stable during the first few seconds of initialization.
- Decoupling the email alert system into a separate background daemon significantly improves inference smoothness.
- `cv2.absdiff` combined with a `cv2.threshold` is an incredibly performant and cheap way to establish a baseline motion detection system before resorting to heavy Deep Learning models.

## 8. Conclusion & Future Work

This project demonstrates a highly efficient, threaded vision application perfect for home security monitoring and lightweight object tracking.

### 🔥 Future Improvements
- Implement a YoloV8 object detection model to distinguish between humans, pets, and cars.
- Add configuration files (`.yaml` or `.json`) to adjust contour threshold limits dynamically.
- Store logging information (time of entry, duration of presence) into a lightweight SQLite database.
- Deploy a persistent web-dashboard for viewing historical logs.

## 🤝 Contributing
PRs welcome — open an issue or drop a suggestion.

## 📜 License
This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.

✅ Use for personal and educational purposes
✅ Modify and adapt the code
❌ Use for commercial purposes

## 👤 Author
**Atishay Jain**
