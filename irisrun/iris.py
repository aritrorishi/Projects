import pandas as pd
import numpy as np
from sklearn.svm import SVC
import pickle

df = pd.read_csv('iris_flower_dataset.csv')
x = np.array(df.drop(columns=['Id','Species']))
y = np.array(df['Species'].replace(['Iris-setosa','Iris-versicolor','Iris-virginica'],[0,1,2]).values)

model = SVC(kernel='rbf', C=100, gamma='scale')
model.fit(x,y)

pickle.dump(model, open('iris.pkl','wb'))