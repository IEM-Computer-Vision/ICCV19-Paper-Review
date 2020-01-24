# Adversarial Robustness vs. Model Compression, or Both?
Reviewed by [Shatadru Majumdar](https://www.linkedin.com/in/shatadru-majumdar-ab262317b/)
## What is Adversarial Robustness?
* Adversarial attacks on deep neural networks (DNNs) are implemented by generating adversarial examples i.e. adding sophisticated perturbations on input examples (which were previously correctly classified) such that those examples are now wrongly classified with high confidence. Adversarial robustness requires adversarial training.
* Most defenses cause obfuscated gradients which can defeat iterative optimization based attacks but can be circumvented by attacks like, backward pass differentiable approximation, expectation over transformation, and reparameterization.
* Adversarial training leveraging min-max robust optimization does not have obfuscated gradients issue and can provide security against all first-order adversaries through the inner maximization problem while the outer minimization represents the training process.
* Adversarial robustness requires a significant larger architectural capacity of the network than that for the natural training thus limiting it's use for resource-constrained environments.
## Weight Pruning for Model Compression:
* Weight pruning is a model compression technique for facilitating DNN implementations on resource constrained application systems, and it explores weight sparsity to prune synapses and consequently neurons (by setting their values to zero) without notable accuracy degradation.
* The regular pruning scheme can preserve the model's architecture in some sense and can be further classified into:
  1. Filter pruning prunes whole filters from a layer by setting their values to zero.
  2. Column pruning prunes weights for all filters in a layer, at the same locations.
* In irregular pruning scheme, we prune the elements in a particular layer without considering whether they belong to the same filter or column.
* Two previous important hypothesis on weight pruning which are explored in this paper:
  1. The lottery ticket hypothesis as mentioned in this [paper](https://arxiv.org/abs/1803.03635) states that dense, randomly-initialized, feed-forward networks contain subnetworks (winning tickets) that when trained in isolation — reach test accuracy comparable to the original network in a similar number of iterations. The original initilizaiton of the sub-network (before the large network pruning) is needed for it to achieve competitive performance when trained in isolation.
  2. This [paper](https://arxiv.org/abs/1810.05270) implies that: 
      * training a large, over-parameterized model is often not necessary to obtain an efficient final model
      * learned “important” weights of the large model are typically not useful for the small pruned model
      * the pruned architecture itself, rather than a set of inherited “important” weights, is more crucial to the efficiency in the final model.
## This paper's contribution:
* They built a framework that achieves both adversarial robustness and model compression through implementing concurrent weight pruning and adversarial training.
* They used the ADMM (alternating direction method of multipliers) based pruning in their framework due to its compatibility with adversarial training and that it supports both irregular pruning and different kinds of regular pruning.
* They also studied the above two hypotheses about weight pruning and experimentally examined their validness for the adversarial training setting.
* They systematically investigated the effect of different pruning schemes on adversarial robustness and model compression.
## Observations:
<p>
  <img src="https://github.com/shatadru99/ICCV19-Paper-Review/blob/name-paper_reviews/images/t3.JPG">
</p>

<p>
  <img src="https://github.com/shatadru99/ICCV19-Paper-Review/blob/name-paper_reviews/images/t1.JPG">
</p>

<p>
  <img src="https://github.com/shatadru99/ICCV19-Paper-Review/blob/name-paper_reviews/images/t2.JPG">
</p>

<p>
  <img src="https://github.com/shatadru99/ICCV19-Paper-Review/blob/name-paper_reviews/images/t4.JPG">
</p>



* Fig 1 shows that Adversarially trained model is less sparse (fewer zero weights) than naturally trained model. Therefore, pre-pruning before adversarial training is not a feasible solution.
* Table 2 shows that the value of weight pruning is essential in the adversarial training setting: it is possible to acquire a network of small model size (by weight pruning) with both high natural test accuracy and adversarial test accuracy. By contrast, one may lose the natural and adversarial test accuracy if the adversarial training is directly applied to a small-size network that is not acquired from weight pruning and thus proves that this [paper](https://arxiv.org/abs/1810.05270) is not applicable in adversarial settings.
* Table 3 suggests that weight pruning in adversarial settings is out-of-scope of [the lottery ticket hypothesis](https://arxiv.org/abs/1803.03635).
* The concurrent adversarial training and weight pruning yields the pruned model robust to transfer attacks. But, experiments on cross-transfer attacks with adversarial examples generated by PGD attack on baseline model imply that the model is most vulnerable against adversarial examples generated by itself, regardless of the size of the model.
* The figure (a) shows that irregular pruning scheme is the best for preserving both standard accuracy and adversarial robustness while pruning the DNN models.

> Code for this paper is made available [here](https://github.com/yeshaokai/Robustness-Aware-Pruning-ADMM) by the authors.
