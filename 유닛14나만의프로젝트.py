import csv
import numpy as np
import matplotlib.pyplot as plt

# with open('age.csv') as f:
#     data = csv.reader(f)
#     next(data)
#     # for row in data:
#     #     pass
#
#     # name = input('지역(읍면동 단위) : ')
#     name = '평거동'
#     for row in data:
#         if name in row[0]:
#             for i in row[3:]:
#                 home = np.array(row[3:],dtype=int)
#     print(home)
#     print(len(home))
#
# plt.rc('font', family='Malgun Gothic')#Gulim
# plt.plot(home)
# plt.show()

# result_name = ''
# main_sum = 0
# total = {}
# sum1 = 0
# sum2 = 100000
# with open('age.csv') as f:
#     data = csv.reader(f)
#     next(data)
#
#     # name = input('지역(읍면동 단위) : ')
#     main_name = '평거동'
#     for row in data:
#         sum1 = 0
#         if main_name in row[0]:
#             g_result = np.array(row[3:],dtype=int)
#             for i in row[3:]:
#                 main_sum += int(i.replace(',',''))
#         else:
#             for i in row[3:]:
#                 sum1 += int(i.replace(',',''))
#             total[row[0]] = sum1
#     a = 0
#     for i in total:
#         if abs(list(total.values())[a] - main_sum) < sum2:
#             sum2 = abs(list(total.values())[a] - main_sum)
#             result_name = i
#         a+=1
#     print(result_name,sum2)
#
# with open('age.csv') as f:
#     data = csv.reader(f)
#     next(data)
#     for asd in data:
#         if result_name == asd[0]:
#             g_result2 = np.array(asd[3:],dtype=int)
#             print(g_result2,10)
#
# plt.rc('font', family='Malgun Gothic')#Gulim
# plt.plot(g_result)
# plt.plot(g_result2)
# plt.show()