from sklearn.tree import DecisionTreeClassifier
import pandas
from sklearn.model_selection import cross_validate

df = pandas.read_csv('trimDataset.csv')

df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('utterance', axis=1, inplace=True)
df.dropna(inplace=True)

#df_features = df[['a', 'e', 'i', 'o', 'u']]
df_features = df.drop('class', axis=1)
print(df_features)
#print(df_features)
DT_classifier = DecisionTreeClassifier(random_state=727)
scores_SVM = cross_validate(DT_classifier, df_features, df['class'], cv=10, scoring=["precision", "recall", "f1"])
print(scores_SVM)
