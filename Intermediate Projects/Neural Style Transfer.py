import numpy as np
from keras.applications import VGG19
from keras.preprocessing import image

model = VGG19(weights='imagenet', include_top=False)
content_image = image.load_img('content.jpg', target_size=(224, 224))
style_image = image.load_img('style.jpg', target_size=(224, 224))
