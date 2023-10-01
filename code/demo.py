import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import TensorBoard

# 创建TensorBoard回调
tensorboard_callback = TensorBoard(log_dir='./logs', histogram_freq=1)

# 创建并编译您的深度学习模型
model = keras.Sequential([...])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 训练模型并将TensorBoard回调传递给fit方法
model.fit(train_data, train_labels, epochs=10, callbacks=[tensorboard_callback])
