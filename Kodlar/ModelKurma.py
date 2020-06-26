import pandas as pd
import numpy as np


# Veri setlerinin yüklenmesi :
X = pd.read_excel("dataset.xlsx")
Y = pd.read_excel("dataset.xlsx")

# Eğitilen veri seçimi :
y_train = X["NO2"]
X_train = X.drop(["Tarih","NO2"], axis=1)
y_test = Y["NO2"]
X_test = Y.drop(["Tarih","NO2"], axis=1)

# Verileri dizi haline getirme :
y_train = np.array(y_train)
X_train = np.array(X_train)
y_test = np.array(y_test)
X_test = np.array(X_test)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
NN_model = Sequential()

# Giriş Katmanı :
NN_model.add(Dense(128, kernel_initializer='normal',input_dim = X_train.shape[1], activation='relu'))

# Ara Katman :
NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))

# Sonuç Katmanı :
NN_model.add(Dense(1, kernel_initializer='normal',activation='linear'))
NN_model.summary()

# Modelin Derlenmesi :
NN_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae','accuracy'])


history = NN_model.fit(X_train, y_train, epochs=500, batch_size=32,  verbose=1)

# Tahmin İşlemi :
predict = np.array(X_test)
predict1=NN_model.predict(predict)

print("Ortalama Eğitim kaybı : ", np.mean(NN_model.history.history["loss"]))
print("Ortalama Eğitim Başarımı : ", np.mean(NN_model.history.history["accuracy"]))




# Grafikle Gösterimi :
import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.plot(history.history['mae'])
plt.title('Model Kaybı')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['Eğitim', 'mae'], loc='upper left')
plt.show()
