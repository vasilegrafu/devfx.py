import numpy as np
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#----------------------------------------------------------------
# scalars
#----------------------------------------------------------------
def test_scalars():
    a = tf.constant(5, name="input_a")
    b = tf.constant(3, name="input_b")
    c = tf.multiply(a, b, name="mul_c")
    d = tf.add(a, b, name="add_d")
    e = tf.add(c, d, name="add_e")
    f = tf.add(d, e, name="add_f")

    with tf.Session() as session:
        output = session.run(f)
    print(output)

# test_scalars()

#----------------------------------------------------------------
# tensors
#----------------------------------------------------------------
def test_tensors():
    a = tf.constant([5, 3], name="input_a")
    b = tf.reduce_prod(a, name="prod_b")
    c = tf.reduce_sum(a, name="sum_c")
    d = tf.add(b, c, name="add_d")

    with tf.Session() as session:
        output = session.run(d)
    print(output)

# test_tensors()

#----------------------------------------------------------------
# tensor dtypes
#----------------------------------------------------------------
def test_dtypes():
    a = np.array([2, 3], dtype=np.int32)
    b = np.array([4, 5], dtype=np.int32)
    c = tf.add(a, b)

    with tf.Session() as session:
        output = session.run(c)
    print(output)

# test_dtypes()

#----------------------------------------------------------------
# tensor board
#----------------------------------------------------------------
def test_tensor_board():
    a = tf.constant(5, name="input_a")
    b = tf.constant(3, name="input_b")
    c = tf.multiply(a, b, name="mul_c")
    d = tf.add(a, b, name="add_d")
    e = tf.add(c, d, name="add_e")
    f = tf.add(d, e, name="add_f")

    with tf.Session() as session:
        summary_file_writer = tf.summary.FileWriter('./tensor_board')
        summary_file_writer.add_graph(graph=session.graph)
        output = session.run(f)
    print(output)

# test_tensor_board()

#----------------------------------------------------------------
# graph
#----------------------------------------------------------------
def test_graph():
    graph = tf.Graph()

    with tf.Graph().as_default() as graph:
        a = np.array([2, 3], dtype=np.int32)
        b = np.array([4, 5], dtype=np.int32)
        c = tf.add(a, b)

    with tf.Session(graph=graph) as session:
        output = session.run(c)
    print(output)

# test_graph()

#----------------------------------------------------------------
# graphs
#----------------------------------------------------------------
def test_graphs():
    with tf.Graph().as_default() as graph1:
        a1 = np.array([2, 3], dtype=np.int32)
        b1 = np.array([4, 5], dtype=np.int32)
        c1 = tf.add(a1, b1)
    with tf.Session(graph=graph1) as session:
        output1 = session.run(c1)
    print(output1)

    with tf.Graph().as_default() as graph2:
        a2 = np.array([2, 3], dtype=np.int32)
        b2 = np.array([4, 5], dtype=np.int32)
        c2 = tf.add(a2, b2)
    with tf.Session(graph=graph2) as session:
        output2 = session.run(c2)
    print(output2)

# test_graphs()

#----------------------------------------------------------------
# session
#----------------------------------------------------------------
def test_session():
    with tf.Graph().as_default() as graph:
        a = np.array([1, 2], dtype=np.int32)
        b = np.array([3, 4], dtype=np.int32)
        c = tf.add(a, b)

    with tf.Session(graph=graph) as session:
        output = session.run(c)
    print(output)

    with tf.Session(graph=graph).as_default():
        output = c.eval()
    print(output)

# test_session()

#----------------------------------------------------------------
# placeholders
#----------------------------------------------------------------
def test_placeholders():
    with tf.Graph().as_default() as graph:
        # Creates a placeholder vector of any length with data type int32
        a = tf.placeholder(tf.int32, shape=[None], name="input")

        # Use the placeholder as if it were any other Tensor object
        b = tf.reduce_prod(a, name="prod_b")
        c = tf.reduce_sum(a, name="sum_c")

        # Finish off the graph
        d = tf.add(b, c, name="add_d")

    with tf.Session(graph=graph) as session:
        output = session.run(d, feed_dict={a: [4, 5, 6]})
    print(output)

    with tf.Session(graph=graph).as_default():
        output = d.eval(feed_dict={a: [4, 5, 6]})
    print(output)

# test_placeholders()

#----------------------------------------------------------------
# variables
#----------------------------------------------------------------
def test_variables():
    with tf.Graph().as_default() as graph:
        a = tf.Variable(initial_value=1, name="a")
        b = tf.Variable(initial_value=2, name="b")
        c = tf.Variable(initial_value=0, name="c")
        d = c.assign(a + b + c)

        global_variables_initializer = tf.global_variables_initializer()

    with tf.Session(graph=graph).as_default() as session:
        session.run(global_variables_initializer)
        output = session.run(d)
        print(output)
        output = session.run(d)
        print(output)

