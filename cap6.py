import numpy as np
import pandas as pd
pd.Series(2)
pd.Series([2]*5)
x=pd.Series(list('hello'))
pd.Series({1:'India',2:'Japan',3:'Singapore'})
pd.Series(np.arange(1,5))
pd.Series(np.random.normal(size=4000))
x=pd.Series(np.random.normal(size=4), index=['a','b','c','d'])
# numero di elementi della Series
x.size
len(x)
# numero di righe e colonne
x.shape
# lista dei valori all'interno della Series
x.values
# lista degli indici della Series
x.index
x
x.value_counts(ascending=True).head(2)
z=pd.Series(['a','b','a','c','d','b'])
x.value_counts().head(2).values
# DataFrame
student_age=pd.Series([22,24,20])
teacher_age=pd.Series([40,50,55])
combined_age=pd.DataFrame([student_age, teacher_age])
combined_age.columns=['Class 1','Class 2','Class 3']
combined_age.index=['Studenti','Insegnanti']
combined_age
# creazione da un Dictionary
v=pd.DataFrame({'Class 1':[22,40],'Class 2':[24,50],'Class 3':[20,45]})
n=pd.DataFrame(np.arange(1,9).reshape(2,4))
pd.DataFrame([(22,24,20),(40,50,455)],columns=['Class 1','Class 2','Class 3'])

titanic=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
titanic.head()
c19=pd.read_json('/home/giuseppe/Documents/java/workspace/git/COVID-19/dati-json/dpc-covid19-ita-andamento-nazionale.json')
c19
import html5lib
import numpy as np
import pandas as pd
#ps=pd.read_html(r"https://www.google.com/maps/place/Pizzeria+'O+Sarracin/@40.7448628,14.6364161,15z/data=!4m5!3m4!1s0x0:0x6c6d41bc8c8ba1c3!8m2!3d40.7448628!4d14.6364161")
url="https://www.w3schools.com/sql/sql_create_table.asp"
ps=pd.read_html(url)
ps[0]