banco_de_dados = []
matricula_atual = 0

def criarAluno(nome, idade, curso):
    # Permite alterar o valor de uam variável global
    global matricula_atual
    matricula_atual += 1
    # Criando um aluno através de um dicionário
    aluno = {'matricula': matricula_atual, 'nome': nome, 'idade': idade, 'curso': curso}
    return aluno

def adicionarAluno():
    nome = input('Digite a nome: ')
    idade = int(input('Digite a idade: '))
    curso = input('Digite o curso: ')
    aluno = criarAluno(nome, idade, curso)
    banco_de_dados.append(aluno)
    print('Aluno adicionado com sucesso!')

def listarTodosAlunos():
    print('----- Alunos Matriculados -----')
    for aluno in banco_de_dados:
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print('---------------------------\n')

def editarAluno():
    matricula = int(input('Digite a matrícula: '))
    nome = input('Digite a nome: ')
    idade = int(input('Digite a idade: '))
    curso = input('Digite o curso: ')
    aluno = alunoExiste(matricula)
    if aluno:
            aluno['nome'] = nome
            aluno['idade'] = idade
            aluno['curso'] = curso
            print('Dados alterados com sucesso!')
    else:
        print('Matrícula informada não encontrada!')

def alunoExiste(matricula):
    for aluno in banco_de_dados:
        if aluno['matricula'] == matricula:
            return aluno
    return False

def removerAluno():
    matricula = int(input('Digite a matrícula: '))
    aluno = alunoExiste(matricula)
    if aluno:
        banco_de_dados.remove(aluno)
        print('Aluno removido com sucesso!')
    else:
        print('Matrícula não encontrada!')

def consultarAluno():
    matricula = int(input('Digite a matrícula: '))
    aluno = alunoExiste(matricula)
    if aluno:
        print('--- DAODS DO ALUNO ---')
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
    else:
        print('Matrícula encontrada')

opcoes = {
    '1': adicionarAluno,
    '2': editarAluno,
    '3': removerAluno,
    '4': consultarAluno,
    '5': listarTodosAlunos
}

def menu():
    while True:
        print('--- BEM VINDO AO MENU ESCOLAR ---')
        print('1 - Adicionar aluno')
        print('2 - Editar aluno')
        print('3 - Remover aluno')
        print('4 - Buscar aluno')
        print('5 - Listar Todos os alunos')
        print('6 - Sair do sistema')
        opcao = input('Selecione uma opção: ')
        if opcao in opcoes:
            opcoes[opcao]()
        else:
            break
menu()            