# test_variables()

#----------------------------------------------------------------
# arrays
#----------------------------------------------------------------
def test_arrays():
    with tf.Graph().as_default() as graph:
        x1_1 = tf.constant(1, name="x1")
        x1_2 = tf.constant(1, name="x2")

        w2_11 = tf.Variable(initial_value=1, name="w2_11")
        w2_21 = tf.Variable(initial_value=1, name="w2_21")
        n2_1 = w2_11 * x1_1 + w2_21 * x1_2

        w2_12 = tf.Variable(initial_value=1, name="w2_12")
        w2_22 = tf.Variable(initial_value=1, name="w2_22")
        n2_2 = w2_12 * x1_1 + w2_22 * x1_2

        w2_13 = tf.Variable(initial_value=1, name="w2_13")
        w2_23 = tf.Variable(initial_value=1, name="w2_23")
        n2_3 = w2_13 * x1_1 + w2_23 * x1_2

        w3_11 = tf.Variable(initial_value=1, name="w3_11")
        w3_21 = tf.Variable(initial_value=1, name="w3_21")
        w3_31 = tf.Variable(initial_value=1, name="w3_31")
        n3_1 = w3_11 * n2_1 + w3_21 * n2_2 + w3_31 * n2_3

        w3_12 = tf.Variable(initial_value=1, name="w3_12")
        w3_22 = tf.Variable(initial_value=1, name="w3_22")
        w3_32 = tf.Variable(initial_value=1, name="w3_32")
        n3_2 = w3_12 * n2_1 + w3_22 * n2_2 + w3_32 * n2_3

        n = n3_1 + n3_2

        global_variables_initializer = tf.global_variables_initializer()

    with tf.Session(graph=graph).as_default() as session:
        session.run(global_variables_initializer)
        output = session.run(n)
    print(output)

test_arrays()

#----------------------------------------------------------------
# namespaces
#----------------------------------------------------------------
def test_namespaces():
    with tf.Graph().as_default() as graph:
        with tf.name_scope("input_layer"):
            input = tf.placeholder(tf.float64, shape=[None], name="input")

        with tf.name_scope("intermadiate_layer"):
            prod = tf.reduce_prod(input, name="prod")
            sum = tf.reduce_sum(input, name="sum")

        with tf.name_scope("output_layer"):
            output = tf.add(prod, sum, name="add")

        with tf.name_scope("status_layer"):
            execution_count = tf.Variable(0, dtype=tf.int64, trainable=False, name="execution_count")
            execution_count_updater = execution_count.assign_add(1)

            accumulated_output = tf.Variable(0.0, dtype=tf.float64, trainable=False, name="accumulated_output")
            accumulated_output_contribution = tf.placeholder(tf.float64, shape=[], name="accumulated_output_contribution")
            accumulated_output_updater = accumulated_output.assign_add(accumulated_output_contribution)

        with tf.name_scope("summaries"):
            output_summary_value = tf.placeholder(tf.float64, shape=[], name="output_summary_value")
            output_summary = tf.summary.scalar("output", output_summary_value)

            execution_count_summary_value = tf.placeholder(tf.float64, shape=[], name="execution_count_summary_value")
            execution_count_summary = tf.summary.scalar("execution_count", execution_count_summary_value)

            accumulated_output_summary_value = tf.placeholder(tf.float64, shape=[], name="accumulated_output_summary_value")
            accumulated_output_summary = tf.summary.scalar("accumulated_output", accumulated_output_summary_value)

        global_variables_initializer = tf.global_variables_initializer()

    with tf.Session(graph=graph).as_default() as session:
        session.run(global_variables_initializer)

        summary_file_writer = tf.summary.FileWriter('./tensor_board')
        summary_file_writer.add_graph(graph=session.graph)

        def session_run(tensor):
            evaluated_output = session.run(output, feed_dict={input: tensor})
            evaluated_output_summary = session.run(output_summary, feed_dict={output_summary_value: evaluated_output})
            summary_file_writer.add_summary(evaluated_output_summary)

            evaluated_execution_count = session.run(execution_count_updater)
            evaluated_execution_count_summary = session.run(execution_count_summary, feed_dict={execution_count_summary_value: evaluated_execution_count})
            summary_file_writer.add_summary(evaluated_execution_count_summary)

            evaluated_accumulated_output = session.run(accumulated_output_updater, feed_dict={accumulated_output_contribution: evaluated_output})
            evaluated_accumulated_output_summary = session.run(accumulated_output_summary, feed_dict={accumulated_output_summary_value: evaluated_accumulated_output})
            summary_file_writer.add_summary(evaluated_accumulated_output_summary)

            print(evaluated_output, evaluated_execution_count, evaluated_accumulated_output)

        session_run([1, 2])
        session_run([2, 3])
        session_run([3, 4])
        session_run([5, 6])

        summary_file_writer.flush()
        summary_file_writer.close()

# test_namespaces()






