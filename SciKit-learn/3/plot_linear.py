import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties()

plt.figure()
plt.title('this is title')
plt.xlabel('x label')
plt.ylabel('y label')
plt.axis([0, 25, 0, 25])
plt.grid(True)
x = [[1],[2],[3],[4],[5],[6]]
y = [[1],[2.1],[2.9],[4.2],[5.1],[5.8]]
plt.plot(x, y, 'k.')
plt.show()