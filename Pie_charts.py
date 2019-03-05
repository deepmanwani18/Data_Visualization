import matplotlib.pyplot as plt

slices = [8, 2, 10, 4]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'g', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0,0,0.2),
        autopct='%0.2f%%')      # for percentage 0.2f denotes floating point upto 2 places of decimal

plt.title('Pie Chart :-)')
plt.show()