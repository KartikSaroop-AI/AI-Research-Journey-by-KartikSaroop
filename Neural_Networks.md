<div align="center">
  
# 🧠 Neural Networks – My Learning Journey

</div>

Welcome to my **Neural Networks Learning Log**, where I document everything I learn and build while exploring the foundations and advanced concepts of **Deep Learning**.  

This file serves as a structured collection of my **daily experiments**, **hands-on implementations**, and **conceptual understanding** of how neural networks learn, generalize, and make intelligent predictions. Each experiment focuses on a specific theme — from basic architectures to advanced models like **CNNs**, **RNNs**, and **Transformers** — with clear explanations, practical code, and reflections.



## 🗂️ Table of Contents

| No. | Section | Description | Status |
|:----|:--------|:-------------|:--------|
| 1 | [Introduction & Basics](#1--introduction--basics) | Overview of neural networks, perceptrons, activation functions, and loss concepts. | 🟡 In Progress |
| 2 | [Feedforward Neural Networks (ANN)](#2--feedforward-neural-networks-ann) | Simple multilayer networks and MNIST digit classification experiments. | 🟡 In Progress|
| 3 | [Convolutional Neural Networks (CNN)](#3--convolutional-neural-networks-cnn) | Deep learning for image recognition and feature extraction. | 🟡 In Progress |
| 4 | [Recurrent Neural Networks (RNN)](#4--recurrent-neural-networks-rnn) | Sequence modeling using time-series and text data. | 🔜 Upcoming |
| 5 | [LSTM & GRU Networks](#5--lstm--gru-networks) | Handling long-term dependencies in sequential data. | 🔜 Upcoming |
| 6 | [Transformers & Attention Mechanisms](#6--transformers--attention-mechanisms) | Modern architectures like BERT and GPT for sequence understanding. | 🔜 Upcoming |
| 7 | [Experiment Logs](#7--experiment-logs) | All experiments performed in TensorFlow/Keras with notebooks and notes. | 🟢 Ongoing |
| 8 | [Articles & External Resources](#8--articles--external-resources) | Curated articles, blogs, and papers related to neural networks. | 🟢 Updating |

---

## 1️⃣ Introduction & Basics
- Overview of artificial neurons, forward propagation, and backpropagation.
- Activation functions: Sigmoid, ReLU, Softmax.
- Loss functions and optimization concepts.

---

## 2️⃣ Feedforward Neural Networks (ANN)


---

## 3️⃣ Convolutional Neural Networks (CNN)
- To explore feature extraction using convolution and pooling layers.
- Planned experiments: CIFAR-10 classification with dropout and data augmentation.
- Related articles to be added.

---


## 4️⃣ Recurrent Neural Networks (RNN)
#### ⚙️ **Experiment 1 – MNIST Classification (Baseline)**  
A fully connected neural network trained on MNIST to establish a baseline for comparison with RNN-based models.  
- 🎯 **Goal:** Understand data representation without sequential modeling.  
- 📓 [mnist.ipynb](Notebooks/mnist.ipynb)


#### ⚙️ **Experiment 2 – TensorFlow Callbacks (EarlyStopping & ModelCheckpoint)**  
Implemented callback functions to optimize training efficiency and prevent overfitting.  
- 🎯 **Goal:** Use `EarlyStopping` and `ModelCheckpoint` in TensorFlow/Keras.  
- 📓 [mnist_callbacks.ipynb](Notebooks/mnist_callbacks.ipynb)  
- 📘 [Notes (PDF)](Docs/TensorFlow_Callbacks.pdf)

---

## 5️⃣ LSTM & GRU Networks
- Understanding vanishing gradients and how LSTM/GRU overcome them.
- Planned notebooks: language modeling and temperature-based text generation.

---

## 6️⃣ Transformers & Attention Mechanisms
- Learn about self-attention, positional encoding, and encoder-decoder models.
- Future experiments: text summarization, question answering, and translation.

---

## 7️⃣ Experiment Logs
| No. | Experiment | Topic | Notebook | Notes |
|:----|:------------|:------|:----------|:------|
| 1 | Feedforward Neural Network | MNIST Classification | [mnist.ipynb](Notebooks/mnist.ipynb) | — |
| 2 | TensorFlow Callbacks | EarlyStopping & ModelCheckpoint | [mnist_callbacks.ipynb](Notebooks/mnist_callbacks.ipynb) | [PDF Notes](Docs/TensorFlow_Callbacks.pdf) |
| 3 | CNN on CIFAR-10 *(Upcoming)* | — | — | — |

---

## 8️⃣ Articles & External Resources
| Topic | Resource | Type |
|:------|:----------|:------|
| Neural Network Fundamentals | [Neural Networks and Deep Learning – Michael Nielsen](http://neuralnetworksanddeeplearning.com/) | Book |
| CNNs Explained | [CS231n Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/convolutional-networks/) | Course Notes |
| RNNs & LSTMs | [Understanding LSTM Networks – Colah’s Blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) | Blog |
| Transformers | [The Illustrated Transformer – Jay Alammar](https://jalammar.github.io/illustrated-transformer/) | Article |


⭐ *This document is continuously evolving as I dive deeper into neural network architectures and their real-world applications.*
