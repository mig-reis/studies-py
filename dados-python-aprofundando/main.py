import numpy as np
import matplotlib.pyplot as plt 

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# Inverte linha por coluna
dadoTransporto = dado.T

precos = dadoTransporto[:, 1:6]

datas = np.arange(1, 88)

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

# Criando gráfico
plt.plot(datas, Moscow)
plt.plot(datas, Kaliningrad)
plt.plot(datas, Petersburg)

plt.legend(['Moscow', 'Kaliningrad', 'Petersburg'])
plt.show()