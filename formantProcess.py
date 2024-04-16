import parselmouth
import pandas
import tqdm
import os

def process_f1(dir, csv_dir):
    total = len(os.listdir(dir)) - 2
    i = 0
    for filename in os.listdir(dir):
        i += 1
        print("Processing", i, "of", total)
        if filename == 'LICENSE' or filename == 'line_index.tsv': continue
        filepath = dir + '/' + filename
        filepath_csv = csv_dir + '/' + filename[:-3] + 'csv'
        sound = parselmouth.Sound(filepath)
        df = pandas.read_csv(filepath_csv)
        formants = sound.to_formant_burg()
        sample_count = int(round(0.045/formants.time_step, 0))
        step = formants.time_step
        f1_list = []
        for time in df['start']:
            formant_sum = 0
            for i in range(sample_count):
                formant_sum += formants.get_value_at_time(1, time + i * step)
            f1 = formant_sum/sample_count
            f1_list.append(f1)
        df = df.assign(f1=f1_list)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df.to_csv(filepath_csv)

process_f1('data/kn_in_male', 'tokens/male')
process_f1('data/kn_in_female', 'tokens/female')
    