# Drop to Adapt: Learning Discriminative Features for Unsupervised Domain Adaptation

[Purbayan Chowdhury](https://www.linkedin.com/in/purbayan-chowdhury-38126914a/)

With increased demand of synthetic datasets in deep neural networks, [domain adaptation](https://en.wikipedia.org/wiki/Domain_adaptation) becomes a prominent part of research. A model trained on the source domain shows disappointing results in the target domain and this is known as _domain shift_.

In this paper, unsupervised domain adaptation id dealt with domain adversarial training where an auxiliary domain discriminator gives a domain-invariant and non-discriminative feature representation. It implements the cluster assumption (decision boundaries should be placed in low density regions in the feature space) using _Drop to Adapt_ (DTA) with adversarial dropout and introduced element-wise and channel-wise adversarial dropout for fully-connected and convolutional layers, respectively.

## Proposed Method

- **Unsupervised Domain Adaptation** - Two distinctive domains : source S= {X&lt;sub&gt;s&lt;/sub&gt;, Y&lt;sub&gt;s&lt;/sub&gt;} and target domain T = {X&lt;sub&gt;t&lt;/sub&gt;} where a feature extractor f(x;m&lt;sub&gt;f&lt;/sub&gt;) takes a datapoint from two domains and creates a latent vector which is fed into a classifier c(.; m&lt;sub&gt;c&lt;/sub&gt;). h(x; m&lt;sub&gt;f&lt;/sub&gt;, m &lt;sub&gt;c&lt;/sub&gt; ) = c(f (x; m&lt;sub&gt;f&lt;/sub&gt; ); m&lt;sub&gt;c&lt;/sub&gt; )
- **Adversarial Dropout** - Virtual Adversarial Dropout is used which maximize the divergence between two in-
  dependent predictions to an input. The network h is decomposed into h&lt;sub&gt;l&lt;/sub&gt; and h&lt;sub&gt;u&lt;/sub&gt; by dropout m : h(x; m) = h&lt;sub&gt;u&lt;/sub&gt; (m ⊙ h&lt;sub&gt;l&lt;/sub&gt; (x)). The divergence between two distributions p and p' is D[p, p']≥ 0.

  - **Element wise** - The element-wise adv. dropout(EAdD) mask m&lt;sup&gt;adv&lt;/sup&gt; is defined with respect to a schocastic dropout mask m&lt;sup&gt;s&lt;/sup&gt; as : m&lt;sup&gt;adv&lt;/sup&gt; = argmax&lt;sub&gt;m&lt;/sub&gt; D [h(x; m&lt;sup&gt;s&lt;/sup&gt; ), h(x; m)] where &#124;&#124;m&lt;sup&gt;s&lt;/sup&gt; − m&#124;&#124; ≤ δ&lt;sub&gt;e&lt;/sub&gt;L.

  - **Channel wise** - The channel adversarial droupout mask is defined as m&lt;sup&gt;adv&lt;/sup&gt; = argmax&lt;sub&gt;m&lt;/sub&gt; D [h(x; m&lt;sup&gt;s&lt;/sup&gt; ), h(x; m)], where 1/HW ∑ &#124;&#124;m&lt;sup&gt;s&lt;/sup&gt;(i) − m(i)&#124;&#124; ≤ δ&lt;sub&gt;c&lt;/sub&gt; C and h&lt;sub&gt;l&lt;/sub&gt;(x) ∈ R&lt;sup&gt;C×H×W&lt;/sup&gt;, where C, H, and W denote the channel, height,
    and width dimensions of the activation, respectively.

- **Drop to Adapt** - The overall loss function is sum of the objectives for task-specific, domain adaptation, entropy minimization and Virtual Adversarial Training(VAT).

  - _Task-specific objective_, L&lt;sub&gt;T&lt;/sub&gt;(S) = - E&lt;sub&gt;x&lt;sub&gt;s&lt;/sub&gt;, y&lt;sub&gt;s&lt;/sub&gt;&lt;sub&gt; ~ S&lt;/sub&gt;&lt;/sub&gt;[y&lt;sub&gt;s&lt;/sub&gt; &lt;sup&gt;T&lt;/sup&gt; log h(x &lt;sub&gt;s&lt;/sub&gt;)], where y&lt;sub&gt;s&lt;/sub&gt; is one-hot encoded vector of y&lt;sub&gt;s&lt;/sub&gt;.

  - _Domain adaptation objective_, L&lt;sub&gt;DTA&lt;/sub&gt;(T) = L&lt;sub&gt;fDTA&lt;/sub&gt;(T) + L&lt;sub&gt;cDTA&lt;/sub&gt;(T),
    where L&lt;sub&gt;fDTA&lt;/sub&gt;(T) = E&lt;sub&gt;x&lt;sub&gt;s&lt;/sub&gt; ~ T &lt;/sub&gt; [D&lt;sub&gt;KL&lt;/sub&gt;[h(x&lt;sub&gt;t&lt;/sub&gt;; m&lt;sup&gt;s&lt;/sup&gt;&lt;sub&gt;f&lt;/sub&gt; ), &#124;&#124;h(x&lt;sub&gt;t&lt;/sub&gt;; m&lt;sup&gt;adv&lt;/sup&gt;&lt;sub&gt;f&lt;/sub&gt;)&#124;&#124;],
    and L&lt;sub&gt;cDTA&lt;/sub&gt;(T) = E&lt;sub&gt;x&lt;sub&gt;s&lt;/sub&gt; ~ T &lt;/sub&gt; [D&lt;sub&gt;KL&lt;/sub&gt;[h(x&lt;sub&gt;t&lt;/sub&gt;; m&lt;sup&gt;s&lt;/sup&gt;&lt;sub&gt;c&lt;/sub&gt; ), &#124;&#124;h(x&lt;sub&gt;t&lt;/sub&gt;; m&lt;sup&gt;adv&lt;/sup&gt;&lt;sub&gt;c&lt;/sub&gt;)&#124;&#124;]

  - _Entropy minimization objective_, L&lt;sub&gt;E&lt;/sub&gt;(T) = - E&lt;sub&gt;x&lt;sub&gt;t&lt;/sub&gt;&lt;sub&gt; ~ S&lt;/sub&gt;&lt;/sub&gt;[h(x &lt;sub&gt;t&lt;/sub&gt;) &lt;sup&gt;T&lt;/sup&gt; log h(x &lt;sub&gt;t&lt;/sub&gt;)]

  - _VAT objective_, L&lt;sub&gt;V&lt;/sub&gt;(T) = E&lt;sub&gt;x&lt;sub&gt;t&lt;/sub&gt; ~ T &lt;/sub&gt; [max&lt;sub&gt;&#124;&#124;r&#124;&#124; ≤ ∈ &lt;/sub&gt; D&lt;sub&gt;KL&lt;/sub&gt;[h(x&lt;sub&gt;t&lt;/sub&gt;), &#124;&#124;h(x&lt;sub&gt;t&lt;/sub&gt; + r)&#124;&#124;]

## Experiment Result

### On Small Datasets

**SVHN ⟶ MNIST** - MNIST consists of binary handwritten
digit images, SVHN consists of coloured images of street
house numbers.

**MNIST ⟷ USPS** - MNIST and USPS contain grayscale
images.

**CIFAR ⟷ STL** - CIFAR and STL are 10-class object recognition datasets with coloured images.

&lt;div align="center"&gt;
&lt;div&gt;Results of experiment on small image datasets.&lt;/div&gt;
&lt;img src="./images/da_small.png"&gt;
&lt;/div&gt;

A substantial margin of improvement is achieved over the source only model across all domain configurations. In four of the five configurations, the stated method outperforms the recent state-of-the-art results.

### On Large Datasets

- The **VisDA-2017** image classification is a 12-class domain adaptation problem. The source domain consists of 152,397 synthetic images, where 3D CAD models are rendered from various conditions.

  &lt;div align="center"&gt;
  &lt;div&gt;Results on VisDA-2017 classification using ResNet-101&lt;/div&gt;
  &lt;img src="./images/da_large.png"&gt;
  &lt;/div&gt;
  The table clearly shows that the proposed method surpasses previous methods by a large margin. Note that all methods in this table use the same ResNet-101 backbone.

- For the source domain, the synthetic **GTA5 dataset** which consists of 24966 labelled images is used. As the target domain, the real-world **Cityscapes**, consisting of 5000 images is used.
  &lt;div align="center"&gt;
  &lt;div&gt;Results on GTA → Cityscapes, using a modified FCN with ResNet-50 as the base network&lt;/div&gt;
  &lt;img src="./images/da_large1.png"&gt;
  &lt;/div&gt;

The stated method clearly improves upon the mIoU of not only the source only model, but also competing methods. Even with the same training procedure and settings as in the classification experiments, DTA is extremely effective at adapting the most common classes in the dataset.

For code, visit this [link](https://github.com/postBG/DTA.pytorch).
