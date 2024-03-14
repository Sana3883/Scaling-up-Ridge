:import cv2
import os
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing.image import load_img
import numpy as np
import glob
import shutil
from tensorflow.keras.models import Model

# Define the path to the directory containing video files
Video_path = '<path_to_your_video_files>/*.mkv'

# Get a sorted list of all video files in the specified directory
movie_ses_1 = sorted(glob.glob(Video_path))

# Load pre-trained VGG16 model
base_model = VGG16()
base_model.summary()

# Define a model that extracts features up to the 'fc2' layer of VGG16
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

# Initialize an empty list to store frame features
list_f_T = []

# Loop through each video file
for name in movie_ses_1:
    print(name)

    # Open the video file for reading
    vidcap = cv2.VideoCapture(name)
    count = 0
    success = True

    # Loop through video frames
    while success:
        success, frame = vidcap.read()
        fps = 30
        Rate = 1  # Interval for extracting frames
        if count % (Rate * fps) == 0:  # Extract frames based on interval
            cv2.imwrite('frames/frame %d.jpg' % count, frame)
        count += 1
    print("Done!")

    # Initialize lists to store frame numbers and features
    list_n = []
    list_f = []

    # Path to the directory containing extracted frames
    path = 'frames'
    
    # Get a list of all frame files in the directory
    filenames2 = glob.glob(path + "/*.jpg")

    # Extract frame numbers from filenames
    for x in filenames2:
        s = x
        start = s.find('/frame') + 7
        end = s.find('.')
        x_p = s[start:end]
        list_n.append(x_p)
    list_n.sort(key=int)

    # Extract features for each frame
    for i in range(len(list_n) - 1):
        img_path = 'frames/' + 'frame ' + list_n[i] + '.jpg'
        img = image.load_img(img_path, target_size=(224, 224))
        x_img = image.img_to_array(img)
        x_img = np.expand_dims(x_img, axis=0)
        x_img = preprocess_input(x_img)
        avg_pool_features = model.predict(x_img)
        features_reduce = avg_pool_features.squeeze()
        list_f.append(features_reduce)

    # Convert list of frame features to numpy array
    frame_features_s = np.array(list_f)
    print(frame_features_s.shape)


    list_f_T.append(list_f)
        

    # Remove all frame files after processing
    files = glob.glob('frames/*')
    for f in files:
        os.remove(f)

# Save the extracted frame features as a numpy array
np.save('stimuli.npy', list_f_T)

