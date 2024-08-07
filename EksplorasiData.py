import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


file = "Dataset//Electronics_sampled.csv"
data = pd.read_csv(file)


#Distribusi Rating-----------------------------------------------------------
rating_counts = data['rating'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
rating_counts.plot(kind='bar', color='skyblue')
plt.title('Distribusi Rating')
plt.xlabel('Rating')
plt.ylabel('Jumlah Ulasan')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



#Rata-Rata Rating-----------------------------------------------------------
average_rating = data['rating'].mean()
print(f'Rata-rata Rating: {average_rating:.2f}')



#Tampilkan Rating Berdasarkan Waktu------------------------------------------
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Mengatur timestamp sebagai indeks
data.set_index('timestamp', inplace=True)

# Mengelompokkan data berdasarkan bulan dan tahun, kemudian menghitung rata-rata rating per bulan
monthly_ratings = data['rating'].resample('ME').mean()
plt.figure(figsize=(12, 6))
plt.plot(monthly_ratings, marker='o', linestyle='-', color='b')
plt.title('Rata-rata Rating Berdasarkan Waktu')
plt.xlabel('Waktu')
plt.ylabel('Rata-rata Rating')
plt.grid(True)
plt.show()


#Analisa Teks Judul Review Yang Sering Muncul------------------------------------------
text = ' '.join(data['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Teks Dari Judul Review Yang Sering Muncul')
plt.show()



#Analisa Teks Di Review Yang Sering Muncul------------------------------------------
text = ' '.join(data['text'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Teks Review Yang Sering Muncul')
plt.show()



#Jumlah Gambar Per Ulasan---------------------------------------------------------
data['num_images'] = data['images'].apply(lambda x: len(eval(x)) if pd.notna(x) else 0)
plt.figure(figsize=(10, 6))
data['num_images'].hist(bins=range(0, data['num_images'].max() + 1), color='lightgreen')
plt.title('Distribusi Jumlah Gambar per Ulasan')
plt.xlabel('Jumlah Gambar')
plt.ylabel('Jumlah Ulasan')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



#Frekuensi Review Yang Bermanfaat----------------------------------------------
plt.figure(figsize=(10, 6))
data['helpful_vote'].hist(bins=range(0, data['helpful_vote'].max() + 1), color='purple')
plt.title('Distribusi Jumlah Vote Berguna per Ulasan')
plt.xlabel('Jumlah Vote Berguna')
plt.ylabel('Jumlah Ulasan')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



#Distribusi Pembelian Yang Terverifikasi-------------------------------------
plt.figure(figsize=(6, 6))
data['verified_purchase'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Distribusi Ulasan Pembelian Terverifikasi')
plt.ylabel('')
plt.show()
