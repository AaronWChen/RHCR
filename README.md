# What is RHCR?

RHCR is a Russian Handwriting Character Recognition (RHCR) project powered by Tensorflow

## How did RHCR come about?

The project originator (Ray) was trying to help out his sister with dissertation work; she had a lot of source material in handwritten Russian and needed a faster way to make the words legible. 

Aaron joined when he mentioned wanting to learn how to use some TensorFlow and wanting to become a data scientist or machine learning engineer to Ray.

## How it works

This repo is in development and uses Tensorflow to perform handwriting recognition.

Synthetic Data is in ```/synthetic_data_generation```

Model development, training code, and saved models are in ```/model_training```

## Future Steps
1. Refactor to proper Tensorflow 2
2. Refactor from PIL to Pillow (Pillow supports Python 3, PIL does not)
3. Create requirements.txt for easier reproducibility
4. Dockerize?
5. Consider a PyTorch branch and see performance differences
6. Would more data help?

## Requirements

