from tensorflow import keras
from keras import datasets
import matplotlib.pyplot as plt
import numpy as np

#  LOAD AND SPLIT DATASET
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# check the shape of the data
# print(train_images.shape)

# view an image
# plt.imshow(train_images[0])
# plt.title(train_labels[0])
# plt.colorbar()
# plt.show()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# We will load already trained model here
model = keras.models.load_model("handwriting_CNN.h5")

# evaluating the model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# display test accuracy
print(test_acc)

# predict accuracy on the whole test dataset
predictions = model.predict(test_images)

# ask a user input index of a test set, display predicted number and real number
num = int(input("Enter the index of a number: "))
image = test_images[num]
label = test_labels[num]
print(f'prediction is {np.argmax(predictions[num])}')
print(f'Real number is {label}')

# display the image of a number
plt.imshow(test_images[num])
plt.show()
