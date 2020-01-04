
Fine Grained Segmentation Networks

The Problem :
1. Visual localization is the problem of estimating the camera pose of a given image relative to a visual representation of a known scene. There are a lot of visual localization algorithms which rely on segmentation.
2. The problem with existing segmentation algorithms is that they are fully supervised and needs annotations.
3. The algorithms are not robust to changes (such as seasonal change in a landscape).

Solution :
1. Increasing the number of classes in an image boosted the performance of semantic visualization algorthms.
2. Usage of a self supervised learning technique to increase the number of classes in an image.

How is it achieved :
1. A fine grained segmentation network is employed for pixel level clustering. 
2. During training, at certain intervals, features are extracted from the images in the training set and clustered using k-means clustering. The cluster assignments, one at each pixel, are then used as supervision during training, i.e. as labels.
3. Usage of a 2D-2D correspondence to make sure the predictions are stable under seasonal/viewpoint changes.
