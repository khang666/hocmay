import numpy as np 
import matplotlib.pyplot as mtp
import pandas as pd

data_set = pd.read_csv('D:/hoc may/lab2/User_Data.csv')
print(data_set.head())

x=data_set.iloc[:,[2,3]].values
y= data_set.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0)
print(x_train.shape)
print(y_train.shape)

from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5 , metric='minkowski', p=2)
classifier.fit(x_train , y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
print(cm)

from matplotlib.colors import ListedColormap 
x_set , y_set = x_train, y_train
x1 , x2 = np.meshgrid(np.arange(start= x_set[:,0].min()-1,stop= x_set[:,0].max()+1,step = 0.01),
                      np.arange(start= x_set[:,1].min()-1,stop= x_set[:,1].max()+1,step = 0.01))
mtp.contour(x1, x2,classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),alpha = 0.75, cmap = ListedColormap(['red','green']))
mtp.xlim(x1.min(), x1.max())
mtp.xlim(x2.min(), x2.max())
for i,j in enumerate(np.unique(y_set)):
    mtp.scatter(x_set[y_set == j,0], x_set[y_set == j, 1],
                c = ListedColormap(['red' , 'green'])(i), label= j)
mtp.title('K-NN Algorithm (Training set)')
mtp.xlabel('Age')
mtp.ylabel('Estimated Salary')
mtp.legend()
mtp.show()