# Effectiveness of Multi-Scaling Keypoints for Sign Language Translation


<div align="center">
  <img src="wetter_wie-aussehen_morgen_28_78.gif" alt="Frame by frame comparison" width="600"/>
</div>


The content below summarizes the original work. For the full details, please refer to: [Link to PDF](nu/KahHanChiaDissertation.pdf)


## Abstract
Sign language primarily relies on visual cues for communication. Existing sign language translation models often overlook facial features or use outdated pose estimation models. We propose a modern sign language translation model using DWPose for facial feature generation. This paper addresses the added complexity of facial features and explores solutions for these challenges. We experiment with various preprocessing techniques to enhance the model’s ability to generate sign language poses, focusing on different scaling variations of pose keypoints. These scaling variations affect the contribution of keypoints to the loss function, guiding the model to prioritize certain features. We evaluate the impact of these scaling methods on keypoint outputs using the Progressive Transformer model.

## Dataset
The dataset used is the PHOENIX14T dataset. You can download it from the [PHOENIX14T website](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/). For convenience, example data is available in the ExampleData folder.

## Qualitative Evaluation

### Comparison with Previous Models
<div align="center">
  <img src="face/face.png" alt="Frame by frame comparison" width="400"/>
</div>

- **Quality of Skeletal Keypoints**: This paper aims to utilize a sign language translation model capable of generating additional keypoint features. We compare the DWPose skeleton poses with OpenPose skeleton poses to highlight feature and visual differences.

### Best Results
<div align="center">
  <img src="face/compare.png" alt="Frame by frame comparison" width="400"/>
</div>

- Comparison of generated skeletons for the gloss "wetter wie aussehen morgen":
  - (a) Lowest DTW and Lowest PCK Model (100-100)
  - (b) Highest PCK and Highest DTW Model (100-0)

## Quantitative Evaluation
<div align="center">
  <img src="face/tables.png" alt="Frame by frame comparison" width="600"/>
</div>

<div align="center">
  <img src="face/extreme.png" alt="Frame by frame comparison" width="600"/>
</div>

- **Percentage of Correct Keypoints (PCK)**: PCK measures the accuracy of predicted keypoints by comparing them to ground truth keypoints. It calculates the percentage of keypoints within a predefined distance threshold from their true positions. A higher PCK score indicates better alignment between predicted and true poses.

- **Dynamic Time Warping (DTW)**: DTW compares two time-ordered sequences by aligning them through time warping. It calculates similarity by finding the warping path that minimizes the total distance between sequences. A smaller DTW distance indicates higher similarity, essential for evaluating the accuracy of keypoint sequences in pose predictions.

### 5.1.2. Equal Scaling Results
- **Models Tested**: Denoted as “poseX”, where “X” represents the scaling value of the entire skeleton pose (tested with values 25 and 100).
- **Findings**: The “pose100” model, with a scaling value of 100, converged faster and performed better across all metrics compared to the “pose25” model.
- **Note**: Models trained with scaling values other than 100 had significantly higher loss values and longer convergence times, making them impractical for training. Therefore, “pose100” is preferred for its superior performance.

### 5.1.3. Multi-Scaling Results
- **Models Tested**: Denoted as “x-y”, where “x” represents scaling for body keypoints and “y” represents scaling for facial features. The body keypoints were scaled by 100, while “y” varied to test its effect.
- **Findings**: 
  - **100-100**: Baseline model with equal scaling for body and facial keypoints.
  - **100-0**: Extreme case where facial keypoints were not scaled down, forcing the model to focus on learning facial features.
  - **100-25** and **100-50**: Intermediate scaling ratios to assess their impact on performance.
- **Evaluation Metrics**: The effects of different scaling parameters were compared using Loss Functions, Dynamic Time Warping (DTW), and Percentage of Correct Keypoints (PCK).


## Instructions
To run the Progressive Transformer:

1. Each folder contains its own `requirements.txt` file. Install all required libraries first.
2. Download the PHOENIX14T dataset.
3. Perform DWPose pose estimation by running `dw_extract.py` in the DWPose_RTMB folder (or use `demo.ipynb` for a single image; an example image from PHOENIX14T is provided).
   ![Alt Text](demo.png)
