import Aluno as a
import Curso as c

def main():
    
    # instanciando os objetos da classe Curso
    curso1 = c.Curso(nome="Python")
    curso2 = c.Curso(nome="Java")
    curso3 = c.Curso(nome="php")
    # instanciando os objetos do classe Aluno
    aluno1 = a.Aluno(matricula="00001", nome="Thiago")
    aluno2 = a.Aluno(matricula="00002", nome="Joao")
    aluno3 = a.Aluno(matricula="00003", nome="Pedro")
    aluno4 = a.Aluno(matricula="00004", nome="José")
    aluno5 = a.Aluno(matricula="00005", nome="Jorge")
    aluno6 = a.Aluno(matricula="00006", nome="Elias")

    # Associando alunos ao curso1
    aluno1.inscrever_curso(curso=curso1)
    aluno2.inscrever_curso(curso=curso1)
    aluno3.inscrever_curso(curso=curso1)
    
    # Associando alunos ao curso2
    aluno4.inscrever_curso(curso=curso2)
    aluno5.inscrever_curso(curso=curso2)

    # Associando curso3 ao aluno6
    curso3.adicionar_aluno(aluno=aluno6)
 
    print(f"{'-'*10} Curso: {curso1.nome} {'-'*10}")
    print("Alunos:")
    for aluno in curso1.listar_alunos():
        print(aluno)

    print(f"{'-'*10} Curso: {curso2.nome} {'-'*10}")
    print("Alunos:")
    for aluno in curso2.listar_alunos():
        print(aluno)

    print(f"{'-'*10} Curso: {curso3.nome} {'-'*10}")
    print("Alunos:")
    for aluno in curso3.listar_alunos():
        print(aluno)


if __name__ == "__main__":
    main()