### Full Name: Minhaz Bin Farukee
### ID: 1002154424
### Language : Python
### Version: 3.8.8
#### Command Line Arguments:
format of the commmand line arguments:
python main.py <n_samples:int> <distribution:string> --params <param_1_name>=<param_1_value> <param_2_name>=<param_2_value> ....<param_n_name>=<param_n_value>  


```
python main.py 1000 'arb-discrete' --params probs=0.125,.375,.375,.125
python main.py 10000 'uniform' --params a=0 b=1
python main.py 100 'bernoulli' --params p=0.5
python main.py 100 'binomial' --params n=20 p=0.3
python main.py 10 'geometric' --params p=0.6
python main.py 100 'neg-binomial' --params k=10 p=0.4
python main.py 100 'exponential' --params lam=4
python main.py 100 'gamma' --params alpha=10 lam=3
python main.py 100 'normal' --params meu=0 sigma=1

```

