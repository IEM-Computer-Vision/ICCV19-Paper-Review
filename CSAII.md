
# Coherent Semantic Attention for Image Inpainting

[Somodyuti Pal](https://www.linkedin.com/in/somodyuti-pal-a01028136/)

[Image Inpainting](https://en.wikipedia.org/wiki/Inpainting) application which works on reconstructing a distorted or hazy image to its original form, is becoming a prominent part of research. The existing approaches often suffer from blurry & distorted images due to discontinuity of local pixels. The local pixel discontinuity happens due to ignoring the semantic relevance and feature continuity of hole/missing regions.

In this paper The human behavior in repairing pictures,i.e. two steps as **conception** and **painting** are introduced to ensure global structure consistency as well as local pixel continuity of a picture .The approach of painting process,constructing new structures and texture from the end nodes of the structures created previously,that ensures the local pixel continuity of the final result. Inspired by this ,a coherent semantic
attention layer (CSA)is proposed which will retain fine details.

<div align="center"><div>Rough,Repainting & CSA Architecture</div>
<img src="./images/p2c1.png">
</div>

## The Proposed System

-  The Proposed model consists of two steps: **1. Rough Inpainting** & **2.    Refinement Inpainting** 
   - **1. Rough Inpainting** -  Training of a rough network to rough out the missing contents/holes is followed. This stabilizes the training and ensures ta larger receptive field.
    <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\{I_g_t\} "> be the ground truth &<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\{I_i_n\} ">(3* 256 * 256 shape) be the input to rough framework. From these  two  we try to have the rough prediction<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\{I_p\} "> by using <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\( 4 * 4\)"> convolutions with skip connections.
     
    - **2. Refinement Inpainting** - This consists of two stages 
        
       - **Refinement Network** - <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\{I_p\} "> is conditioned on <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\{I_i_n\} "> as a input of The encoder-decoder pair of ths network with <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\( 3*3\)"> convolutions to double channels & <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\( 4 * 4\)">  **Dilated Convolutions** to reduce spatial size that enlarges receptive fields.
        
       - **Coherent Semantic Attention** -A novel coherent semantic attention layer is applied to construct the correlation between the deep features of hole regions. Completed in two phases: **Searching and Generating** 
        
      <div align="center"> 
      <div>Searching & Generating.</div>
      <img src="./images/s&G.png"> 
      </div>
        
        - **Searching** -  CSA layer searches the closest-matching contextual     patch <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? m_i "> in 
        known region <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? M">to initialize  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? m_i "> during the search process.<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? M"> and  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? \overline{M}"> in feature map are considered &  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? \overline{M}"> is used to extract patches ,patches as<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? m_i ">, to obtain vector values denoting cross correlational value between <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? M"> and  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? \overline{M}"> & compute maximum as <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? D_m_a_x_i">.Which stands for similarity between<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? \overline{m_i}"> & <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? m_i">.
        
        - **Generating** - As a initial patch the left of <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? M"> is taken and  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? D_{ad} = \frac{< m_i, \overline{m_i} >}{(\parallel m_i \parallel \cdot \parallel \overline{m_i} \parallel)}">  initially is 0. as <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? \overline{m_i}"> is zero. Now the future patches are resolved with a reference from previous as a formulae of <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? m_i\in_{2\sim n} = \frac{D_{adi} \times m_{i-1} + D_{max_i} \times m_i}{D_{adi} + D_{max_i}}"> Based on this,an attention map<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? A_i =\frac{(D_{adi} \times A_{i-1})}{D_{adi} + D_{max_i}}"> is used to create the attention matrix. Which with deconvolutional layers reconstruct <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? M"> 
   
- **Consistency Loss** - A ImageNet-pretrained VGG-16 is used to extract
a high level feature space from the original image. In <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? M">, we set the feature space as the target for the CSA layer and the corresponding layer of the CSA
in decoder respectively to compute the the <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_c">distance as :
  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_c = \sum_{y\in M}&space;||CSA&space;(I_i_p)_y-&space;\Phi_n(I_g_t)_y||^2 _2&space; + ||CSA_d&space;(I_i_p)_y-&space;\Phi_n(I_g_t)_y||^2 _2">

- **Feature Path Discriminator** -  A feature patch discriminator is developed to discriminate completed images and original images by inspecting their feature maps. As receptive fields of each point features the entire image, the adversarial loss <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? D_R">,
<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?D_R&space;=&space;-E_{I_g_t}[D(I_g_t ,&space; I_r)^2]-E_{I_r}[(1-D(I_g_t ,&space; I_r)^2)] ">  & Loss function <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? D_F"> for discriminators:
<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? D_F =&space;-E_{I_g_t}[(1-D(I_g_t ,&space; I_r)^2)]-E_{I_r}[D(I_g_t ,&space; I_r)^2]"> where <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? E_{I_g_t}/E_{T_r}">, represents the operation of taking average for all real/fake data in the mini-batch.


## Experimental Results
  - On three datasets this model was tested **Places2** , **CelebA**,and **Paris StreetView** model is optimized by the **Adam algorithm**
    with a learning rate of 2 × 10−4 and <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex? \beta _1"> = 0.5. The tradeoff
    parameters are set as <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\lambda _r"> =1,<img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\lambda _c">=0.01, <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\lambda _d">=0.002,with a batch size of 1.The weak correlation areas in attention maps are areas of concern for generated patches which are far from it, the strong correlation areas are areas of concern for both adjacent generated patches and most relevant patches.    
  
  <div align="center">
  <div>Qualitative comparison</div>
  <img src="./images/CAII33.png">
  </div>


 - **Effectof CSA Layer** - The CSA layer was replacced with convolutional layers as a query to understand it's importance . And it failed to perform like CSA as the pixels were not consistent with the background.
 Hence global semantic structure and local coherency are constructed by the CSA layer.
 <div align="center">
 <div>Quantitative comparison</div>
 <img src="./images/pc32.png"></div>
 - **Feature path Discriminator** & **Consistency loss** also proved to be much effective than conventional ways.

   

<div align="center">
<div>Quantitative comparison</div>
<img src="./images/pc35.png"></div>

 The inpainting task thus is completed through this two stage method. Whether the unknown region is irregular or centering, this algorithm can achieve state-of-the-art inpainting results. The Human inspired **Rough & Refinement** steps added new path on this application.

The stated method clearly had great effect on inpainting techniques and worked well than other Architectures it compared with. The new introduced **Feature path Discriminator** & **Consistency loss** achieved greater impact than conventional ways.

For code, visit this [link](https://github.com/KumapowerLIU/CSA-inpainting.).