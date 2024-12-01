import matplotlib.pyplot as plt
import numpy as np

width = 0.4

x = [1,2,3,4,5,6,7,8,9,10]
female = [175,158,166,175,160,165,166,170,170,172]
male = [184,182,180,191,189,181,180,170,176,185]

bar1= np.arange(len(x))
bar2 = [i+width for i in bar1]

plt.bar(bar1,male,width,label = 'Males')
plt.bar(bar2,female,width,label = 'Females')

plt.xlabel('Sequence')
plt.ylabel('height')
plt.title('Height between male and females')
plt.xticks()
plt.legend()
plt.show()
