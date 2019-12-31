# SANet: Scene Agnostic Network for Camera Localization
This paper presents a scene agnostic neural architecture for camera localization, where model parameters and scenes are independent from each other.

## The Need of SANet
SLAM, location recognition, robot navigation, augmented reality and many applications require Camera localization as a critical component. The Conventional approach is often brittle due to the long pipeline of hand-crafted components (image retrieval, feature correspondence matching, and camera pose estimation). Learning based approaches of camera localization with random forests (RFs) and convolutional neural networks often enjoy better robustness than the conventional pipeline. However, the RFs or CNNs are learned from images for a specific scene and require retraining before they can be applied to a different scene. While online adaptation is possible with RGBD query images and a RF. CNNs produce higher localization accuracy, but cannot be quickly adapted to a different scene.

For online applications such as SLAM and robotic navigation, where retraining is impossible, it is important to build a scene agnostic network for camera localization that works on unseen scenes without retraining or adaptation. By learning-based approach this paper achieves that.<br>
This Paper have achieved state-of-the-art performance, while this method works for arbitrary scenes without retraining or adaptation.

## Let’s look upon the Limitations of Related Works and how SANet comes
1)Feature Matching & Camera Fitting: The works, by the PnP algorithms focus on making the hand-crafted descriptor either more efficient, more robust, or more scalable to large outdoor scenes. However, the handcrafted feature detectors and descriptors only work with well textured images. Using VGG and etVLAD instead of hand-crafted features achieves strong performance, it is still based on the conventional pipeline of correspondence matching and camera model fitting.

2)Random Forests: These works trained a random forest to predict diverse scene coordinates to resolve scene ambiguities, to predict multi-model distributions of scene coordinates for increased pose accuracy. None of these works are scene agnostic.

As the following camera pose estimation from a scene coordinate map is a well-behaved optimization problem, recent works use CNN (Convolutional Neural Networks) to regress the scene coordinates as intermediate quantities. Their method belongs to these categories and use CNNs to predict the scene coordinate of an image. However, our network extracts hierarchical features from scenes rather than learn a set of scene-specific network parameters. In this way, their method is scene agnostic and can be applied to unknown scenes. The sequence of operation followed here is
- Constructing Pyramids 
- Predicting Scene Coordinate
-	Query Pose Estimation


