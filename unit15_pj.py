import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Malgun Gothic')
df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df = df.div(df['2020년12월_계_총인구수'], axis=0)
del df['2020년12월_계_총인구수'], df['2020년12월_계_연령구간인구수']
a = df.index.str.contains('평거동')
df2 = df[a]

# print(df2)

plt.rc('font',family='Malgun Gothic')
# df2.T.plot()
# plt.show()
plt.rcParams['axes.unicode_minus'] = False
x = df.sub(df2.iloc[0],axis=1)
y = np.power(x,2)
z = y.sum(axis=1)
i = z.sort_values().index[:5]

print(df.loc[i])

# df.loc[np.power(df.sub(df2.iloc[0], axis=1), 2).sum(axis=1).sort_values().index[:5]].T.plot()

# print(df.loc[i])

df.loc[i].T.plot()
plt.show()