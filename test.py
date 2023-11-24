import numpy as np
import random
import matplotlib.pyplot as plt

random.seed(42)

samples_binom = np.random.binomial(100,0.3,10000)
samples_geom = np.random.geometric (p=0.3, size = 100000)
samples_neg_binom = np.random.negative_binomial (n=100,p=0.3, size = 100000)
samples_poisson = np.random.poisson(lam=5,size=10000)
samples_exp = np.random.exponential(scale=5,size=10000)
samples_norm = np.random.normal(loc = 0, scale = 1,size=100)

plt.hist(samples_norm)
plt.show()

