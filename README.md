# Effectiveness of Multi-Scaling Keypoints for Sign Language Translation

## Abstract
Sign language primarily uses visual cues to communicate. However, existing sign language translation models tend to neglect facial features or rely on outdated pose estimation models. In this project, we propose a modern sign language translation model that generates facial features using a modern pose estimation method, DWPose. This paper discusses the additional complexity facial features bring and potential solutions to address these challenges. We experiment with various preprocessing techniques to enhance the model’s capability in generating sign language poses, focusing on different scaling variations to the pose keypoints. By scaling keypoints differently, the loss function contribution of all the keypoints is affected, encouraging the translation model to focus on learning certain features more than others. Through experimentation, we assess the impact of different scaling methods on the generated keypoint output. The translation model used in this work is based on the Progressive Transformer.

## Dataset
The dataset used in this project is the PHOENIX14T dataset. You can download it from the [PHOENIX14T website](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/). Due to size constraints, example data can be found in the ExampleData folder.

## Qualititave Evaluation

### Comparison with previous models
<div align="center">
  <img src="face/face.png" alt="Frame by frame comparison" width="400"/>
</div>

- **Quality of Skeletal Keypoints**: The goal of this paper is to utilise a sign language translation model that is capable of generating additional keypoint features, As this work is based on the Saunder PT. The results of the DWPose skeleton poses will be used to compare to the OpenPose skeleton poses to demonstrate the feature and visual differences between the two models

### Best Results
<div align="center">
  <img src="wetter_wie-aussehen_morgen_28_78.gif" alt="Frame by frame comparison" width="400"/>
</div>

- The figure above showcases the model's results by comparing the ground truth poses with the predicted poses.

<div align="center">
  <img src="face/compare.png" alt="Frame by frame comparison" width="400"/>
</div>

- Generated Skeleton comparison for the gloss ”wetter wie aussehen morgen”, (a) Lowest DTW and Lowest PCK Model 100-100, (b) Highest PCK and Highest DTW Model 100-0.




## Quantitative Evaluation
<div align="center">
  <img src="face/tables.png" alt="Frame by frame comparison" width="600"/>
</div>


<div align="center">
  <img src="face/extreme.png" alt="Frame by frame comparison" width="600"/>
</div>

- The **Percentage of Correct Keypoints(PCK)** score measures the percentage accuracy of the predicted pose across all the poses in the datasets. This is done by calculating the Euclidean distance between the Ground Truth keypoints and the predicted keypoints across the entire dataset. If the distance between two points is lower than a predefined threshold, then the predicted keypoints would be considered as correctly predicted. The PCK score is then calculated from the percentage of correctly predicted keypoints out of the total keypoints in the dataset. A higher PCK score indicates a closer resemblance between the predicted and ground truth poses, which suggests a better performance.

- **Dynamic Time Warping(DTW)** is a technique used to measure the similarity between two sequences of data points that are indexed in time order, these sequences are normally referred as Two Time Series Data and may vary in terms of length. The similarity is useful to align the different data sequences by warping its time indices, this is useful for our keypoints data as it preserves the time order introduced in the counting embedding layer. To compute the similarity be tween the sequences, the distance matrix containing pairwise distances between the keypoints of the predicted and ground truth sequences is first constructed. Then the warping path that minimises the aggregate distance between the sequences is located. Using the warping path and distance matrices, the algorithm sum the distance matrices along the warping path to calculate the DTW distance. A smaller DTW distance represents a greater similarity between the sequences and a greater similarity results in a better matching pose sequence. DTW allow us to effectively compare sequences of different lengths, In this case, the sequences represent the skeleton keypoints of individual frames, which is important for evaluating the performance of our continuously generated output










### Instructions
To run the Progressive Transformer:

1. Each folder contains its own `requirements.txt` file. To run the code, all the required libraries need to be downloaded first.
2. Download the PHOENIX14T dataset.
3. Perform DWPose pose estimation by running the `dw_extract.py` file located in the DWPose_RTMB folder (or you can run the `demo.ipynb` file on a single image; an image from PHOENIX14T is also included for testing if interested).
   ![Alt Text](demo.png)
4. Ensure that the skeleton poses are in a file ending with ".skels" (further instructions are in the Progressive Transformer folder).
5. Pass the skeleton ".skels" file into the `counter_embedding.py` file to perform counter embedding. Make sure to do this for each dataset.
6. Adjust the configuration file as needed. Make sure that you have `.skels`, `.file`, and `.gloss` for all training, validation, and test sets (as shown in the ExampleData folder).
7. Put all the files into the `sign_data` folder in the Progressive Transformer folder (adjust the `dw_plot_video.py` scaling value according to the normalization done to keypoints).
8. Run the `training.py` file in the Progressive Transformer folder (make sure the correct config is utilized, as noted in the #Change here# section).

- Note: `dw_plot_video.py` is important for drawing skeleton poses for DWPose. It uses code from rtmlib ([GitHub Repository](https://github.com/Tau-J/rtmlib)) and is implemented to be compatible with the transformer.




## Information about the Code
The code consists of three sections:
- **DWPose_RTMB:** This is the rtmlib from Jiang, Tao ([GitHub Repository](https://github.com/Tau-J/rtmlib)). This part of the code performs DWPose and draws the skeletal keypoints for the poses. Note that the code was also changed to make it compatible with our project.
- **Counter_embedding:** Adds counter values to the skeleton keypoints estimates (done right after pose estimation for the dataset).
- **Progressive Transformer:** An adjusted version of Ben Saunders' Progressive Transformer ([saunders2020progressive](https://arxiv.org/abs/2004.14874)) to make it DWPose compatible.









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
