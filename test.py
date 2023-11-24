import numpy as np
import matplotlib.pyplot as plt

samples_binom = np.random.binomial(100,0.3,10000)
samples_geom = np.random.geometric (p=0.3, size = 100000)
samples_neg_binom = np.random.negative_binomial (n=100,p=0.3, size = 100000)
samples_poisson = np.random.poisson(lam=5,size=10000)

plt.hist(samples_geom)
plt.show()

