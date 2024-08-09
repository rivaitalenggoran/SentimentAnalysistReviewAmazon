import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
from sklearn.preprocessing import MinMaxScaler
from keras import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
from tensorflow.keras.layers import Dropout
from keras.src.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

filepath = 'Dataset//Electronics_sampled.csv'
data = pd.read_csv(filepath)

#Analisis Menggunakan Statistika Deskriptif--------------------------------------------------------

#Rata-Rata Rating dan Helpful Vote-----------------------------------------------------------------------------------------
mean_Rating = data['rating'].mean()
mean_HelpfulVote = data['helpful_vote'].mean()
print("Rata-Rata Rating : ", math.floor(mean_Rating))
print("Rata-Rata Ulasan Bermanfaat : ", math.floor(mean_HelpfulVote))

#Median Rating---------------------------------------------------------------------------------------
median_Rating = data['rating'].median()
median_HelpfulVote = data['helpful_vote'].median()
print("Median Rating : ", math.floor(median_Rating))
print("Median Ulasan Bermanfaat : ", math.floor(median_HelpfulVote))


#Modulo Rating---------------------------------------------------------------------------------------
modulo_Rating = data['rating'].std()
modulo_HelpfulVote = data['helpful_vote'].std()
print("Modulo Rating : ", math.floor(modulo_Rating))
print("Modulo Ulasan Bermanfaat : ", math.floor(modulo_HelpfulVote))

#Varian Rating---------------------------------------------------------------------------------------
varian_Rating = data['rating'].var()
varian_HelpfulVote = data['helpful_vote'].var()
print("Varian Rating : ", math.floor(varian_Rating))
print("Varian Ulasan Bermanfaat : ", math.floor(varian_HelpfulVote))

#Minimum Rating---------------------------------------------------------------------------------------
minimum_Rating = data['rating'].min()
minimum_HelpfulVote = data['helpful_vote'].min()
print("Minimum Rating : ", math.floor(minimum_Rating))
print("Minimum Ulasan Bermanfaat : ", math.floor(minimum_HelpfulVote))

#Maksimal Rating---------------------------------------------------------------------------------------
maximum_Rating = data['rating'].max()
maximum_HelpfulVote = data['helpful_vote'].max()
print("Maximum Rating : ", math.floor(maximum_Rating))
print("Maximum Ulasan Bermanfaat : ", math.floor(maximum_HelpfulVote))


#Analisis Sentimen Pengguna Menggunaakn TextBlob, Analisa Topik yang Sering Dibicarakan Menggunakan LDA------------------------------------------------------------
#Polaritas Title dan Text review(Positif,Negatif,Netral)
polarity_title_temp = {
    'Positif' : [],
    'Negatif'  : [],
    'Netral'   : []
}
polarity_text_temp = {
    'Positif': [],
    'Negatif': [],
    'Netral': []
}

subjectivity_title_temp = {
    'Objektif' : [],
    'Subjektif' : []
}
subjectivity_text_temp = {
    'Objektif' : [],
    'Subjektif' : []
}

for title,text in zip(data['title'].astype(str),data['text'].astype(str)):
    blobtitle = TextBlob(title)
    blobtext = TextBlob(text)
    sentimenttitle = blobtitle.sentiment.polarity
    sentimenttext = blobtext.sentiment.polarity
    subjectivtytitle = blobtitle.subjectivity
    subjectivtytext = blobtext.subjectivity
    if sentimenttitle < 0 :
        polarity_title_temp['Negatif'].append(sentimenttitle)
    elif sentimenttitle > 0:
        polarity_title_temp['Positif'].append(sentimenttitle)
    else :
        polarity_title_temp['Netral'].append(sentimenttitle)

    if sentimenttext < 0 :
        polarity_text_temp['Negatif'].append(sentimenttext)
    elif sentimenttext > 0:
        polarity_text_temp['Positif'].append(sentimenttext)
    else:
        polarity_text_temp['Netral'].append(sentimenttitle)

    if subjectivtytitle == 0 :
        subjectivity_title_temp['Objektif'].append(subjectivtytitle)
    else:
        subjectivity_title_temp['Subjektif'].append(subjectivtytitle)

    if subjectivtytext == 0 :
        subjectivity_text_temp['Objektif'].append(subjectivtytext)
    else:
        subjectivity_text_temp['Subjektif'].append(subjectivtytext)

print("\n")
print("Polaritas untuk Title")
print('Polaritas Title Positif : ',len(polarity_title_temp['Positif']))
print('Polaritas Title Negatif : ',len(polarity_title_temp['Negatif']))
print('Polaritas Title Netral  : ',len(polarity_title_temp['Netral']))
print('Objektifitas Title :', len(subjectivity_title_temp['Objektif']))
print('Subjektifitas Title :', len(subjectivity_title_temp['Subjektif']))

print("\n")
print("Polaritas untuk Text")
print('Polaritas Text Positif : ',len(polarity_text_temp['Positif']))
print('Polaritas Text Negatif : ',len(polarity_text_temp['Negatif']))
print('Polaritas Text Netral  : ',len(polarity_text_temp['Netral']))
print('Objektifitas Text :', len(subjectivity_text_temp['Objektif']))
print('Subjektifitas Text :', len(subjectivity_text_temp['Subjektif']))

#Prediksi Rating berdasarkan Timestamp menggunakan LSTM-------------------------------------------
df = pd.DataFrame({'timestamp': data['new_timestamp'], 'rating': data['rating']})
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values(by='timestamp')
df.set_index('timestamp', inplace=True)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['rating'].values.reshape(-1, 1))

def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

time_step = 10
X, y = create_dataset(scaled_data, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(time_step, 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping], verbose=1)

predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)
y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))
mse = mean_squared_error(y_test_scaled, predictions)
print(f'Mean Squared Error: {mse}')

plt.figure(figsize=(12, 6))
plt.plot(df.index[-len(y_test_scaled):], y_test_scaled, label='Actual Ratings')
plt.plot(df.index[-len(predictions):], predictions, label='Predicted Ratings', linestyle='--')
plt.title('Ratings Prediction with LSTM')
plt.xlabel('Timestamp')
plt.ylabel('Rating')
plt.legend()
plt.grid(True)
plt.show()



