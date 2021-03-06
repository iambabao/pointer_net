# -*- coding: utf-8 -*-

"""
@Author             : Bao
@Date               : 2020/6/29 22:29
@Desc               : 
@Last modified by   : Bao
@Last modified date : 2020/6/29 22:29
"""

import tensorflow as tf


class CustomSchedule:
    def __init__(self, d_model, global_step, warmup_steps=4000):
        self.d_model = tf.cast(d_model, tf.float32)
        self.global_step = tf.cast(global_step, tf.float32)
        self.warmup_steps = warmup_steps

    def __call__(self):
        arg1 = tf.math.rsqrt(self.global_step)
        arg2 = self.global_step * (self.warmup_steps ** -1.5)

        return tf.math.rsqrt(self.d_model // 2) * tf.math.minimum(arg1, arg2)
