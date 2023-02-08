
Code
import pandas as pd
df=pd.read_csv(r'C:\Users\HP\Downloads\churn_Modelling.csv')
df
RowNumber	CustomerId	Surname	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited
0	1	15634602	Hargrave	619	France	Female	42	2	0.00	1	1	1	101348.88	1
1	2	15647311	Hill	608	Spain	Female	41	1	83807.86	1	0	1	112542.58	0
2	3	15619304	Onio	502	France	Female	42	8	159660.80	3	1	0	113931.57	1
3	4	15701354	Boni	699	France	Female	39	1	0.00	2	0	0	93826.63	0
4	5	15737888	Mitchell	850	Spain	Female	43	2	125510.82	1	1	1	79084.10	0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
9995	9996	15606229	Obijiaku	771	France	Male	39	5	0.00	2	1	0	96270.64	0
9996	9997	15569892	Johnstone	516	France	Male	35	10	57369.61	1	1	1	101699.77	0
9997	9998	15584532	Liu	709	France	Female	36	7	0.00	1	0	1	42085.58	1
9998	9999	15682355	Sabbatini	772	Germany	Male	42	3	75075.31	2	1	0	92888.52	1
9999	10000	15628319	Walker	792	France	Female	28	4	130142.79	1	1	0	38190.78	0
10000 rows × 14 columns

df=df.drop(columns='Surname')
df
RowNumber	CustomerId	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited
0	1	15634602	619	France	Female	42	2	0.00	1	1	1	101348.88	1
1	2	15647311	608	Spain	Female	41	1	83807.86	1	0	1	112542.58	0
2	3	15619304	502	France	Female	42	8	159660.80	3	1	0	113931.57	1
3	4	15701354	699	France	Female	39	1	0.00	2	0	0	93826.63	0
4	5	15737888	850	Spain	Female	43	2	125510.82	1	1	1	79084.10	0
...	...	...	...	...	...	...	...	...	...	...	...	...	...
9995	9996	15606229	771	France	Male	39	5	0.00	2	1	0	96270.64	0
9996	9997	15569892	516	France	Male	35	10	57369.61	1	1	1	101699.77	0
9997	9998	15584532	709	France	Female	36	7	0.00	1	0	1	42085.58	1
9998	9999	15682355	772	Germany	Male	42	3	75075.31	2	1	0	92888.52	1
9999	10000	15628319	792	France	Female	28	4	130142.79	1	1	0	38190.78	0
10000 rows × 13 columns

df['Geography'] =df['Geography'].astype('category')
df['Geography'] =df['Geography'].cat.codes
df
RowNumber	CustomerId	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited
0	1	15634602	619	0	Female	42	2	0.00	1	1	1	101348.88	1
1	2	15647311	608	2	Female	41	1	83807.86	1	0	1	112542.58	0
2	3	15619304	502	0	Female	42	8	159660.80	3	1	0	113931.57	1
3	4	15701354	699	0	Female	39	1	0.00	2	0	0	93826.63	0
4	5	15737888	850	2	Female	43	2	125510.82	1	1	1	79084.10	0
...	...	...	...	...	...	...	...	...	...	...	...	...	...
9995	9996	15606229	771	0	Male	39	5	0.00	2	1	0	96270.64	0
9996	9997	15569892	516	0	Male	35	10	57369.61	1	1	1	101699.77	0
9997	9998	15584532	709	0	Female	36	7	0.00	1	0	1	42085.58	1
9998	9999	15682355	772	1	Male	42	3	75075.31	2	1	0	92888.52	1
9999	10000	15628319	792	0	Female	28	4	130142.79	1	1	0	38190.78	0
10000 rows × 13 columns

df['Gender'] =df['Gender'].astype('category')
df['Gender'] =df['Gender'].cat.codes
df
RowNumber	CustomerId	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited
0	1	15634602	619	0	0	42	2	0.00	1	1	1	101348.88	1
1	2	15647311	608	2	0	41	1	83807.86	1	0	1	112542.58	0
2	3	15619304	502	0	0	42	8	159660.80	3	1	0	113931.57	1
3	4	15701354	699	0	0	39	1	0.00	2	0	0	93826.63	0
4	5	15737888	850	2	0	43	2	125510.82	1	1	1	79084.10	0
...	...	...	...	...	...	...	...	...	...	...	...	...	...
9995	9996	15606229	771	0	1	39	5	0.00	2	1	0	96270.64	0
9996	9997	15569892	516	0	1	35	10	57369.61	1	1	1	101699.77	0
9997	9998	15584532	709	0	0	36	7	0.00	1	0	1	42085.58	1
9998	9999	15682355	772	1	1	42	3	75075.31	2	1	0	92888.52	1
9999	10000	15628319	792	0	0	28	4	130142.79	1	1	0	38190.78	0
10000 rows × 13 columns

df.isnull().sum()
RowNumber          0
CustomerId         0
CreditScore        0
Geography          0
Gender             0
Age                0
Tenure             0
Balance            0
NumOfProducts      0
HasCrCard          0
IsActiveMember     0
EstimatedSalary    0
Exited             0
dtype: int64
x=df.drop(columns = 'Exited')
x
RowNumber	CustomerId	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary
0	1	15634602	619	0	0	42	2	0.00	1	1	1	101348.88
1	2	15647311	608	2	0	41	1	83807.86	1	0	1	112542.58
2	3	15619304	502	0	0	42	8	159660.80	3	1	0	113931.57
3	4	15701354	699	0	0	39	1	0.00	2	0	0	93826.63
4	5	15737888	850	2	0	43	2	125510.82	1	1	1	79084.10
...	...	...	...	...	...	...	...	...	...	...	...	...
9995	9996	15606229	771	0	1	39	5	0.00	2	1	0	96270.64
9996	9997	15569892	516	0	1	35	10	57369.61	1	1	1	101699.77
9997	9998	15584532	709	0	0	36	7	0.00	1	0	1	42085.58
9998	9999	15682355	772	1	1	42	3	75075.31	2	1	0	92888.52
9999	10000	15628319	792	0	0	28	4	130142.79	1	1	0	38190.78
10000 rows × 12 columns

y=df['Exited']
from sklearn.model_selection import train_test_split
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[2], line 1
----> 1 from sklearn.model_selection import train_test_split

ModuleNotFoundError: No module named 'sklearn'

x_train, x_test, y_train, y_test =train_test_split(x,y, test_size=0.4, random_state=22)
x_train
  Cell In[4], line 1
    x_train, x_test, y_train, y_test =(x,y, test_size=0.4, random_state=22)
                                                     ^
SyntaxError: invalid syntax


from sklearn.preprocessing import standardScaler
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[5], line 1
----> 1 from sklearn.preprocessing import standardScaler

ModuleNotFoundError: No module named 'sklearn'

scaler=standardScaler()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[6], line 1
----> 1 scaler=standardScaler()

NameError: name 'standardScaler' is not defined

import numpy as np
import seaborn as sns
data.Isnull().sum()
​
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 1
----> 1 data.Isnull().sum()

NameError: name 'data' is not defined