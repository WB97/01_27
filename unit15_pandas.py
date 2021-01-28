import pandas as pd
import numpy as np

# df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
# summer = df[1].iloc[1:,:5]
# summer.columns = ['경기수','금','은','동','계']
# summer = summer.sort_values('금',ascending=False)
# print(summer)
# summer.to_excel('하계올림픽메달.xlsx')

index = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.round(np.random.rand(8,3)*100), index=index, columns=list('ABC'))
# df['D'] = df['A']/df['B']
print(df.T)
# df = df.sub(df['A'],axis=0)
# print(df)
# df2 = df[df['B']>0.4]
# print(df2)