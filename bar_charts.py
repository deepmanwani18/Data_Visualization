import matplotlib.pyplot as plt
x=[0,2,4,6,8]
y=[4,6,8,3,7]

x2=[1,3,5,7,9]
y2=[5,7,9,1,8]

plt.bar(x, y, label='Bar1')
plt.bar(x2, y2, label='Bar2', color='g')

plt.xlabel('countries')
plt.ylabel('population(in million)')
plt.title('Bar Chart\nCheck it out')
plt.legend()
plt.show()