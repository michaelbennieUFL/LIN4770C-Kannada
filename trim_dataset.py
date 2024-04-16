import pandas

df = pandas.read_csv('dataset.csv')

cols = ['utterance', 'a', 'aː', 'b', 'bʰ', 'b̤', 'c', 'cʰ', 'd̪', 'd̪ʰ', 'd̪̤', 'e', 'eː', 'f', 'h', 'i', 'iː', 'j', 'k', 'kʰ', 'l', 'l̪', 'm', 'n', 'n̪', 'o', 'oː', 'p', 'pʰ', 'r̪', 's',
 's̪', 't̪', 't̪ʰ', 'u', 'uː', 'v', 'w', 'z̪', 'æ', 'ŋ', 'ɖ', 'ɖʰ', 'ɖ̤', 'ɟ', 'ɟʰ', 'ɟ̤', 'ɡ', 'ɡʰ', 'ɭ', 'ɳ', 'ɾ', 'ʂ', 'ʃ', 'ʈ', 'ʈʰ', 'ʝ', 'class']
phonemes = cols[1:-1]

phoneme_dict = {}

for phoneme in phonemes:
    phoneme_dict[phoneme] = 0
    f1_list = df[phoneme].tolist()
    for f1 in f1_list:
        if f1 != 0.0: phoneme_dict[phoneme] += 1
print(phoneme_dict)