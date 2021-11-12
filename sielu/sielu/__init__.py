from __future__ import division, print_function
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from keras.models import Sequential,load_model
from keras.layers import LSTM,Dense,Dropout, Activation
import keras
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import StratifiedKFold
import seaborn as sns
import tensorflow as tf
from keras.layers import LeakyReLU
from keras.utils.generic_utils import get_custom_objects

# Add the GELU function to Keras
def sielu(x):
    return 0.5 * x * (1 + tf.sigmoid(tf.sqrt(2 / np.pi) * (x + 0.044715 * tf.pow(x, 3))))
get_custom_objects().update({'sielu': sielu})
sielu = ['sielu']