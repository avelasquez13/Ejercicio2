import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn import linear_model
import scipy

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Credit.csv', index_col=0)

X=data[['Income', 'Limit', 'Rating', 'Cards', 'Age', 'Education', 'Gender']]
Y=data['Balance']

X_N=X['Income']
X_G=X['Gender'].values
trainG=[]

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

var_female = np.var(female_incomes)
var_male = np.var(male_incomes)

mean_female = np.mean(female_incomes)
mean_male = np.mean(male_incomes)


print "p-value de que las varianzas son iguales:", scipy.stats.levene(female_incomes, male_incomes)[1]
print "Como p-value >> 0.05, no rechazamos la hipotesis de que las varianzas son iguales y podemos usar un ttest para evaluar diferencia de medias"
print "p-value de que las medias son iguales (asumiendo varianzas iguales):", scipy.stats.ttest_ind(female_incomes, male_incomes)[1]
print "como p-value >> 0.05, no rechazamos la hipotesis de que los promedios son iguales, entonces no hay diferencia en income entre hombres y mujeres"

