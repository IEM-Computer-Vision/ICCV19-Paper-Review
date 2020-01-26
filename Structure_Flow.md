## StructureFlow: Image Inpainting via Structure-aware Appearance Flow


 This paper addresses one of the most significant computer vision technique is Image Inpainting. Image inpainting is a modern way of doing image restoring with the help of computer vision. Image restoring is a way of making any distorted and damaged images back to its previous state. There are so many research works that have been done like Diffusion-based methods, Bidirectional similarity, PatchMctch, EdgeConnect, etc. However, most of them may either fail to reconstruct reasonable structures or restore ﬁne-grained textures. To solve this problem a team of researchers from SECE, Peking University; Peng Cheng Laboratory; AIIT, Peking University, and  Tencent America took the initiative and proposed this paper.
 
 <p align="center">
  <img width="360"height="220" src="https://iem-computer-vision.github.io/ICCV19-Paper-Review/images/Structure_Flow_Example.png.jpg">
 </p>

 The main contributions of this paper can be summarized as:
* They propose a structure reconstructor to generate edge preserved smooth images as the global structure information.
* They introduce appearance ﬂow to establish long-term corrections between missing regions and existing regions for vivid texture generation.
* To ease the optimization of appearance ﬂow, they propose to use Gaussian sampling instead of Bilinear sampling and introduce a novel sampling correctness loss.
* Experiments on multiple public datasets show that this method is able to competitive results

> Source code can be found [here .](https://github.com/RenYurui/StructureFlow)

![Structure_Flow_Archetucture.jpg](https://iem-computer-vision.github.io/ICCV19-Paper-Review/images/Structure_Flow_Archetucture.jpg)
### 1. Model Details:
As per the paper they have proposed a two step process 
* Structure reconstructure and 
* Texture generator 

####  1.1 Structure Reconstructor :
In structure reconstructor, they used removed high-frequency textures by keeping the sharp edge and low-frequency structures which guided the structure reconstructor and helped the network to focus on recovering global structures without being disturbed by irrelevant texture information. In that phase, they obtain the whole basic structure of the image as shown in Fig:1. and this structure is basically an edge preserved smooth image. So, you can understand this gives the base to the Image inpainting process.


#### 1.2 Texture Generator :

As the obtained image is consists of low-frequency details, so to make that to its previous position high-frequency details are needed to be added. To do that they use structure generator Since image neighborhoods with similar structures are highly correlated, the uncorrupted regions can be used to generate textures for missing regions.

#### 1.3 Appearance Flow :
In order to establish a clear relationship between different regions, they propose to use appearance ﬂow. appearance ﬂow generates sample features form the existing regions which have a similar structure. Some modifications are been done to achieve higher convergence rate. First, Gaussian sampling is employed instead of Bilinear sampling to expand the receptive ﬁeld of the sampling operation. Second, we introduce a new loss function, called sampling correctness loss, to determine if the correct regions are sampled. Follow Fig 1.

#### 1.4 Gaussian Sampling :

In Gaussian sampling, we calculate the gradients according to the input pixels. If the receptive ﬁeld of the sampling operation is limited, only a few pixels can participate in the operation. except that adjacent pixels (features) are often highly correlated, so a large receptive ﬁeld is required to obtain correct and stable gradients. That’s why they are using Gaussian sampling.
Then merging that with the texture generator they obtain the final result.  
### 2. Results and Comparisons :
#### 2.1 Objective comparisons :
In order to compare the results as accurately as possible, they used two types of metrics: distortion measurement metrics and perceptual quality measurement metrics. Structural similarity index(SSIM) and peak signal-to-noise ratio (PSNR) assume that the ideal recovered results are exactly the same as the target images. They are used to measure the distortions of the results. Fr´echet Inception Distance (FID) calculates the Wasserstein-2 distance between two distributions. Therefore, it can indicate the perceptual quality of the results.results are shown in Table 1.
<p align="center">
  <img width="580"height="300" src="https://iem-computer-vision.github.io/ICCV19-Paper-Review/images/Structure_Flow_table1.png.jpg">
 </p>


#### 2.2 Subjective comparisons :
They implement a human subjective study on the Amazon Mechanical Turk (MTurk). They ask volunteers to choose the more realistic image from image pairs of real and generated images. For each dataset, we randomly select 600 images and assign them random mask ratios from 0% − 60% for the evaluation. Each image is compared 5 times by different volunteers. The evaluation results are shown in Table 2.
<p align="center">
  <img width="360"height="220" src="https://iem-computer-vision.github.io/ICCV19-Paper-Review/images/Structure_flow_table2.jpg">
 </p>

* Reviewed by [Soumyadip Sarkar](https://www.linkedin.com/in/soumyadip-sarkar-173901183/)
