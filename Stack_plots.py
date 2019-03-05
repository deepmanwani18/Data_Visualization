import matplotlib.pyplot as plt
days=[1,2,3,4,5,6]

sleeping=[11,11,8, 9, 7, 9]
eating=  [3, 2, 3, 3, 5, 2]
working= [5, 8, 9, 7, 10, 9]
playing= [5, 3, 4, 5, 2, 4]

plt.stackplot(days,sleeping,eating,working,playing, colors=['k','m','b','r'])

plt.plot([],[], color='k', label='sleeping') # we don't have legends in stack plot so using seste jugad -_-
plt.plot([],[], color='m', label='eating')
plt.plot([],[], color='b', label='working')
plt.plot([],[], color='r', label='playing')

plt.xlabel('days')
plt.ylabel('time')
plt.title('Stack Plot :-)')
plt.legend()
plt.show()