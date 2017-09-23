import numpy as np

np.random.seed(123)  # for reproducibility
np.set_printoptions(threshold='nan')
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from scipy import misc
import os
from keras import backend as K
K.set_image_dim_ordering('th')

# 4. Load pre-shuffled MNIST data into train and test sets
#(X_train, y_train), (X_test, y_test) = mnist.load_data()

#TODO: Read names of matrices to an array with os.listdir
# A vector of filenames.
matrices = os.listdir("image_400")
print len(matrices)
matrices.remove(".DS_Store")
#min type is 0 for COO, 1 for CSR, 2 for ELL
type = open("min_type.txt", 'r')
types = []
count = 0
for line in type:
    type_data = line.rstrip().split(' ')
    if matrices[count] == type_data[0]+".png":
        types.append(type_data[1])
        count += 1
#TODO: Read values of spmv from min_type to an array
# `labels[i]` is the label for the image in `filenames[i].

images = []
image_size = 400
for im in matrices:
    image = misc.imread("image_400/" + im)
    images.append(image)

(X_train, y_train) = (images[:-180], types[:-180])
(X_test, y_test) = (images[-180:], types[-180:])

X_train = np.array(X_train)
X_test = np.array(X_test)

# 5. Preprocess input data
X_train = X_train.reshape(X_train.shape[0], 3, image_size, image_size)
X_test = X_test.reshape(X_test.shape[0], 3, image_size, image_size)

# 6. Preprocess class labels
Y_train = np_utils.to_categorical(y_train, 3)
Y_test = np_utils.to_categorical(y_test, 3)

# 7. Define model architecture
model = Sequential()

model.add(Conv2D(20, (5, 5), activation='relu', input_shape=(3, image_size, image_size)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(50, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='softmax'))

# 8. Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 9. Fit model on training data
model.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

# 10. Evaluate model on test data
score = model.evaluate(X_test, Y_test, verbose=0)
print "result on test set:" + str(score)
