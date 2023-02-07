 pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_csv(r'C:\Users\HP\Downloads\insurance.csv')
print(data)
      age     sex     bmi  children smoker     region      charges
0      19  female  27.900         0    yes  southwest  16884.92400
1      18    male  33.770         1     no  southeast   1725.55230
2      28    male  33.000         3     no  southeast   4449.46200
3      33    male  22.705         0     no  northwest  21984.47061
4      32    male  28.880         0     no  northwest   3866.85520
...   ...     ...     ...       ...    ...        ...          ...
1333   50    male  30.970         3     no  northwest  10600.54830
1334   18  female  31.920         0     no  northeast   2205.98080
1335   18  female  36.850         0     no  southeast   1629.83350
1336   21  female  25.800         0     no  southwest   2007.94500
1337   61  female  29.070         0    yes  northwest  29141.36030

[1338 rows x 7 columns]
data.describe()
age	bmi	children	charges
count	1338.000000	1338.000000	1338.000000	1338.000000
mean	39.207025	30.663397	1.094918	13270.422265
std	14.049960	6.098187	1.205493	12110.011237
min	18.000000	15.960000	0.000000	1121.873900
25%	27.000000	26.296250	0.000000	4740.287150
50%	39.000000	30.400000	1.000000	9382.033000
75%	51.000000	34.693750	2.000000	16639.912515
max	64.000000	53.130000	5.000000	63770.428010
data.head()
age	sex	bmi	children	smoker	region	charges
0	19	female	27.900	0	yes	southwest	16884.92400
1	18	male	33.770	1	no	southeast	1725.55230
2	28	male	33.000	3	no	southeast	4449.46200
3	33	male	22.705	0	no	northwest	21984.47061
4	32	male	28.880	0	no	northwest	3866.85520
data.tail()
age	sex	bmi	children	smoker	region	charges
1333	50	male	30.97	3	no	northwest	10600.5483
1334	18	female	31.92	0	no	northeast	2205.9808
1335	18	female	36.85	0	no	southeast	1629.8335
1336	21	female	25.80	0	no	southwest	2007.9450
1337	61	female	29.07	0	yes	northwest	29141.3603
data.columns
Index(['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'], dtype='object')
data.nunique()
age           47
sex            2
bmi          548
children       6
smoker         2
region         4
charges     1337
dtype: int64
data['sex'].unique()
array(['female', 'male'], dtype=object)
data.isnull().sum()
age         0
sex         0
bmi         0
children    0
smoker      0
region      0
charges     0
dtype: int64
data = data.drop(['smoker', 'charges' ], axis=1)
data.head()
age	sex	bmi	children	region
0	19	female	27.900	0	southwest
1	18	male	33.770	1	southeast
2	28	male	33.000	3	southeast
3	33	male	22.705	0	northwest
4	32	male	28.880	0	northwest
sns.countplot (x='age', hue='region',data='data')
​
        
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[13], line 1
----> 1 sns.countplot (x='age', hue='region',data='data')

NameError: name 'sns' is not defined

Sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[14], line 1
----> 1 Sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)

NameError: name 'Sns' is not defined

sns.pairplot('data')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[15], line 1
----> 1 sns.pairplot('data')

NameError: name 'sns' is not defined

sns.relplot('x=region','y=age', hue='bmi', data=data )
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[17], line 1
----> 1 sns.relplot('x=region','y=age', hue='bmi', data=data )

NameError: name 'sns' is not defined