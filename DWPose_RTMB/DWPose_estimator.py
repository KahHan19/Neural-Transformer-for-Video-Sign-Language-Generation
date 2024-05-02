import os
import cv2
import numpy as np
from rtmlib import Wholebody
import concurrent.futures

# Define the path to the directory containing the test.file
test_folder_path = os.path.join("simple")
# Define the path to the test.file
test_file_path = os.path.join(test_folder_path, "test.files")
output_file_path = os.path.join(test_folder_path, "test.skels")

device = 'cpu'  # cpu, cuda
backend = 'onnxruntime'  # opencv, onnxruntime, openvino
openpose_skeleton = True 

wholebody = Wholebody(to_openpose=openpose_skeleton,
                      mode='performance',  # 'performance', 'lightweight', 'balanced'. Default: 'balanced'
                      backend=backend, device=device)

# Function to process images and return keypoints along with the image file
def process_image(image_file):
    img = cv2.imread(image_file)
    if img is not None:
        keypoints, _ = wholebody(img)
        return image_file, np.array(keypoints).flatten()
    return image_file, None

# Open the test.file and read its contents line by line
with open(test_file_path, "r") as input_file, open(output_file_path, "a") as output_file:
    count = 0
    for line in input_file:
        count += 1
        if count >= 0:
            print(count)
            # Remove any leading or trailing whitespace characters
            line = line.strip()
            # Construct the full path to the image folder using the line content
            image_folder_path = os.path.join("PHOENIX-2014-T-release-v3", "PHOENIX-2014-T", "features", "fullFrame-210x260px", line)
            if os.path.isdir(image_folder_path):  # Check if the path is a directory
                image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path)]

                # Process images asynchronously
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    # Submit image processing tasks
                    future_to_file = {executor.submit(process_image, image_file): image_file for image_file in image_files}
                    
                    # Store results in a dictionary to maintain the order
                    results = {}
                    for future in concurrent.futures.as_completed(future_to_file):
                        image_file = future_to_file[future]
                        results[image_file] = future.result()

                    # Sort results based on the order of image files
                    sorted_results = [results[image_file] for image_file in image_files if results[image_file][1] is not None]

                    # Write keypoints to output file for this image folder
                    for image_file, keypoints in sorted_results:
                        keypoints_str = " ".join(map(str, keypoints))
                        output_file.write(keypoints_str + " ")
                
                    # Write a newline character to separate keypoints of different folders
                    output_file.write("\n")