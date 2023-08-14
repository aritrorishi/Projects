import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv('spam.csv')
data = df.where((pd.notnull(df)),'')
data = data.replace(['spam','ham'],[1,0])
x = data.Message
y = data.Category
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.4, random_state=42 )
ytrain = ytrain.astype('int64')
ytest = ytest.astype('int64')
tclf = Pipeline([('tfidf', TfidfVectorizer()),('clf', SVC())])
tclf.fit(xtrain,ytrain)

pickle.dump(tclf, open('spamrun.pkl','wb'))
