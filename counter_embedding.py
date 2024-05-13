src = "train.skels" # Change to the chose skels
trainv2 = "face/train.skels" # Target skels

# Conter Embedding
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


## For Equal Scaling

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


# For Multi-scaling ( better code compared to equal scaling )

def process_keypoints(line):
    keypoints = line.strip().split()
    processed_keypoints = []
    
    for i in range(0, len(keypoints), 268):  
        for j in range(i, i + 268, 2):
            x = float(keypoints[j])
            y = float(keypoints[j + 1])

            if (j - i) // 2 in range(23, 91): 
                x = x
                y = y
            else:  # For the rest
                x *= 0
                y *= 0

            processed_keypoints.extend([x, y])
    
    return " ".join(f"{value}" for value in processed_keypoints)

count = 0

with open(src, "r") as f:
    with open(trainv2, "a") as w:
        for line in f:
            content = process_keypoints(line)
            
            line = add_counter(content)
            w.write(line + "\n")
            
            count += 1

print(count) #Sanity Check for Results