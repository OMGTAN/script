import tensorflow as tf
import numpy as np

a  = np.array([[3, 4], [2, 16]])  # 初始化一个非奇异矩阵(数组)

# 矩阵对象可以通过 .I 更方便的求逆
A = np.matrix(a)
print(A.I)