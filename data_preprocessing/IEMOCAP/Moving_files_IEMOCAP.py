import pandas as pd
import os
import shutil


base_path = "./Classified_Excels_Excitment+Happy"
source_path = "./Data"
destination_path = "./Data_classified_EH_Train"
classes = ['Anger','Happy','Neutral','Sad']

iterator = 0
for current_file in os.listdir(base_path):
    iemocap_df = pd.read_csv(base_path + '/' + current_file, sep=';')
    for path in iemocap_df['path']:
        full_source_path = source_path + path
        full_destination_path = destination_path + classes[iterator]
        shutil.copy2(full_source_path, full_destination_path)
    iterator += 1

