import sys
import math
import numpy as np
import cv2
import os
import _pickle as cPickle
import gzip
import subprocess
import torch

from rtmlib.visualization.dwdraw import draw_skeleton

from dtw import dtw
from constants import PAD_TOKEN

# Plot a video given a tensor of joints, a file path, video name and references/sequence ID
def plot_video(joints,
               file_path,
               video_name,
               references = None,
               skip_frames=1,
               sequence_ID= None):
    # Create video template
    FPS = (25 // skip_frames)
    video_file = file_path + "/{}.mp4".format(video_name.split(".")[0])
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    if references is None:
        video = cv2.VideoWriter(video_file, fourcc, float(FPS), (650, 650), True)
    elif references is not None:
        video = cv2.VideoWriter(video_file, fourcc, float(FPS), (1300, 650), True)  # Long

    num_frames = 0

    for (j, frame_joints) in enumerate(joints):

        # Reached padding
        if PAD_TOKEN in frame_joints:
            continue

        # Initialise frame of white
        frame = np.zeros((650, 650, 3), np.uint8) * 255

        # Cut off the percent_tok, multiply by 3 to restore joint size
        frame_joints = frame_joints[:-1]



        # Change the Scaling Here #
        for i, value in enumerate(frame_joints):
            if i in range(45,181):
                frame_joints[i] = value
            else:
                frame_joints[i] = value
                




        # Reduce the frame joints down to 2D for visualisation - Frame joints 2d shape is (48,2)
        frame_joints_2d = np.reshape(frame_joints, (1,134, 2))
        # Draw the frame given 2D joints
        # draw_frame_2D(frame, frame_joints_2d)
        frame = draw_skeleton(frame,frame_joints_2d,openpose_skeleton=True)

        cv2.putText(frame, "Predicted Sign Pose", (180, 600), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2)

        # If reference is provided, create and concatenate on the end
        if references is not None:
            # Extract the reference joints
            ref_joints = references[j]
            # Initialise frame of white
            ref_frame = np.zeros((650, 650, 3), np.uint8)

            ref_joints = ref_joints[:-1]


        # Change the Scaling Here #
            for i, value in enumerate(ref_joints):
                if i in range(45,181):
                    ref_joints[i] = value
                else:
                    ref_joints[i] = value

            # Reduce the frame joints down to 2D- Frame joints 2d shape is (48,2)
            ref_joints_2d = np.reshape(ref_joints, (1,134, 2))

            # Draw these joints on the frame
            # draw_frame_2D(ref_frame, ref_joints_2d)
            ref_frame = draw_skeleton(ref_frame,ref_joints_2d,openpose_skeleton=True)

            cv2.putText(ref_frame, "Ground Truth Pose", (190, 600), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)

            frame = np.concatenate((frame, ref_frame), axis=1)

            sequence_ID_write = "Sequence ID: " + sequence_ID.split("/")[-1]
            cv2.putText(frame, sequence_ID_write, (700, 635), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 0, 0), 2)
        
        # Write the video frame
        video.write(frame)
        num_frames += 1
    # Release the video
    video.release()


# Apply DTW to the produced sequence, so it can be visually compared to the reference sequence
def alter_DTW_timing(pred_seq,ref_seq):

    # Define a cost function
    euclidean_norm = lambda x, y: np.sum(np.abs(x - y))

    # Cut the reference down to the max count value
    _ , ref_max_idx = torch.max(ref_seq[:, -1], 0)
    if ref_max_idx == 0: ref_max_idx += 1

    # Cut down frames by counter
    ref_seq = ref_seq[:ref_max_idx,:].cpu().numpy()
    
    # Cut the hypothesis down to the max count value
    _, hyp_max_idx = torch.max(pred_seq[:, -1], 0)
    if hyp_max_idx == 0: hyp_max_idx += 1
    
    # Cut down frames by counter
    pred_seq = pred_seq[:hyp_max_idx,:].cpu().numpy()

    # Run DTW on the reference and predicted sequence
    d, cost_matrix, acc_cost_matrix, path = dtw(ref_seq[:,:-1], pred_seq[:,:-1], dist=euclidean_norm)

    # Normalise the dtw cost by sequence length
    d = d / acc_cost_matrix.shape[0]

    # Initialise new sequence
    new_pred_seq = np.zeros_like(ref_seq)
    # j tracks the position in the reference sequence
    j = 0
    skips = 0
    squeeze_frames = []
    for (i, pred_num) in enumerate(path[0]):

        if i == len(path[0]) - 1:
            break

        if path[1][i] == path[1][i + 1]:
            skips += 1

        # If a double coming up
        if path[0][i] == path[0][i + 1]:
            squeeze_frames.append(pred_seq[i - skips])
            j += 1
        # Just finished a double
        elif path[0][i] == path[0][i - 1]:
            new_pred_seq[pred_num] = avg_frames(squeeze_frames)
            squeeze_frames = []
        else:
            new_pred_seq[pred_num] = pred_seq[i - skips]

    return new_pred_seq, ref_seq, d

# Find the average of the given frames
def avg_frames(frames):
    frames_sum = np.zeros_like(frames[0])
    for frame in frames:
        frames_sum += frame

    avg_frame = frames_sum / len(frames)
    return avg_frame