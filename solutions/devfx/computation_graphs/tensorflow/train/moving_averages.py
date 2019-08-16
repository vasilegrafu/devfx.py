import tensorflow as tf

def ema(decay=0.95):
    return tf.train.ExponentialMovingAverage(decay=decay)