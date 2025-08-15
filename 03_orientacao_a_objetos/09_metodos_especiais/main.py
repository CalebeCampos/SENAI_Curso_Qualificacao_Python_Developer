import Pessoa as p

def main():
    usuario = p.Pessoa(nome="Julio Cesar", idade=37)
    
    # chamadno o metodo __str__
    print(usuario)

    # chamando o metodo __len__
    print(f"Idade: {len(usuario)}")

    # executando o metodo destritor __del__
    del(usuario)

if __name__ == "__main__":
    main()
