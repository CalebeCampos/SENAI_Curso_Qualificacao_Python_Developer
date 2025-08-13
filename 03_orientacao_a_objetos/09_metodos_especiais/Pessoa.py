class Pessoa:

    # metodo especial construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # metodo especial que retorna uma string pre programada bastando chamar apenas o nome_variavel_instanciada
    def __str__(self):
        return f"Meu nome é: {self.nome}\nMinha idade é: {self.idade}"
    
    # metodo especial que retorna umo valor de um atributo do tipo inteiro pre programada bastando chamar len(nome_variavel_instanciada)
    def __len__(self):
        return self.idade
    
    # metodo especial que destroi da memoria o objeto instanciado dessa classe
    def __del__(self):
        print(f"Metodo destrutor. Objeto {self.nome} destruido com sucesso!")