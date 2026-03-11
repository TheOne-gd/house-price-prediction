arr = [60,'RL',65,8450,'Pave','NA','Reg','Lvl','AllPub','Inside','Gtl','CollgCr','Norm','Norm','1Fam','2Story',7,5,2003,2003,'Gable','CompShg','VinylSd','VinylSd','BrkFace',196,'Gd','TA','PConc','Gd','TA','No','GLQ',706,'Unf',0,150,856,'GasA','Ex','Y','SBrkr',856,854,0,1710,1,0,2,1,3,1,'Gd',8,'Typ',0,'NA','Attchd',2003,'RFn',2,548,'TA','TA','Y',0,61,0,0,0,0,'NA','NA','NA',0,2,2008,'WD','Normal']

import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
url = "D:\\House Price Prediction\\house price prediction\\traindataset.csv"
dataframe = pandas.read_csv(url)

array = dataframe.values
print(array[0])
X = array[:, 0:80]
Y = array[:, 80]
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(
    X, Y, test_size=0.25, random_state=0)
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
xtrain = sc_x.fit_transform(xtrain)
xtest = sc_x.transform(xtest)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(xtrain, ytrain)
y_pred = classifier.predict(arr)

print(y_pred,"hiiiiiiiiiiiiiiiiiiiiiii")




