import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[4,6,8,3,7]

plt.scatter(x, y, label="skitscat", color='c', marker='*', s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot :-)')
plt.legend()
plt.show()