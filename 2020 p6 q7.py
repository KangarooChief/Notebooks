import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

p=0.5
q=0.5
n=100

t=[[1-p,p],[q,1-q]]
sd = 0.5

def rx(n):
  Xs = [np.random.choice([0,1],p=[q/(p+q),p/(p+q)])]
  for i in range(n):

    Xs.append(np.random.choice([0,1],p=[t[Xs[-1]][0],t[Xs[-1]][1]]))
  return Xs

actualXs = rx(n)
actualYs = np.random.normal(loc=actualXs, scale=sd)

def genWeights(m):
    Xs_samples = [rx(n) for i in range(m)]
    PrY = [np.prod(stats.norm.pdf(actualYs, loc=Xs, scale=sd)) for Xs in Xs_samples]
    ws = PrY/sum(PrY)
    print(len(ws))
    plt.hist([i for i in range(m)],weights=ws, bins=np.linspace (0,1,30))
    plt.show()
    return ws

ws = genWeights(101)
#testing
