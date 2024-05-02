# Dissertation

This is my Research Project: Effectiveness of multi-scaling keypoints for Sign Language Translation

The dataset can be downloaded is PHOENIX14T dataset: https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/ 
Due to size constraints: Example data can be found at the ExampleData Foulder


![Video](https://github.com/KahHan19/Diss/blob/main/wetter_wie-aussehen_morgen_28_78.mp4)




The code consists of Three sections:

    - Counter_embedding: Add Counter Values in the skeleton keypoints estimates

    - DWPose_RTMB: This is the rtmlib from Jiang, Tao (https://github.com/Tau-J/rtmlib) This part of the code is to perform DWPose and draw the skeletal keypoints for the poses. Do know that the code was also changed to make it compatible with the assingment.

    - Progressive Transformer: Adjusted version of Ben Saunders Progressive Transformer to make it DWPose compatible

Remark: Each word containts its own Liscene and its respective Readme File.

To run the progressive Transformer: 
- Directories of the config needs to be changed
- Change the scaling for dw_plot_video.py
- Run the training.py file in the Progressive Transformer folder ( make sure the correct config is utilised )
- A sample config is also uploaded for reference


# Citation        
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
    	title		=	{{Progressive Transformers for End-to-End Sign Language Production}},
    	author		=	{Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
    	booktitle   	=   	{Proceedings of the European Conference on Computer Vision (ECCV)},
    	year		=	{2020}}
    
    @inproceedings{saunders2020adversarial,
    	title		=	{{Adversarial Training for Multi-Channel Sign Language Production}},
    	author		=	{Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
    	booktitle   	=   	{Proceedings of the British Machine Vision Conference (BMVC)},
    	year		=	{2020}}
    
    @inproceedings{saunders2021continuous,
    	title		=	{{Continuous 3D Multi-Channel Sign Language Production via Progressive Transformers and Mixture Density Networks}},
    	author		=	{Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
    	booktitle   	=   	{International Journal of Computer Vision (IJCV)},
    	year		=	{2021}}


    @misc{diss,
      author = {Gonzalez, Adam},
      title = {diss},
      howpublished = {\url{https://github.com/adamg4911/diss}},
      year = {2023},
    }
