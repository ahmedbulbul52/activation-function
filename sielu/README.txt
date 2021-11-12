This is an activation function can be used in deep learning model development.
Installation command: pip3 install sielu
Alternately,

from keras.utils.generic_utils import get_custom_objects
import tensorflow as tf
def sielu(x):
    return 0.5 * x * (1 + tf.sigmoid(tf.sqrt(2 / np.pi) * (x + 0.044715 * tf.pow(x, 3))))
get_custom_objects().update({'sielu': sielu})
sielu = ['sielu']
