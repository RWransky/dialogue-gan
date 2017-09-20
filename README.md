# Tensorflow 1.3+ Implementation of Adversarial Learning for Neural Dialogue Generation

Algorithms derived from this [paper](https://arxiv.org/pdf/1701.06547.pdf) by Stanford's Jiwei Li et al.


## Requirements:
Updated and improved from earlier versions now supporting:
TensorFlow 1.3+  Python 3.6+



## Model Overview:
The model is based on generative adversarial architectures with a Generative model learning to create examples to be evaluated by a Discriminator model. 

**Generative Model**: Since this is a NLP task we use a Seq2Seq setup utilizing a GRU cell to implement attention.

**Discriminator Model**: Hierarchical RNN as used in Iulian V. Serban's [paper](http://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/11957/12160).

As discussed by Jiwei Li et al. discrete problems such as dialogue generation have been difficult to train using a reinforcement strategy. Li implemented a Monte Carlo search amongst partially decoded sequences to develop a method of reward for the reinforcement.


## Contributors and Special Thanks:
Many thanks to @liuyuemaicha for providing the initial code base for Tensorflow < 1.x.

