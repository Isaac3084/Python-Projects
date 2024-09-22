import cv2
import face_recognition

image = face_recognition.load_image_file("image.jpg")
face_locations = face_recognition.face_locations(image)
