# Fine-Grained Segmentation Networks: Self-Supervised Segmentation for Improved Long-Term Visual Localization

- [Himanshu Raj](https://github.com/himanshuraj001)

In computer vision, image segmentation is the process of partitioning a digital image into multiple segments . The goal of segmentation is
to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. Visual localization is the problem of estimating the 6 Degree-of-Freedom (DoF) camera pose from which a given image was taken relative to
a reference scene representation.

### Traditional Method and problems with it:

#### Semantic Segmentation:
Semantic segmentation is the task of assigning a class label to each pixel in an input image. Mostly CNN are used and are trained in fully 
supervised fashion.However, obtaining a large amount of densely labeled images is very time-consuming and expensive . As a result,
approaches based on weaker forms of annotations have been developed. CNNs for semantic segmentation typically only perform well under 
varying conditions if these conditions are reflected in the training set. Yet, creating pixel-level annotations for large image sets is 
a time consuming task.

#### (Semantic) Visual Localization :
It is done by using a 3D scene model constructed from a set of database images via Structure-from Motion.Thus approach establish a set of 2D-3D correspondences
between a query image and the model. There is another machine learning based approaches either replace the 2D-3D matching stage
through scene coordinate regression.  The former type of methods achieves state-of-the-art localization accuracy in smallscale scenes ,
but do not seem to easily scale to larger scenes.

In this paper a new neural network is proposed, the Fine-Grained Segmentation Network (FGSN), that can be used to provide image 
segmentations with a larger number of labels and can be trained in a self-supervised fashion and then after integrating the fine-grained
segmentation produced by FSGNs we get substantial improvment in visual localization algorithm.

### Fine-Grained Segmentation Networks (FGNs):
The Fine-Grained Segmentation Network (FGSN) has the same structure as a standard CNN used for semantic segmentation, but instead of being
trained on a set of manually created labels, labels are created in a self-supervised manner.During training, at certain intervals, features
are extracted from the images in the training set and clustered using k-means clustering. In this we use a set of 2D-2D point correspondences
during training to ensure that the predictions are stable under seasonal changes and viewpoint variations, method we use for label creation is  based on k-means clustering.

* Training loss:
 Training loss consists of two parts, a correspondence part Lcorr and a cluster classification part Lclass. The final Lclass loss is an average of over all samples.
 For Lcorr, we use the 2D-2D point correspondences. Denote the content of one sample from the correspondence dataset as (Ir, It, xr, xt). 
 Here Ir is an image from the reference traversal, It is an image from the target traversal, and xr as well as xt are the pixel positions of the matched
points in the reference and target images, respectively. The correspondence loss function Lcorr is an average over all such samples. And in last
we minimize L=Lcorr+Lclass.

<p align = "center">
<img src="https://github.com/himanshuraj001/demo/blob/master/unt1.png" />
</p>

### Segmantic Visual Localization using FSN:
In this we use fine semantic segmantations from FSN to get substantial improvment in visual localization algorithm.

#### Simple Semantic Match Consistency (SSMC):
The first approach is a simple-to-implement match consistency filter used as a baseline method . Given a set of 2D-3D matches between 
features in a query image and 3D points in a Structure-from-Motion (SfM) point cloud, SSMC uses semantics to filter out inconsistent 
matches.

#### Geometric-Semantic Match Consistency (GSMC):
The projections are used to measure a semantic consistency score for the pose by counting the number of points projecting into a query 
image region with the same label as the point.While performing significantly better than SSMC, GSMC makes additional assumptions and is 
computationally less efficient

#### Particle Filter-based Semantic Localization (PFSL):
In this approach, localization is approached as a filtering problem where we, in addition to a sequence of camera images, also have access to noisy odometry information. Both
these sources are combined in a particle filter to sequentially estimate the pose of the camera by letting each particle describe a possible camera pose.

### Evaluation measures:
We are doing evalution based on this table: 
<p align = "center">
<img src="https://github.com/himanshuraj001/demo/blob/master/Unt2.png" />
</p>

* Impact of the number of clusters:  The experiments clearly show that SSMC benefits from using fine-grained segmentations, even though
clusters might not necessarily correspond to standard semantic concepts. SSMC benefits from a larger number of clusters is that the corresponding segmentations provide
a more discriminative representation of the query images and the 3D point cloud. This allows SSMC to filter out more wrong matches by enforcing label consistency. This
in turn increases the inlier ratio and thus the probability that RANSAC finds the correct pose.

* Impact of pretraining FGSNs : FGSNs pre-trained on a classification task result in a significantly lower performance compared to networks trained for semantic segmentation. This shows the importance of
using segmentations that retain some semantic information, which is more the case for FGSNs pre-trained on semantic segmentation than
for FGSNs pre-trained on classification.

* Impact of using 2D-2D point correspondences: Using fine-grained segmentation yields better results than using semantic classes
on the Extended CMU Seasons dataset.

* Genralization Abilities : when training the FGSNs on a different dataset. We observe a substantial drop in performance compared to
FGSNs trained on the same dataset. While the performance of FGSNs trained on another dataset is comparable to using networks trained for
semantic segmentation, our results indicate that there is still significant room for improving FGSNs

* Repetation of clusters: The clustering is repeated after a setnumber of training iterations and because of not resetting the network 
actually gives slightly better performance.

* Comparison with state-of-the-art methods: using segmentations with more labels, as afforded by our FGSNs, improves localization performance closing the performance gap to the current
state-of-the-art. The results clearly validate the motivation behind FGSNs: using more segmentation labels to create
more discriminative, yet still robust, representations for semantic visual localization.

## Conclusion 
1. We present a novel type of segmentation network, the Fine-Grained Segmentation Network (FGSN), that outputs dense segmentation maps
based on cluster indices.This removes the need for human-defined classes.

2. FGSNs allow us to create finer segmentations with more classes. We show that this has a positive impact on semantic visual localization algorithm.

3. We perform detailed experiments to investigate the impact the number of clusters has on multiple visual localization algorithms. 
In addition, we compare two types of weight initializations, using networks pre-trained for semantic segmentation and image
classification, respectively.
