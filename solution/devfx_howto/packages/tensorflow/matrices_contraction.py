import numpy as np
import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""
def test1():
    a = tf.constant([1], shape=[2, 3])
    b = tf.constant([2], shape=[3, 2])
    c1 = tf.einsum('ij,jk->ik', a, b)
    c2 = tf.tensordot(a, b, ([1], [0]))

    with tf.Session() as session:
        output = session.run(a)
        print('a-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run(b)
        print('b-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run([c1, c2])
        print('[c1-{}, c2-{}]:\n{}\n{}'.format(np.asarray(output[0]).shape, np.asarray(output[1]).shape, output[0], output[1]))

# if __name__ == '__main__':
#     test1()

"""------------------------------------------------------------------------------------------------
"""
def test2():
    a = tf.constant([1], shape=[2, 2, 3])
    b = tf.constant([2], shape=[4, 2, 3])
    c1 = tf.einsum('mij,nij->mn', a, b)
    c2 = tf.tensordot(a, b, ([1, 2], [1, 2]))

    with tf.Session() as session:
        output = session.run(a)
        print('a-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run(b)
        print('b-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run([c1, c2])
        print('[c1-{}, c2-{}]:\n{}\n{}'.format(np.asarray(output[0]).shape, np.asarray(output[1]).shape, output[0], output[1]))

# if __name__ == '__main__':
#     test2()

"""------------------------------------------------------------------------------------------------
"""
def test3():
    a = tf.constant([1], shape=[4, 2, 3])
    b = tf.constant([2], shape=[2, 2, 2, 3])
    c1 = tf.einsum('mij,nkij->mnk', a, b)
    c2 = tf.tensordot(a, b, ([1, 2], [2, 3]))

    with tf.Session() as session:
        output = session.run(a)
        print('a-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run(b)
        print('b-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run([c1, c2])
        print('[c1-{}, c2-{}]:\n{}\n{}'.format(np.asarray(output[0]).shape, np.asarray(output[1]).shape, output[0], output[1]))

# if __name__ == '__main__':
#     test3()

"""------------------------------------------------------------------------------------------------
"""
def test4():
    a = tf.constant([1], shape=[4, 2, 3])
    b = tf.constant([2], shape=[2, 2, 2, 3])
    c1 = tf.einsum('mij,nkij->mnk', a, b)
    c2 = tf.tensordot(a, b, ([1, 2], [2, 3]))

    with tf.Session() as session:
        output = session.run(a)
        print('a-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run(b)
        print('b-{}:\n{}'.format(np.asarray(output).shape, output))

        output = session.run([c1, c2])
        print('[c1-{}, c2-{}]:\n{}\n{}'.format(np.asarray(output[0]).shape, np.asarray(output[1]).shape, output[0], output[1]))

if __name__ == '__main__':
    test4()