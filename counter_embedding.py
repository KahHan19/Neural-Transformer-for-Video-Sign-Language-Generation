src = "train.skels"
trainv2 = "face/train.skels"


def add_counter(preprocline):
    values = [float(m) for m in preprocline.strip().split()]
    x= 268
    start = 0
    length = len(values)
    xl = length//x

    for i in range(1, xl+1):
        if i == 1:
            start += x 
            values.insert(start , (i - 1) / xl)
        else:
            start += x+1
            values.insert(start , (i - 1) / xl)

    content = str(values)[1:-1].replace(', ', ' ')
    return content



# count = 0
# with open(src, "r") as f:
#     for line in f:
#         values = [float(m)/25 for m in line.strip().split()]
#         content = " ".join(f"{value:.4f}" for value in values)
#         line = add_counter(content)
#         with open(trainv2, "a") as w:
#             w.write(line + "\n")
#         count += 1

# print(count)



def process_keypoints(line):
    # Split the line into individual keypoint coordinates
    keypoints = line.strip().split()
    processed_keypoints = []
    
    for i in range(0, len(keypoints), 268):  # Iterate through each image's keypoints
        for j in range(i, i + 268, 2):
            x = float(keypoints[j])
            y = float(keypoints[j + 1])

            # Modify specific keypoints as per the requirements
            if (j - i) // 2 in range(23, 91):  # For index 23-90
                x = x
                y = y
            else:  # For the rest
                x *= 0
                y *= 0

            # Append the modified keypoint coordinates
            processed_keypoints.extend([x, y])
    
    # Return the processed keypoints as a formatted string
    return " ".join(f"{value:.4f}" for value in processed_keypoints)

count = 0

with open(src, "r") as f:
    with open(trainv2, "a") as w:
        for line in f:
            # Process the keypoints
            content = process_keypoints(line)
            
            # Write the processed keypoints into the new file
            line = add_counter(content)
            w.write(line + "\n")
            
            count += 1

print(count)


# count = 0
# with open(src, "r") as f:
#     for line in f:
#         if count <= 5010:
#             with open(trainv2, "a") as w:
#                 w.write(line)
#         count += 1

# print(count)