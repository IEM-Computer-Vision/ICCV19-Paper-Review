# Shape Reconstruction using Differentiable Projections and Deep Priors

- [Himanshu Raj](https://github.com/himanshuraj001)

Shape reconstruction has always been an important topic of resarch in field of Computer vision. Using shape reconstruction we can determine  shape profile of any object as well as coordinate of any point in the profile. It has many applications in various fields i.e Medicine, 3d- Shape recounstruction, gaming, etc. This paper gives us information about Shape recounstruction from images of an object from different projection angle by using deep prior and differentiable projection operator .


In this three differentiable projection operators are used:
* Radon Projection (TR)
* Silhouette Projection (TS)
* Depth Image Projection (TD)

## Method

In this we are using following differentiable projection operators and deep shape priors for which Bayesian inference can be performed via stochastic gradient descent and their variants. In shape recounstruction we use an encoder and decoder network architecture with skip connections in which input to the network is tensor and is of same size as output. Thus, By combining the deep image or volumetric prior with differentiable projection operators, signals can be reconstructed from a few noisy projection measurements using stochastic gradient descent.

<p align = "center">
<img src="https://github.com/himanshuraj001/numerical_method-project-c-/blob/master/Untitled.png" />
</p>
