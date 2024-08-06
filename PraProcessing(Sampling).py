import pandas as pd

input_file = 'Dataset//Electronics.jsonl'
output_file = 'Dataset//Electronics_sampled.csv'
num_objects = 10000


# Membaca file JSONL dan mengambil 1000 objek pertama
data = pd.read_json(input_file, lines=True, nrows=num_objects)

# Menyimpan data dalam format CSV
data.to_csv(output_file, index=False, encoding='utf-8')