import os
import cv2
import numpy as np
from rtmlib import Wholebody
import concurrent.futures


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
    if img is not None:
        keypoints, _ = wholebody(img)
        return image_file, np.array(keypoints).flatten()
    return image_file, None

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

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future_to_file = {executor.submit(process_image, image_file): image_file for image_file in image_files}
                    
                    results = {}
                    for future in concurrent.futures.as_completed(future_to_file):
                        results[future_to_file[future]] = future.result()

                    sorted_results = [results[image_file] for image_file in image_files if results[image_file][1] is not None]

                    for keypoints in sorted_results[1]: # Make it so that it is sorted back in sequence
                        keypoints_str = " ".join(map(str, keypoints))
                        output_file.write(keypoints_str + " ")
                
                    output_file.write("\n")