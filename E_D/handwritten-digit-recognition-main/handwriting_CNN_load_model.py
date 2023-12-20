from tensorflow import keras
from keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

#  LOAD AND SPLIT DATASET
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# # check the shape of the data
# print(train_images.shape)
#
# # check the datatype
# print(type(train_images))
#
# # view an image
# plt.imshow(train_images[0])
# plt.title(train_labels[0])
# plt.colorbar()
# plt.show()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0


# creating a model
model = models.Sequential()
model.add(layers.Conv2D(64, (5, 5), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#print(model.summary())

# adding dense layers
model.add(layers.Flatten())
model.add(layers.Dense(128, keras.activations.relu))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(64, keras.activations.relu))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, keras.activations.softmax))

#print(model.summary())

# train model
model.compile(keras.optimizers.Adam(learning_rate=0.003),
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# create a callback
checkpoint_cb = keras.callbacks.ModelCheckpoint("handwriting_CNN.h5", save_best_only=True)

model.fit(train_images, train_labels, epochs=10, validation_split=0.2, callbacks=checkpoint_cb)


# # evaluating the model
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# print(test_acc)
#
# predictions = model.predict(test_images)
#
# num = int(input("Enter the index of a number: "))
# image = test_images[num]
# label = test_labels[num]
# print(f'prediction is {np.argmax(predictions[num])}')
# print(f'Real number is {label}')
# plt.imshow(test_images[num])
# plt.show()