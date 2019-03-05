import matplotlib.pyplot as plt

x=[1,2,3,4,4]
y=[4,10,8,9,3]

x2=[4,4.5,7,6]
y2=[3,10,4,0]

plt.plot(x, y, label='first line')
plt.plot(x2, y2, label='second line')
plt.xlabel('time taken')
plt.ylabel('displacement covered')
plt.title('s-t graph\nCheck it out')
plt.legend()
plt.show()