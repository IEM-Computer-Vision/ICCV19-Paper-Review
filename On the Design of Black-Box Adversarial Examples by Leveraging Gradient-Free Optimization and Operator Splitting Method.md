# On the Design of Black-box Adversarial Examples by LeveragingGradient-free Optimization and Operator Splitting Method
Reviewed by [Shatadru Majumdar](https://www.linkedin.com/in/shatadru-majumdar-ab262317b/)
## What are Adversarial Attacks?
Adding a very small amount of noise to a correctly classified image, we can fool our deep neural nets into incorrectly classifying the image with high confidence. These are known as adversarial attacks. When the attacker has access to the model’s architecture and internal parameters, then it is a white-box attack and otherwise, it is a black-box attack.
## Introduction:
Adversarial attacks raise security concerns about the robustness of DNNs in extreme situations such as face recognition, autonomous driving car and malware detection, and hence, investigating adversarial examples is an extremely prevalent field. However, existing studies on black-box adversarial attacks are still restricted to very specific settings of threat models (e.g. single distortion techniques and restrictive assumption on target model’s feedback to queries) and/or suffer from prohibitively high query complexity. Also, white-box attack methods are not adapted to practical black-box threat models.
## This Paper’s Contribution:
* This paper proposes a general black-box adversarial attack framework via ADMM, including zeroth-order ADMM (ZO-ADMM) and ADMM with Bayesian optimization (BO-ADMM). They used ZO-ADMM with random gradient estimation (RGE) to avoid the intensive query complexity of attacks. Besides, the ADMM with BO gives higher query efficiency in black-box settings.
* They further generalized the formulation to accommodate various bounded ℓp-norm-ball distortion metrics unlike the other black-box attacks, which are often heavily customized towards a specific norm-ball (e.g., ℓ2 or ℓ∞) for distortion metrics.
* This framework can be applied to both score-based (the attacker to have access to a vector of assessment scores for all output candidates, called, soft labels) and decision based settings (the attacker has access to the system’s final decision on the most probable output, called, hard labels).
* Finally, they demonstrated the efficiency of the framework on a variety of real-world image classification datasets such as MNIST, CIFAR-10 and ImageNet. 
## Evaluation:

<p>
  <img src="https://github.com/shatadru99/ICCV19-Paper-Review/blob/name-paper_reviews/images/BlackBox_FrameWork_Results.JPG">
</p>

<p>
  <img src="https://github.com/shatadru99/ICCV19-Paper-Review/blob/name-paper_reviews/images/table.JPG">
</p>

(These values are obtained for certain near-optimal values of various internal parameters). </br> The empirical results consistently show that this framework performs competitively to existing works in terms of the attack success rate while achieving a significant reduction on the query complexity. </br>

>Code for this paper is available [here](https://github.com/LinLabNEU/Blackbox_ADMM).