4. Ensure skeleton poses are in a file ending with ".skels" (instructions available in the Progressive Transformer folder).
5. Pass the ".skels" file to `counter_embedding.py` for counter embedding. Repeat for each dataset.
6. Adjust the configuration file as needed. Ensure you have `.skels`, `.file`, and `.gloss` for all training, validation, and test sets (as shown in the ExampleData folder).
7. Place all files into the `sign_data` folder in the Progressive Transformer directory (adjust the `dw_plot_video.py` scaling value according to keypoint normalization).
8. Run `training.py` in the Progressive Transformer folder (ensure the correct configuration is used as noted in the #Change here# section).

**Note**: `dw_plot_video.py` is used for drawing skeleton poses for DWPose. It utilizes code from rtmlib ([GitHub Repository](https://github.com/Tau-J/rtmlib)) and is adapted for compatibility with the transformer.

## Information about the Code
The code is divided into three sections:
- **DWPose_RTMB**: Uses rtmlib from Jiang, Tao ([GitHub Repository](https://github.com/Tau-J/rtmlib)) for DWPose and skeleton keypoint drawing. Modified for project compatibility.
- **Counter_embedding**: Adds counter values to skeleton keypoints estimates (immediately after pose estimation).
- **Progressive Transformer**: An adapted version of Ben Saunders' Progressive Transformer ([saunders2020progressive](https://arxiv.org/abs/2004.14874)) to be compatible with DWPose.


## Summary

This paper successfully integrates DWPose into the Progressive Transformer model, emphasizing the significance of facial features in sign language translation. By extending the Progressive Transformer to include facial features, DWPose has demonstrated substantial improvements over previous pose estimation methods. Enhancing sign language skeleton pose generation can significantly advance sign language translation, benefiting both communities and individuals interested in learning sign language.

Key findings include:

- **Scaling Results**: Dividing each keypoint by 100 produced the best results for skeletal keypoints. While different scaling methods influenced the loss function, models with varied scaling for facial keypoints did not meet expectations.
- **Overfitting Issue**: Multi-scaled models tended to overfit to an “O” shape mouthing, likely due to the dataset's limited size and the frequent use of this mouth shape in sign poses. This pattern also appears in face-only models, which show improved head movement but still exhibit the “O” shape issue.



## Citations

```bibtex
@misc{rtmlib,
  title={rtmlib},
  author={Jiang, Tao},
  year={2023},
  howpublished = {\url{https://github.com/Tau-J/rtmlib}},
}

@misc{jiang2023,
  doi = {10.48550/ARXIV.2303.07399},
  url = {https://arxiv.org/abs/2303.07399},
  author = {Jiang, Tao and Lu, Peng and Zhang, Li and Ma, Ningsheng and Han, Rui and Lyu, Chengqi and Li, Yining and Chen, Kai},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RTMPose: Real-Time Multi-Person Pose Estimation based on MMPose},
  publisher = {arXiv},
  year = {2023},
  copyright = {Creative Commons Attribution 4.0 International}
}

@misc{lu2023rtmo,
      title={{RTMO}: Towards High-Performance One-Stage Real-Time Multi-Person Pose Estimation},
      author={Peng Lu and Tao Jiang and Yining Li and Xiangtai Li and Kai Chen and Wenming Yang},
      year={2023},
      eprint={2312.07526},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@inproceedings{saunders2020progressive,
  title = {{Progressive Transformers for End-to-End Sign Language Production}},
  author = {Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},
  year = {2020}
}

@inproceedings{saunders2020adversarial,
  title = {{Adversarial Training for Multi-Channel Sign Language Production}},
  author = {Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
  booktitle = {Proceedings of the British Machine Vision Conference (BMVC)},
  year = {2020}
}

@inproceedings{saunders2021continuous,
  title = {{Continuous 3D Multi-Channel Sign Language Production via Progressive Transformers and Mixture Density Networks}},
  author = {Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
  booktitle = {International Journal of Computer Vision (IJCV)},
  year = {2021}
}

@misc{diss,
  author = {Gonzalez, Adam},
  title = {diss},
  howpublished = {\url{https://github.com/adamg4911/diss}},
  year = {2023},
}
