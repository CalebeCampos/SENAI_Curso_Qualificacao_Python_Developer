import Aluno
import Curso

def main():
    
    # instanciando os objetos da classe Curso
    curso1 = Curso.Curso(nome="Python")
    curso2 = Curso.Curso(nome="Java")
    # instanciando os objetos do classe Aluno
    aluno1 = Aluno.Aluno(matricula="00001", nome="Thiago")
    aluno2 = Aluno.Aluno(matricula="00002", nome="Joao")
    aluno3 = Aluno.Aluno(matricula="00003", nome="Pedro")
    aluno4 = Aluno.Aluno(matricula="00004", nome="José")
    aluno5 = Aluno.Aluno(matricula="00005", nome="Jorge")
    aluno6 = Aluno.Aluno(matricula="00006", nome="Elias")
    aluno7 = Aluno.Aluno(matricula="00007", nome="Elton")

    # Associando alunos ao curso1
    aluno1.inscrever_curso(curso=curso1)
    aluno2.inscrever_curso(curso=curso1)
    aluno3.inscrever_curso(curso=curso1)
    aluno4.inscrever_curso(curso=curso1)

    # Associando alunos ao curso2
    aluno5.inscrever_curso(curso=curso2)
    aluno6.inscrever_curso(curso=curso2)
 
    print(f"{'-'*10} Curso: {curso1.nome} {'-'*10}")
    print("Alunos:")
    for aluno in curso1.listar_alunos():
        print(aluno)


if __name__ == "__main__":
    main()