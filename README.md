# What is RHCR?

RHCR is a Russian Handwriting Character Recognition (RHCR) project powered by TensorFlow

## How did RHCR come about?

The project originator (Ray) was trying to help out his sister with dissertation work; she had a lot of source material in handwritten Russian and needed a faster way to make the words legible. 

Aaron joined when he mentioned wanting to learn how to use some TensorFlow and wanting to become a data scientist or machine learning engineer to Ray.

## How it works

This repo is in development and uses TensorFlow 2 to perform handwriting recognition.

Synthetic Data is in ```/synthetic_data_generation```

Model development, training code, and saved models are in ```/model_training```

From phone call with Ray on April 6
1. Run wikidump
2. Run traindata 

## Current Status
From Ray:
"We left off at the final stages of synthetic data generation, but work could definitely be started on the model structure but the accuracy will be pointless"

Ran the TensorFlow TF2 migration script, but because the original mnist_saved_model script used tf.contrib, there will need to be manual code refactoring.

## Future Steps
1. Refactor to proper Tensorflow 2
2. Refactor from PIL to Pillow (Pillow supports Python 3, PIL does not)
3. Create requirements.txt for easier reproducibility
4. Dockerize?
5. Consider a PyTorch branch and see performance differences
6. Would more data help?

### From phone call with Ray on April 6
1. Better Bounding Box Drawing in Traindatagen.py
    a. Add random noise to the box dimensions?

2. A real CNN and spellchecker/RNN to get to text
    a. Possibly double sided if using CNN and RNN

3. Accuracy Assessment
    a. We are using Image of Text to Text

4. Image Warping/Colors/Damage (more realistic images)
    a. This part will be tedious due to matrix math

5. Make it faster

## Requirements

