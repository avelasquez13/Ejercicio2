import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn import linear_model

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Credit.csv', index_col=0)

X=data[['Income', 'Limit', 'Rating', 'Cards', 'Age', 'Education', 'Gender']]
Y=data['Balance']

X_N=X['Income']
X_G=X['Gender'].values
trainG=[]

#linreg=linear_model.LinearRegression()
#linreg.fit(X_N,Y)
#print(linreg.coef_)

for i in range(len(X_G)):
    if X_G[i]==' Male':
        trainG.append(0)
    else:
        trainG.append(1)

income = np.asarray(X_N.values)
gender = np.asarray(trainG)

male_incomes = []
female_incomes = []
for i in range(len(income)):
    if gender[i] == 0:
        male_incomes.append(income[i])
    if gender[i] == 1:
        female_incomes.append(income[i])





