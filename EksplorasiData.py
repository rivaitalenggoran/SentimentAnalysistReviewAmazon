import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
file = "Dataset//Electronics_sampled.csv"

data = pd.read_csv(file)



#Distribusi Rating-----------------------------------------------------------
rating_counts = data['rating'].value_counts().sort_index()
print(rating_counts)

# Membuat grafik distribusi rating
plt.figure(figsize=(10, 6))
rating_counts.plot(kind='bar', color='skyblue')
plt.title('Distribusi Rating')
plt.xlabel('Rating')
plt.ylabel('Jumlah Ulasan')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



#Rata-Rata Rating-----------------------------------------------------------
# Menghitung rata-rata rating
average_rating = data['rating'].mean()

# Menampilkan rata-rata rating
print(f'Rata-rata Rating: {average_rating:.2f}')



#Tampilkan Rating Berdasarkan Waktu------------------------------------------
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Mengatur timestamp sebagai indeks
data.set_index('timestamp', inplace=True)

# Mengelompokkan data berdasarkan bulan dan tahun, kemudian menghitung rata-rata rating per bulan
monthly_ratings = data['rating'].resample('M').mean()

# Membuat grafik waktu seri
plt.figure(figsize=(12, 6))
plt.plot(monthly_ratings, marker='o', linestyle='-', color='b')

# Menambahkan label dan judul
plt.title('Rata-rata Rating Berdasarkan Waktu')
plt.xlabel('Waktu')
plt.ylabel('Rata-rata Rating')
plt.grid(True)

# Menampilkan grafik
plt.show()



#Analisa Judul Review Yang Sering Muncul------------------------------------------
text = ' '.join(data['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud dari Judul Ulasan')
plt.show()



#Analisa Isi Review Yang Sering Muncul------------------------------------------
text = ' '.join(data['text'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud dari Teks Ulasan')
plt.show()

