import streamlit as st
import cv2
from datetime import datetime


st.title("Motion Detector")
start = st.button("start camera")

if start :
    st_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True :
        now = datetime.now()
        day = now.strftime("%A")
        time = now.strftime("%H:%M:%S")
        check,frame = camera.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        lines = [day, time]
        x, y = 50, 50
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2
        color = (255, 255, 255)
        line_height = 30  # adjust based on font size

        for i, line in enumerate(lines):
            cv2.putText(frame, line, (x, y + i * line_height), font, font_scale, color, thickness)
        st_image.image(frame)