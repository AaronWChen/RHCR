"""
This script is a refactor of the original mnist_saved_model.py originally included in the repo. 
The original was written in 2016 by Google and the original tutorial does not seem to be available 
anymore. 

Also, TensorFlow 2 debuted in September 2019, so refactoring to TF 2 seemed like a good idea.

It is based on the tutorial "Multi-class classification with MNIST" colab notebook:
https://colab.research.google.com/github/google/eng-edu/blob/master/ml/cc/exercises/multi-class_classification_with_MNIST.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=multiclass_tf2-colab&hl=en

Requires Python 3, TensorFlow 2
Easiest way to work is to pip install the requirements.txt file

Train and export a simple Softmax Regression TensorFlow model.
The model is from the TensorFlow "MNIST For ML Beginner" tutorial. This program
simply follows all its training instructions, and uses TensorFlow SavedModel to
export the trained model with proper signatures that can be loaded by standard
tensorflow_model_server.

Usage: mnist_saved_model.py [--training_iteration=x] [--model_version=y] export_dir
"""

from __future__ import absolute_import, division, print_function, unicode_literals
import os
import sys
import tensorflow as tf
from tensorflow.keras import Layers
import mnist_input_data
import numpy as np
import pandas as pd

tf.compat.v1.app.flags.DEFINE_integer('training_iteration', 1000,
                            'number of training iterations.')
tf.compat.v1.app.flags.DEFINE_integer('model_version', 1, 'version number of the model.')
tf.compat.v1.app.flags.DEFINE_string('work_dir', '/tmp', 'Working directory.')
FLAGS = tf.compat.v1.app.flags.FLAGS

