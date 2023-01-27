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

combined_age=pd.DataFrame({'class 1':[22,40],'class 2':[24,50],'class 3':[20,45]})
combined_age.index
combined_age.columns
combined_age.values
combined_age.rename(columns={'class 1':'batch 1','class 2':'batch 2','class 3':'batch 3'},inplace=True)
combined_age
combined_age['class 4']=([18,40])
combined_age.insert(2,'class 0',[18,35])
combined_age=pd.DataFrame({'class 1':[22,40],'class 2':[24,50],'class 3':[20,45]})
combined_age
combined_age.loc[:,'class 4']=[20,40]
combined_age=pd.DataFrame({'class 1':[32,22], 'class 2':[37,44], 'class 3':[41,33]})
combined_age.append({'class 1':40,'class 2':50,'class 3':45}, ignore_index=True)
combined_age.insert({'class 0',[18,35]})
combined_age.index # AttributeError: 'dict' object has no attribute 'index'
combined_age.columns=['batch 1', 'batch 2', 'batch 3']
combined_age.rename(columns={'class 1':'batch 1','class 2':'batch 2','class 3':'batch 3'},inplace=True)

import html5lib
import numpy as np
import pandas as pd
now_row=pd.DataFrame({'class 1':[32,22], 'class 2':[37,44], 'class 3':[41,33]})
now_row
pd.concat([combined_age,now_row])
del combined_age['class 3']
del now_row['class 3']
now_row

import html5lib
import numpy as np
import pandas as pd
now_row=pd.DataFrame({'class 1':[32,22], 'class 2':[37,44], 'class 3':[41,33]})
now_row

now_row.drop(1)

periodic_table=pd.DataFrame({'Element':['Hydrogen','Helium','Lithium','Beryllium','Boron']},index=['H','He','Li','Be','B'])