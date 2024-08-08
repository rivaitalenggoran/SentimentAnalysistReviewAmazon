import pandas as pd
import regex as re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

#persiapkan data
input_file = 'Dataset//Electronics.jsonl'
output_file = 'Dataset//Electronics_sampled.csv'
num_objects = 10000



# Membaca file JSONL
data = pd.read_json(input_file, lines=True, nrows=num_objects)

#Set StopWord dari NLTK
stop_words = set(stopwords.words('english'))

# Inisialisasi WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


'''
Praprocessing :
- Hapus HTML parsing (<br /> untuk text review)
- LowerCase title
- Hapus Angka
- Menghapus karakter tidak penting
- Tokenisasi
- Hapus StopWord
'''

title_data = data['title']
new_title_data = []
for title in title_data:
    #lower title
    lower_title = title.lower()
    #hapus angka
    number_title = re.sub(r'\d+', '', lower_title)
    #hapus karakter
    character_title = number_title.translate(str.maketrans('', '', string.punctuation))
    #tokenisasi
    token_title = character_title.split()
    #hapus Stopword
    stopword_title = [word for word in token_title if word not in stop_words]
    #lemmatisasi
    lematisasi_title = [lemmatizer.lemmatize(stopwords) for stopwords in stopword_title]
    new_title_data.append(lematisasi_title)



#regex untuk hapus <br /> pada review, lowerCase, menghapus karakter tidak penting
text_data = data['text']
new_text_data = []
for text in text_data:
    #hapus tag HTML menggunakan HTML parsing
    soup = BeautifulSoup(text, 'html.parser')
    newtext = soup.get_text()
    #lower title
    lower_title = newtext.lower()
    #hapus angka
    number_text = re.sub(r'\d+', '', lower_title)
    #hapus karakter
    character_text = number_text.translate(str.maketrans('', '', string.punctuation))
    #tokenisasi
    token_text = character_text.split()
    #hapus Stopword
    stopword_text = [word for word in token_text if word not in stop_words]
    #lemmatisasi
    lematisasi_text = [lemmatizer.lemmatize(stopwords) for stopwords in stopword_text]
    new_text_data.append(lematisasi_text)



new_title_df = pd.Series(new_title_data)
data['title'] = new_title_df
new_text_df = pd.Series(new_text_data)
data['text'] = new_text_df


concat_df = pd.concat([data['rating'],data['title'],data['text'],data['images'],data['asin'],data['parent_asin'],data['user_id'],data['timestamp'],data['helpful_vote'],data['verified_purchase']],axis=1)
new_df = pd.DataFrame(concat_df)
# menyimpan data dalam format CSV
new_df.to_csv(output_file, index=False, encoding='utf-8')
