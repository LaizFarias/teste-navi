'''3.	Fazer um algoritmo que leia a nota de 5 alunos e uma nota para cada aluno Guarde essas informações 
 em um dicionário e depois apresente o aluno com a maior nota e a sua respectiva nota.'''

#A função irá receber um lista de nomes e uma lista de notas, com base nisso, irá calcular qual é o aluno com a maior nota. 
estado = True 
#Antes de tudo criei as listas para armazenar o nome do aluno e a nota fornecida pelo usuário
nomes = []
notas = []
#Foi criado um loop infinito de maneira que usuário possa adicionar quantos nomes e quantas notas ele quiser
while estado:
    nome_do_aluno = input('Qual é o nome do aluno ')
    #para o usuário para de digitar, basta que ele digite a palavra nenhum para o nome do aluno 
    if nome_do_aluno == 'nenhum':
        estado = False
    else:
        nomes.append(nome_do_aluno)
        nota_do_aluno = int(input('Qual é a nota desse aluno '))
        notas.append(nota_do_aluno)
    # se ele digitar a palavra nenhum em nome_do_aluno o loop para e devolver a lista até onde o usuário digitou

dicionario_de_notas = {}

def maior_nota(nomes,notas):

    for nome in nomes:
        indice = nomes.index(nome)
        dicionario_de_notas[nome] = notas[indice]

    maior_nota = 0
    aluno_de_maior_nota = ''

    for aluno,nota in dicionario_de_notas.items():
        if nota > maior_nota:
            maior_nota = nota 
            aluno_de_maior_nota = aluno 

    return 'A maior nota é {} e é do aluno {}'.format(maior_nota,aluno_de_maior_nota)

print(maior_nota(nomes,notas))
