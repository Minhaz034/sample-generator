import random
import math
import matplotlib.pyplot as plt


def bernoulli(p):
    u = random.random()
    sample = 0
    if u < p:
        sample = 1
    return sample

def binomial(n,p):
    sample = 0
    for i in range(n):
        sample += bernoulli(p)
    return sample

def geometric(p):
    geom_sample = 0
    while(1):
        bern_sample = bernoulli(p)
        geom_sample += 1
        if bern_sample == 1:
            break
    return geom_sample

def neg_binomial(k,p):
    neg_binom_sample = 0
    for i in range(k):
        neg_binom_sample += geometric(p=p)
    return neg_binom_sample
        
def poisson(lambda_val): 
    k = 0
    e_pow_lambda = math.exp(-lambda_val)
    u = 1
    while(1):
        u_new = random.random()
        u *= u_new
        if u > e_pow_lambda:
            k += 1
        else: break        
    return k        

def exponential(lam):
    u = random.random()
    sample = -(1/lam)*




def uniform(a,b):
    u = random.random()
    return a + u*(b-a)

def sampleGen(n_samples, distribution, **parameters):
    #SETTING THE SEED:
    random.seed(42)
    generated_samples = []
    distribution = distribution.lower()
    print(f"Generating {n_samples} samples from {distribution} distribution")
    if distribution == 'bernoulli':
        # extracting the parameter 'p' for bernoulli distribution
        p = parameters['p']
        for i in range(n_samples):
            generated_samples.append(bernoulli(p=p))

    elif distribution == 'binomial':
        n = parameters['n']
        p = parameters['p']
        for i in range(n_samples):
            generated_samples.append(binomial(n=n , p=p))
    
    elif distribution == 'geometric':
        p = parameters['p']
        generated_samples =  [geometric(p) for i in range(n_samples)]
            
    elif distribution == 'neg-binomial':
        k = parameters['k']
        p = parameters['p']
        generated_samples = [neg_binomial(k,p) for i in range(n_samples)]
    
    elif distribution == 'poisson':
        lambda_val = parameters['lambda_val']
        generated_samples = [poisson(lambda_val=lambda_val) for i in range(n_samples)]

    elif distribution == 'uniform':
        a = parameters['a']
        b = parameters['b']
        generated_samples = [uniform(a,b) for i in range(n_samples)]




    return generated_samples

    


    



if __name__ == '__main__':
    samples = sampleGen(n_samples=10000, distribution='geometric',p=0.4)
    print(samples)
    plt.hist(samples)
    plt.show()


