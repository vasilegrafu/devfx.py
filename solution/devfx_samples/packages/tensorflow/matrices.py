import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


"""------------------------------------------------------------------------------------------------
"""
def test1():
    a = tf.constant(1, shape=[4, 2, 3])
    b = tf.constant(2, shape=[2, 3])
    c = tf.multiply(a, b)
    d = tf.reduce_sum(c, axis=0)

    with tf.Session() as session:
        output = session.run(a)
        print(output)

        output = session.run(b)
        print(output)

        output = session.run(c)
        print(output)

        output = session.run(d)
        print(output)

if __name__ == '__main__':
    test1()