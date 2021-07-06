import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
dataset = pd.read_csv("winequality-red.csv")
bins = (2, 6.5, 8)
group_names = ['bad', 'good']
dataset['quality'] = pd.cut(dataset['quality'], bins = bins, labels = group_names)
label_quality = LabelEncoder()
dataset['quality'] = label_quality.fit_transform(dataset['quality'])
X = dataset.drop('quality', axis = 1)
y = dataset['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
rfc = RandomForestClassifier(n_estimators=200)
rfc = rfc.fit(X_train, y_train)
pred_rfc = rfc.predict(X_test)
accuracy =rfc.score(X_test,y_test)
print('Accuracy of the model is',accuracy*100,'%')
pickle.dump(rfc, open('rfc_model.pkl','wb'))