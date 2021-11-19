'''2.	Fazer um algoritmo para criar um vetor x com 10 posições começando pelo zero. A construção desse vetor dará pela seguinte maneira
Sendo “i” a posição do elemento dentro desse vetor v.
Se a posição i for par, entáo esse elemento na posição i do vetor x deverá ser alimentado da seguinte maneira
X[i] = 3'+7*(i!)
Lembrando que “i!” indica o fatorial da posição i


Caso o i seja um valor ímpar, entáo esse elemento na posição i do vetor x devera ser alimentado da seguinte maneira
X[] =2+4’tn()
Lembrando que “in(i)” indica o logaritmo neperiano do número i


Alimentado esse vetor, deseja saber qual a posiçáo do maior elemento desse vetor e qual a média dos elementos contidos nesse vetor (Arredonde o valor para 2 casas decimais).
'''

import math 
x = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(x)):
    if i % 2 == 0: 
        x[i] = (3**i) + 7*(math.factorial(i))
    else:
        x[i] = (2**i) + 4*(math.log(i))
print(x)
posicao_maior_vetor = x.index(max(x))
media_vetor = sum(x)/len(x)

print('A posição do maior elemento do vetor é {} e a média dos elementos do vetor é {:.2f}'.format(posicao_maior_vetor,media_vetor))