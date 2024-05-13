import os
import cv2
import numpy as np
from rtmlib import Wholebody
import concurrent.futures



##############

# The code provided is similar to the one from the main paper, with the addition of reading and writing files. Similar to the demo.ipynb file

###############

test_folder_path = os.path.join("simple")
test_file_path = os.path.join(test_folder_path, "test.files") # files to read from
output_file_path = os.path.join(test_folder_path, "test.skels") # Output file for DWPose poses

device = 'cpu'  
backend = 'onnxruntime'  
openpose_skeleton = True 

wholebody = Wholebody(to_openpose=openpose_skeleton,
                      mode='performance', 
                      backend=backend, device=device)

def process_image(image_file):

    img = cv2.imread(image_file)
    keypoints, _ = wholebody(img)
    new_keys = np.array(keypoints).flatten()
    return new_keys
    

with open(test_file_path, "r") as input_file, open(output_file_path, "a") as output_file:
    count = 0
    for line in input_file:
        count += 1
        if count >= 0: # This if statemetn is not needed ( just in case the program stopped running we can change the "0" to something else )
            line = line.strip()
            # Replace it with the directory to your dataset
            image_folder_path = os.path.join("PHOENIX-2014-T-release-v3", "PHOENIX-2014-T", "features", "fullFrame-210x260px", line)
            if os.path.isdir(image_folder_path):  # Check if the path is a directory
                image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path)]

                for img_file in image_files:
                    keypoint = process_image(img_file)
                    keypoints_str = " ".join(map(str, keypoint))
                    output_file.write(keypoints_str + " ")

                output_file.write("\n")