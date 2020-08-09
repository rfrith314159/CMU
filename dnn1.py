import sys
import tensorflow
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

def main():
    print("Deep Learning Neural Net")
    # generate training dummy data for 1000 students and dummy test data for 500
    # columns: age, hours of study, average previous test scores
    # set seed for reproducibility
    np.random.seed(2018)
    train_data, test_data = np.random.random((1000,3)), np.random.random((500,3))
    # generate dummy results for 1000 students : whether passed (1) or failed (0)
    labels = np.random.randint(2, size=(1000,1))

    #defining the model structure with the required layers, # of neurons, activation function, and optimizers
    model = Sequential()
    model.add(Dense(5, input_dim=3, activation="relu"))
    model.add(Dense(4, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    #train the model and make predictions
    model.fit(train_data, labels, epochs=10, batch_size=32)

    #make predictions from the trained model
    predictions = model.predict(test_data)



if __name__ == '__main__':
    main()
