import matplotlib.pyplot as plt

ages=[2,34,22,8,23,4,25,29,54,12,57,72,61,26,39,63,31,39,25,15,44,19,33]

#ids=[x for x in range(len(ages))]
#plt.bar(ids, ages, label='Bar1')

bins=[0,10,20,30,40,50,60,70,80]
plt.hist(ages, bins, histtype='bar', rwidth=0.6)

plt.xlabel('Ids')
plt.ylabel('Ages')
plt.title('Histogram!')
plt.legend()
plt.show()