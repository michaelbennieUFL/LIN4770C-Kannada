import pandas
import os

import allosaurus.app

def process_dir(dir, output_dir, total):
    i = 0
    for filename in os.listdir(dir):
        i += 1
        print("Processing", i, "of", total)
        if filename == 'LICENSE' or filename == 'line_index.tsv': continue
        filepath = dir + '/' + filename
        filepath_csv = output_dir + '/' + filename[:-3] + 'csv'
        output = parse.recognize(filepath, "kan", timestamp=True)
        lines = output.split('\n')
        arr = []
        for line in lines:
            line_split = line.split(' ')
            start_time = float(line_split[0])
            end_time = start_time + float(line_split[1])
            phone = line_split[2]
            arr.append(dict(start=start_time, end=end_time, phoneme=phone))
        df = pandas.DataFrame.from_records(arr)
        df.to_csv(filepath_csv)


parse = allosaurus.app.read_recognizer()
os.makedirs('tokens/female', exist_ok=True)
os.makedirs('tokens/male', exist_ok=True)  
i = 0
count_female = len(os.listdir('data/kn_in_female')) - 2
count_male = len(os.listdir('data/kn_in_male')) - 2

process_dir('data/kn_in_male', 'tokens/male', count_male)
process_dir('data/kn_in_female', 'tokens/female', count_female)
