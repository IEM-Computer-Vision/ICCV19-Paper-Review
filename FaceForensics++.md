# FaceForensics++: Learning to Detect Manipulated Facial Images
- [Shatadru Majumdar](https://www.linkedin.com/in/shatadru-majumdar-ab262317b)

The rapid progress in synthetic face generation and manipulation poses significant threat, like, loss of trust in online content, spreading of false news and many more. This paper gives an overview of the current state-of-the-art face manipulation methods, the existing Forensic analysis datasets, the different forgery detector architectures.
This paper makes the following contributions:
- an automated benchmark for facial manipulation detection under random compression for a standardized comparison, including a human baseline
- a novel large-scale dataset of manipulated facial imagery composed of more than 1.8 million images from 1,000 videos with pristine (i.e., real) sources and target ground truth to enable supervised learning
- an extensive evaluation of state-of-the-art hand-crafted and learned forgery detectors in various scenarios
 - a state-of-the-art forgery detection method tailored to facial manipulations.
## PROPOSED DATASET
They created the FaceForensics++ dataset, which is an extension from the previous FaceForensics dataset and is a large-scale dataset which enables researchers to train state-of-the-art forgery detectors for facial image manipulation in a supervised fashion.
They downloaded 1000 pristine videos from the Internet, performed manual screening of the resulting clips to ensure a high-quality video selection and to avoid videos with face occlusions. They selected 1,000 video sequences containing 509,914 images which to use as their pristine data.
To generate a large scale manipulation dataset, they adopted two computer-graphics based approaches (Face2Face and FaceSwap) and two deep-learning based approaches (DeepFakes and NeuralTextures).
- Face2Face:  Face2Face is a facial reenactment system that transfers the expressions of a source video to a target video while maintaining the identity of the target person.
- FaceSwap:  FaceSwap is a graphics-based approach to transfer the face region from a source video to a target video.
- DeepFakes: In DeepFakes, a face in a target sequence is replaced by a face that has been observed in a source video or image collection.
- NeuralTextures: NeuralTextures uses the original video data to learn a neural texture of the target person, including a rendering network. This is trained with a photometric reconstruction loss in combination with an adversarial loss.
 
To create a realistic setting for manipulated videos, they generate output videos with different quality levels –
a) Raw
b) High Quality (constant rate quantization parameter 23)
c) Low Quality (constant rate quantization parameter 40)
