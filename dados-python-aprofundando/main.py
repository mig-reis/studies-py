import numpy as np
import matplotlib.pyplot as plt 

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# Inverte linha por coluna
dadoTransporto = dado.T

datas = dadoTransporto[:,0]

preços = dadoTransporto[:, 1:6]

datas = np.arange(1, 88)

# Criando gráfico
plt.plot(datas, preços[:, 0])
plt.show()

print(datas)
