class Aluno:
    def __init__(self, matricula, nome):
        self.__matricula = matricula
        self.__nome = nome
        self.cursos_inscritos = []

    # metodos getter e setter    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    # metodos de acao
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)
    
    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
        return lista
            