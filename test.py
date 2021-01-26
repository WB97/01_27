import numpy as np
import csv
import matplotlib.pyplot as plt

# with open('age.csv') as f:
#     data = csv.reader(f)
#     next(data)
#
#     for row in data:
#         if '평거동' in row[0]:
#             for i in row[3:]:
#                 s = np.array(row[3:],dtype=int)/int(row[2].replace(',',''))
#         if '중계1동' in row[0]:
#             for i in row[3:]:
#                 g = np.array(row[3:],dtype=int)/int(row[2].replace(',',''))
#     re = np.sum((s-g)**2)
#     print(re)

a = []
with open('age.csv') as f:
    data = csv.reader(f)
    next(data)
    data = list(data)

    name = '평거동'
    mn = 1
    result_name = ''
    result = 0

    for row in data:
        if name in row[0]:
            home = np.array(row[3:],dtype=int)/int(row[2])
    for row in data:
        away = np.array(row[3:],dtype=int)/int(row[2])
        s = np.sum((home-away)**2)
        if s < mn and name not in row[0]:
            mn = s
            result = away

plt.rc('font', family='Malgun Gothic')
plt.plot(home)
plt.plot(result)
plt.show()