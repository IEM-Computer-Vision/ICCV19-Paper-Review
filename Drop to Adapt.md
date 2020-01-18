# Drop to Adapt: Learning Discriminative Features for Unsupervised Domain Adaptation

[Purbayan Chowdhury](https://www.linkedin.com/in/purbayan-chowdhury-38126914a/)

With increased demand of synthetic datasets in deep neural networks, [domain adaptation](https://en.wikipedia.org/wiki/Domain_adaptation) becomes a prominent part of research. A model trained on the source domain shows disappointing results in the target domain and this is known as _domain shift_.

In this paper, unsupervised domain adaptation id dealt with domain adversarial training where an auxiliary domain discriminator gives a domain-invariant and non-discriminative feature representation. It implements the cluster assumption (decision boundaries should be placed in low density regions in the feature space) using _Drop to Adapt_ (DTA) with adversarial dropout and introduced element-wise and channel-wise adversarial dropout for fully-connected and convolutional layers, respectively.

## Proposed Method

<<<<<<< HEAD
- **Unsupervised Domain Adaptation** - Two distinctive domains : source <img src="https://latex.codecogs.com/svg.latex?S&space;=&space;\{X_s,&space;Y_s\}" class="eqn-inline"> and target domain <img src="https://latex.codecogs.com/svg.latex?T&space;=&space;\{X_t\}" class="eqn-inline"> where a feature extractor <img src="https://latex.codecogs.com/svg.latex?f(x;&space;m_f)" class="eqn-inline"> takes a datapoint from two domains and creates a latent vector which is fed into a classifier <img src="https://latex.codecogs.com/svg.latex?c(.;&space;m_c)" class="eqn-inline">. 

<img src="https://latex.codecogs.com/svg.latex?h(x;&space;m_f,&space;m_c)&space;=&space;c(f(x;&space;m_f);&space;m_c)" class="eqn-outline">


=======
- **Unsupervised Domain Adaptation** - Two distinctive domains : source <img src="https://latex.codecogs.com/svg.latex?S&space;=&space;\{X_s,&space;Y_s\}" class="eqn-slate"> and target domain T = {X<sub>t</sub>} where a feature extractor f(x;m<sub>f</sub>) takes a datapoint from two domains and creates a latent vector which is fed into a classifier c(.; m<sub>c</sub>). h(x; m<sub>f</sub>, m <sub>c</sub> ) = c(f (x; m<sub>f</sub> ); m<sub>c</sub> )
>>>>>>> 1da111918495da1edd87f670e3773d612ef102d2
- **Adversarial Dropout** - Virtual Adversarial Dropout is used which maximize the divergence between two in-
  dependent predictions to an input. The network h is decomposed into h<sub>l</sub> and h<sub>u</sub> by dropout m : <img src="https://latex.codecogs.com/svg.latex?h(x;m)=h_u&space;(m&space;\odot&space;h_l&space;(x))" class="eqn-inline">. The divergence between two distributions p and p' is D[p, p']≥ 0.

  - **Element wise** - The element-wise adv. dropout(EAdD) mask m<sup>adv</sup> <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?m^{adv}"> is defined with respect to a schocastic dropout mask <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?m^s"> as : <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?m^{adv}&space;=&space;argmax_m\&space;D[h(x;&space;m^s),&space;h(x;&space;m)]"> where <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?||m^s&space;-&space;m||\leq&space;\delta_eL">.

  - **Channel wise** - The channel adversarial droupout mask is defined as <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?m^{adv}&space;=&space;argmax_m\&space;D [h(x; m^s ), h(x; m)]">, where <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?\frac{1}{HW}\sum&space;||m^s(i)&space;-&space;m(i)||&space;\leq&space;\delta_CC"> and <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?h_l(x)\&space;\epsilon R^{C&space;\times&space;H\times&space;W}">, where C, H, and W denote the channel, height,
    and width dimensions of the activation, respectively.

- **Drop to Adapt** - The overall loss function is sum of the objectives for task-specific, domain adaptation, entropy minimization and Virtual Adversarial Training(VAT).

  - _Task-specific objective_, <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_T(S)&space;=&space;-&space;E_{x_{s},&space;y_{s}&space;\sim&space;S}[y_s^T&space;log\&space;h(x_s)]">, where  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?y_s"> is one-hot encoded vector of  <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?y_s">.

  - _Domain adaptation objective_, <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_{DTA}(T)&space;=&space;L_{fDTA}(T)&space;&plus;&space;L_{cDTA}(T)">,
    where <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_{fDTA}(T)&space;=&space;E_{x_{s}&space;\sim&space;T}\&space;[D_{KL}[h(x_t;&space;m^s_f&space;),&space;||h(x_t;&space;m^{adv}_f)||]">,
    and <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_{cDTA}(T)&space;=&space;E_{x_{s}&space;\sim&space;T}\&space;[D_{KL}[h(x_t;&space;m^s_c&space;),&space;||h(x_t;&space;m^{adv}_c)||]">

  - _Entropy minimization objective_, <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_E(T)&space;=&space;E_{x_{t}&space;\sim&space;S}\&space;[h(x_t)^T\&space;log\&space;h(x_t)]">

  - _VAT objective_, <img class="eqn-inline" src="https://latex.codecogs.com/svg.latex?L_V(T)&space;=&space;E_{x_{t}&space;\sim&space;T}&space;[max_{||r||&space;\leq&space;\epsilon&space;}&space;D_{KL}[h(x_t),&space;||h(x_t&space;&plus;&space;r)||]">

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
