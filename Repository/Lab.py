import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

std = 2
mean = 5
n = 100
liczba_prob = 200
wektor_powtorzen = []

for i in range(0, 1000):

    X = np.random.normal(std, mean, n)

    odchylenie = np.std(X)
    srednia = np.mean(X)

    df = n - 1

    poziom_ufnosci = 0.95

    przedział_ufności = t.interval(poziom_ufnosci, df, loc=srednia, scale=odchylenie / np.sqrt(n))

    if(przedział_ufności[0] <= mean <= przedział_ufności[1]):
        wektor_powtorzen.append(1)
    else:
        wektor_powtorzen.append(0)

plt.hist(wektor_powtorzen, bins=2, density=False, alpha=0.7, color='green', edgecolor='black')
plt.xticks([0, 1], ['0', '1'])
plt.show()