# DeepVCP: An End-to-End Deep Neural Network for Point Cloud Registration

<a href="http://www.youtube.com/watch?feature=player_embedded&v=O9AMulNyrzY
" target="_blank"><img src="http://img.youtube.com/vi/O9AMulNyrzY/0.jpg" 
alt="Youtube Video" width="240" height="180" border="10" /></a>

DeepVCP is a novel end-to-end learning-based 3D point cloud registration framework that achieves comparable registration accuracy to prior state-of-the-art geometric methods. Instead of implementing other keypoint based methods where a RANSAC procedure is usually needed, the implementation of various deep neural network structures is done to establish an end-to-end trainable network. The keypoint detector is trained through this end-to-end structure and enables the system to avoid the inference of dynamic objects, leverages the help of sufficiently salient features on stationary objects, and as a result, achieves high robustness. 

Generation of corresponding points are done based on learned matching probabilities among a group of candidates which improves registration accuracy. KITTI & Apollo-SouthBay datasets are used to validate the efficiency.

Results demonstrate that it achieves comparable registration accuracy and runtime efficiency compared to state-of-the-art geometry-based methods, but with higher robustness to inaccurate initial poses. 

Low registration error and high robustness of this method makes it suitable for substantial applications based on the point cloud registration.

- [Soham Biswas](https://www.linkedin.com/in/soham-biswas-590784168/)
