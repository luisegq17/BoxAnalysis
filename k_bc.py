import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from json_to_np import x_train, y_train
from k_c_xtest import x_test

model = Sequential()
model.add(Dense(64, input_dim=5, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(
    x_train,
    y_train,
    epochs=8,
    batch_size=8
)

y_test=model.predict(x_test)
print(y_test)