import os
import cv2
import numpy as np
from rtmlib import Wholebody
import concurrent.futures

test_file_path = "DWPose/valid.files"
output_file_path = "DWPose/chicken.skels"
counter = 0
bad = 0
z = 0
pop = 0

with open(test_file_path, "r") as input_file:
    for line in input_file:
        line = line.strip()
        image_folder_path = os.path.join("PHOENIX-2014-T-release-v3","PHOENIX-2014-T", "features","fullFrame-210x260px",line)
        if os.path.isdir(image_folder_path):
            counter += 1
            image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path)]
            for file_path in image_files:
                if os.path.exists(file_path):
                    z += 1
                else: 
                    pop += 1
        else: 
            bad += 1

print(counter)
print(bad)
print(z)
print(pop)