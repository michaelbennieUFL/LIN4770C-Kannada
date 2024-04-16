from sklearn.tree import DecisionTreeClassifier
import pandas
from sklearn.model_selection import cross_validate
from sklearn.dummy import DummyClassifier
from sklearn import metrics

df = pandas.read_csv('trimDataset.csv')

df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Unnamed: 0.1', axis=1, inplace=True)
df.drop('utterance', axis=1, inplace=True)
df.dropna(inplace=True)

random_classifier = DummyClassifier(strategy = 'uniform', random_state = 727)  

df_features = df[['a', 'e', 'i', 'o', 'u']]
#df_features = df.drop(['a', 'e', 'i', 'o', 'u', 'class'], axis=1)
#df_features = df.drop('class', axis=1)
print(df_features)
DT_classifier = DecisionTreeClassifier(random_state=727)
#scores_SVM = cross_validate(DT_classifier, df_features, df['class'], cv=10, scoring=["precision", "recall", "f1"])
scores_Rand = cross_validate(random_classifier, df_features, df['class'], cv=10, scoring=["precision", "recall", "f1"])

precision = sum(scores_Rand['test_precision'])/len(scores_Rand['test_precision'])
recall = sum(scores_Rand['test_recall'])/len(scores_Rand['test_recall'])
f1 = sum(scores_Rand['test_f1'])/len(scores_Rand['test_f1'])

print(precision, recall, f1)
