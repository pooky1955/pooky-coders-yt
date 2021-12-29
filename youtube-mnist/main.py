import os
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D
from keras.models import Model

def create_model():
    in_layer = Input(shape=(28,28,1))
    conv = Conv2D(32,(3,3),activation="relu",padding="same")(in_layer)
    pool = MaxPool2D()(conv)
    conv = Conv2D(64,(3,3),activation="relu",padding="same")(pool)
    pool = MaxPool2D()(conv)
    flatten_layer = Flatten()(pool)

    dense = Dense(256,activation="relu")(flatten_layer)
    out_layer = Dense(10,activation="softmax")(dense)
    model = Model(in_layer,out_layer)
    model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
    return model

NUM_CLASSES = 10
def show_images(images,titles,layout=(3,3)):
    total = layout[0] * layout[1]
    for i in range(total):
        plt.subplot(layout[0],layout[1],i+1)
        plt.title(f"hello {titles[i]}")
        plt.imshow(images[i],cmap="gray")
    plt.show()
    
def one_hots(ys,num_classes):
    ohs = np.zeros((ys.shape[0],num_classes))
    for i, y in enumerate(ys):
        ohs[i][y] = 1
    return ohs

def load_data():
    (raw_X_train, raw_Y_train), (raw_X_test, raw_Y_test) = mnist.load_data()
    X_train = raw_X_train.astype("float32") / 255
    X_test = raw_X_test.astype("float32") / 255
    Y_train = one_hots(raw_Y_train,NUM_CLASSES)
    Y_test = one_hots(raw_Y_test,NUM_CLASSES)
    show_images(X_train,Y_train,(5,5))

    return (X_train, Y_train),(X_test,Y_test)

(X_train,Y_train),(X_test,Y_test)= load_data()
model = create_model()

model.fit(X_train,Y_train,validation_split=0.1,epochs=5,batch_size=32)
model.save("model.hdf5")




