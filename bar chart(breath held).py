import matplotlib.pyplot as plt
import numpy as np

width = 0.4
x = [1,2,3,4,5,6,7,8,9,10]
male = [60.75,67.41,42.19,59.74,52.64,43.37,73.27,59.09,51.15,58.32]
female = [22.22,30.57,17.47,22.39,26.90,36.85,27.55,29.55,13.87,34.66]

bar1 = np.arange (len(x))
bar2 = [i+width for i in bar1]

plt.bar(bar1,male,width, label='Male')
plt.bar(bar2,female,width, label='Female')

plt.xlabel('Seqeunce')
plt.ylabel('Breath Held')
plt.title('Breath held chart between male and female')
plt.legend()
plt.show()
