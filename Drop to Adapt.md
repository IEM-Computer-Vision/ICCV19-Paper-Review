# Drop to Adapt: Learning Discriminative Features for Unsupervised Domain Adaptation

[Purbayan Chowdhury](https://www.linkedin.com/in/purbayan-chowdhury-38126914a/)

With increased demand of synthetic datasets in deep neural networks, [domain adaptation](https://en.wikipedia.org/wiki/Domain_adaptation) becomes a prominent part of research. A model trained on the source domain shows disappointing results in the target domain and this is known as _domain shift_.

In this paper, unsupervised domain adaptation id dealt with domain adversarial training where an auxiliary domain discriminator gives a domain-invariant and non-discriminative feature representation. It implements the cluster assumption (decision boundaries should be placed in low density regions in the feature space) using _Drop to Adapt_ (DTA) with adversarial dropout and introduced element-wise and channel-wise adversarial dropout for fully-connected and convolutional layers, respectively.

## Proposed Method

- **Unsupervised Domain Adaptation** - Two distinctive domains : source <img src="https://latex.codecogs.com/svg.latex?S&space;=&space;\{X_s,&space;Y_s\}" class="eqn-slate"> and target domain T = {X<sub>t</sub>} where a feature extractor f(x;m<sub>f</sub>) takes a datapoint from two domains and creates a latent vector which is fed into a classifier c(.; m<sub>c</sub>). h(x; m<sub>f</sub>, m <sub>c</sub> ) = c(f (x; m<sub>f</sub> ); m<sub>c</sub> )
- **Adversarial Dropout** - Virtual Adversarial Dropout is used which maximize the divergence between two in-
  dependent predictions to an input. The network h is decomposed into h<sub>l</sub> and h<sub>u</sub> by dropout m : h(x;m)=h_u (m⊙ h_l (x)). The divergence between two distributions p and p' is D[p, p']≥ 0.

  - **Element wise** - The element-wise adv. dropout(EAdD) mask m<sup>adv</sup> is defined with respect to a schocastic dropout mask m<sup>s</sup> as : m<sup>adv</sup> = argmax<sub>m</sub> D [h(x; m<sup>s</sup> ), h(x; m)] where &#124;&#124;m<sup>s</sup> − m&#124;&#124; ≤ δ<sub>e</sub>L.

  - **Channel wise** - The channel adversarial droupout mask is defined as m<sup>adv</sup> = argmax<sub>m</sub> D [h(x; m<sup>s</sup> ), h(x; m)], where 1/HW ∑ &#124;&#124;m<sup>s</sup>(i) − m(i)&#124;&#124; ≤ δ<sub>c</sub> C and h<sub>l</sub>(x) ∈ R<sup>C×H×W</sup>, where C, H, and W denote the channel, height,
    and width dimensions of the activation, respectively.

- **Drop to Adapt** - The overall loss function is sum of the objectives for task-specific, domain adaptation, entropy minimization and Virtual Adversarial Training(VAT).

  - _Task-specific objective_, L<sub>T</sub>(S) = - E<sub>x<sub>s</sub>, y<sub>s</sub><sub> ~ S</sub></sub>[y<sub>s</sub> <sup>T</sup> log h(x <sub>s</sub>)], where y<sub>s</sub> is one-hot encoded vector of y<sub>s</sub>.

  - _Domain adaptation objective_, L<sub>DTA</sub>(T) = L<sub>fDTA</sub>(T) + L<sub>cDTA</sub>(T),
    where L<sub>fDTA</sub>(T) = E<sub>x<sub>s</sub> ~ T </sub> [D<sub>KL</sub>[h(x<sub>t</sub>; m<sup>s</sup><sub>f</sub> ), &#124;&#124;h(x<sub>t</sub>; m<sup>adv</sup><sub>f</sub>)&#124;&#124;],
    and L<sub>cDTA</sub>(T) = E<sub>x<sub>s</sub> ~ T </sub> [D<sub>KL</sub>[h(x<sub>t</sub>; m<sup>s</sup><sub>c</sub> ), &#124;&#124;h(x<sub>t</sub>; m<sup>adv</sup><sub>c</sub>)&#124;&#124;]

  - _Entropy minimization objective_, L<sub>E</sub>(T) = - E<sub>x<sub>t</sub><sub> ~ S</sub></sub>[h(x <sub>t</sub>) <sup>T</sup> log h(x <sub>t</sub>)]

  - _VAT objective_, L<sub>V</sub>(T) = E<sub>x<sub>t</sub> ~ T </sub> [max<sub>&#124;&#124;r&#124;&#124; ≤ ∈ </sub> D<sub>KL</sub>[h(x<sub>t</sub>), &#124;&#124;h(x<sub>t</sub> + r)&#124;&#124;]

## Experiment Result

### On Small Datasets

**SVHN ⟶ MNIST** - MNIST consists of binary handwritten
digit images, SVHN consists of coloured images of street
house numbers.

**MNIST ⟷ USPS** - MNIST and USPS contain grayscale
images.

**CIFAR ⟷ STL** - CIFAR and STL are 10-class object recognition datasets with coloured images.

<div align="center">
<div>Results of experiment on small image datasets.</div>
<img src="./images/da_small.png">
</div>

A substantial margin of improvement is achieved over the source only model across all domain configurations. In four of the five configurations, the stated method outperforms the recent state-of-the-art results.

### On Large Datasets

- The **VisDA-2017** image classification is a 12-class domain adaptation problem. The source domain consists of 152,397 synthetic images, where 3D CAD models are rendered from various conditions.

  <div align="center">
  <div>Results on VisDA-2017 classification using ResNet-101</div>
  <img src="./images/da_large.png">
  </div>
  The table clearly shows that the proposed method surpasses previous methods by a large margin. Note that all methods in this table use the same ResNet-101 backbone.

- For the source domain, the synthetic **GTA5 dataset** which consists of 24966 labelled images is used. As the target domain, the real-world **Cityscapes**, consisting of 5000 images is used.
  <div align="center">
  <div>Results on GTA → Cityscapes, using a modified FCN with ResNet-50 as the base network</div>
  <img src="./images/da_large1.png">
  </div>

The stated method clearly improves upon the mIoU of not only the source only model, but also competing methods. Even with the same training procedure and settings as in the classification experiments, DTA is extremely effective at adapting the most common classes in the dataset.

For code, visit this [link](https://github.com/postBG/DTA.pytorch).
