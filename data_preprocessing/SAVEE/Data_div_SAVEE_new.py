import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt 
import os
import shutil
from PIL import Image

source_folder = "./AudioData_Train"
destination_folder = "./AudioData_Test"

for folder_name in os.listdir(source_folder):

    current_folder = source_folder + '\\' + folder_name
    for file_name in os.listdir(current_folder):
        
        source = current_folder + '\\' + file_name
        actor_id = file_name[0] + file_name[1] # 1 person for test
        if actor_id in ['JK']:

            if folder_name == 'Anger':
                destination = destination_folder + '\\Anger\\'
                shutil.move(source, destination)
            elif folder_name == 'Disgust':
                destination = destination_folder + '\\Disgust\\'
                shutil.move(source, destination)
            elif folder_name == 'Fear':
                destination = destination_folder + '\\Fear\\'
                shutil.move(source, destination)
            elif folder_name == 'Happy':
                destination = destination_folder + '\\Happy\\'
                shutil.move(source, destination)
            elif folder_name == 'Neutral':
                destination = destination_folder + '\\Neutral\\'
                shutil.move(source, destination)
            elif folder_name == 'Sad':
                destination = destination_folder + '\\Sad\\'
                shutil.move(source, destination)
            elif folder_name == 'Calm':
                destination = destination_folder + '\\Calm\\'
                shutil.move(source, destination)
            elif folder_name == 'Surprise':
                destination = destination_folder + '\\Surprise\\'
                shutil.move(source, destination)