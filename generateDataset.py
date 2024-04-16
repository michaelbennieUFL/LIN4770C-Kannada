import pandas
import os

def processTokens(dir, df, classID):
    i = 0
    total = len(os.listdir(dir))
    for filename in os.listdir(dir):
        i += 1
        if(i % 100 == 0): print("Processing", i, 'of', total)
        utterance_name = filename[:-4]
        df_utterance = pandas.read_csv(dir + '/' + filename)
        f1_dict = {}
        for index, row in df_utterance.iterrows():
            if row["phoneme"] in f1_dict: f1_dict[row['phoneme']].append(row["f1"])
            else: f1_dict[row['phoneme']] = [row["f1"]]

        for phoneme in phonemes:
            if phoneme in f1_dict: f1_dict[phoneme] = sum(f1_dict[phoneme])/len(f1_dict[phoneme])
            else: f1_dict[phoneme] = 0.0

        f1_list = [utterance_name]
        f1_dict = dict(sorted(f1_dict.items()))

        for phoneme in f1_dict:
            f1_list.append(f1_dict[phoneme])

        f1_list.append(classID)

        df = pandas.concat([df, pandas.DataFrame([f1_list], columns=cols)], ignore_index=True)

    return df
    

cols = ['utterance', 'a', 'aː', 'b', 'bʰ', 'b̤', 'c', 'cʰ', 'd̪', 'd̪ʰ', 'd̪̤', 'e', 'eː', 'f', 'h', 'i', 'iː', 'j', 'k', 'kʰ', 'l', 'l̪', 'm', 'n', 'n̪', 'o', 'oː', 'p', 'pʰ', 'r̪', 's',
 's̪', 't̪', 't̪ʰ', 'u', 'uː', 'v', 'w', 'z̪', 'æ', 'ŋ', 'ɖ', 'ɖʰ', 'ɖ̤', 'ɟ', 'ɟʰ', 'ɟ̤', 'ɡ', 'ɡʰ', 'ɭ', 'ɳ', 'ɾ', 'ʂ', 'ʃ', 'ʈ', 'ʈʰ', 'ʝ', 'class']
phonemes = cols[1:-1]
df_final = pandas.DataFrame(columns=cols)

df_final = processTokens('tokens/female', df_final, 1)
df_final = processTokens('tokens/male', df_final, 0)
df_final.to_csv('dataset.csv')