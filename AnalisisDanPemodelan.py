import pandas as pd
import math
from textblob import TextBlob

filepath = 'Dataset//Electronics_sampled.csv'
data = pd.read_csv(filepath)

#Analisis Menggunakan Statistika Deskriptif--------------------------------------------------------

#Rata-Rata-----------------------------------------------------------------------------------------
mean_Rating = data['rating'].mean()
print("Rata-Rata Rating : ", math.floor(mean_Rating))

#Median Rating---------------------------------------------------------------------------------------
median_Rating = data['rating'].median()
print("Median Rating : ", math.floor(median_Rating))


#Modulo Rating---------------------------------------------------------------------------------------
modulo_Rating = data['rating'].std()
print("Modulo Rating : ", math.floor(modulo_Rating))

#Varian Rating---------------------------------------------------------------------------------------
varian_Rating = data['rating'].var()
print("Varian Rating : ", math.floor(varian_Rating))

#Minimum Rating---------------------------------------------------------------------------------------
minimum_Rating = data['rating'].min()
print("Minimum Rating : ", math.floor(minimum_Rating))

#Maksimal Rating---------------------------------------------------------------------------------------
maximum_Rating = data['rating'].max()
print("Maximum Rating : ", math.floor(maximum_Rating))


#Analisis Sentimen Pengguna Melalui Review------------------------------------------------------------
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

for title,text in zip(data['title'].astype(str),data['text'].astype(str)):
    blobtitle = TextBlob(title)
    blobtext = TextBlob(text)
    sentimenttitle = blobtitle.sentiment.polarity
    sentimenttext = blobtext.sentiment.polarity
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

print("\n")
print("Polaritas untuk Title")
print('Polaritas Title Positif : ',len(polarity_title_temp['Positif']))
print('Polaritas Title Negatif : ',len(polarity_title_temp['Negatif']))
print('Polaritas Title Netral  : ',len(polarity_title_temp['Netral']))

print("\n")
print("Polaritas untuk Text")
print('Polaritas Text Positif : ',len(polarity_text_temp['Positif']))
print('Polaritas Text Negatif : ',len(polarity_text_temp['Negatif']))
print('Polaritas Text Netral  : ',len(polarity_text_temp['Netral']))





