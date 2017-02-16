import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import os

#optional style
#matplotlib.style.use('ggplot')
# draw 2000 random points and plot the sum
df_rand = pd.Series(np.random.randn(2000))
df_rand_sum = df_rand.cumsum()
#df_rand_sum.plot()
#plt.show()



# overplot the random with the pure distribution
#fig, ax = plt.subplots()
#n, bins, patches = ax.hist(df_rand, 50, normed=1)
#y = matplotlib.mlab.normpdf(bins, 0, 1)
#ax.plot(bins, y, '--')
#ax.set_xlabel('Random number')
#ax.set_ylabel('Probability density')
#ax.set_title(r'Normal distribution with $\mu=0$, $\sigma=1$')
#fig.tight_layout()
#plt.show()


# basic plot of a function that we export to png
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)
plt.xlabel('Time [s]')
plt.ylabel('Y-value')
plt.title('Sinusoid')
plt.grid(True)
plt.savefig(os.path.abspath('../Results/sinusoid.png'))
plt.show()
