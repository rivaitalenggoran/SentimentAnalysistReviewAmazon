import pandas as pd
import regex as re


#persiapkan data
input_file = 'Dataset//Electronics.jsonl'
output_file = 'Dataset//Electronics_sampled.csv'
num_objects = 10000



# Membaca file JSONL dan mengambil 10000 objek pertama
data = pd.read_json(input_file, lines=True, nrows=num_objects)



#LowerCase title, Menghapus karakter tidak penting
title_data = data['title']
new_title_data = []
for title in title_data:
    lower_title = title.lower()
    new_title = re.sub(r"[..!|?|&|,|-|/|\|:|’|'|(|)|%|#|$|..]", '', lower_title)
    new_title_data.append(new_title)



#regex untuk hapus <br /> pada review, LowerCase, Menghapus karakter tidak penting
text_data = data['text']
new_text_data = []
for text in text_data:
    new_text = re.sub(r"<br\s*/?>", '', text)
    lower_text = new_text.lower()
    new_text = re.sub(r"[..!|?|&|,|-|/|\|:|’|'|(|)|%|#|$|..]", '', lower_text)
    new_text_data.append(new_text)


new_title_df = pd.Series(new_title_data)
data['title'] = new_title_df
new_text_df = pd.Series(new_text_data)
data['text'] = new_text_df


concat_df = pd.concat([data['rating'],data['title'],data['text'],data['images'],data['asin'],data['parent_asin'],data['user_id'],data['timestamp'],data['helpful_vote'],data['verified_purchase']],axis=1)
new_df = pd.DataFrame(concat_df)
# Menyimpan data dalam format CSV
new_df.to_csv(output_file, index=False, encoding='utf-8')