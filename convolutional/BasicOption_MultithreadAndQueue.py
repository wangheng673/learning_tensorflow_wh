# -*- coding: utf-8 -*-
'''
    python file describe:multithreading and queue
'''
import tensorflow as tf
queue = tf.FIFOQueue(100, 'float')
enqueue_op = queue.enqueue([tf.random_normal([1])])
qr = tf.train.QueueRunner(queue, [enqueue_op]*5)
tf.train.add_queue_runner(qr)
out_tensor = queue.dequeue()

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)
    for _ in range(20): print(sess.run(out_tensor))
    coord.request_stop()
    print("hello word")
    coord.join(threads)
