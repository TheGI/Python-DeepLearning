import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

#x_train = [1,2,3]
#y_train = [1,2,3]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2000):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
                            feed_dict={X: [1,2,3], Y: [1,2,3]})

    # sess.run(train)
    if step % 100 == 0:
        # print(step, sess.run(cost), sess.run(W), sess.run(b))
        print(step, cost_val, W_val, b_val)
