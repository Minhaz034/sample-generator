import random
import math
import matplotlib.pyplot as plt

def arb_discrete(probs) ->list(float):
    n = len(probs)
    for i in range


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
    return -(1/lam)* math.log(1-u)

def gamma(alpha, lam):
    exp_samples = [exponential(lam) for i in range(alpha)]
    return sum(exp_samples)

def normal(meu, sigma):
    u1 = random.random()
    u2 = random.random()
    log_term  = math.sqrt(-2*math.log(u1))
    z1 = log_term * math.cos(2*math.pi*u2)
    z2 = log_term * math.sin(2*math.pi*u2) 
    x1 = z1*sigma + meu
    x2 = z2*sigma + meu
    return x1, x2

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

    elif distribution == 'exponential':
        lam = parameters['lam']
        generated_samples = [exponential(lam) for i in range(n_samples)]
   
    elif distribution == 'gamma':
        alpha = parameters['alpha']
        lam = parameters['lam']
        generated_samples = [gamma(alpha,lam) for i in range(n_samples)]
    
    elif distribution == 'normal':
        meu = parameters['meu']
        sigma = parameters['sigma']
        generated_samples = [sample for i in range(n_samples) for sample in normal(meu, sigma)]


    return generated_samples

    


    



if __name__ == '__main__':
    #samples = sampleGen(n_samples=10000, distribution='gamma',alpha=2,lam = 3)
    samples_norm = sampleGen(n_samples=100, 
                             distribution='normal', 
                             meu = 0, 
                             sigma = 1
    )
    print(samples_norm)
    plt.hist(samples_norm)
    plt.show()


