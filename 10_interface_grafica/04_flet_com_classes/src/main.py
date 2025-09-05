import flet as ft
from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    idade: int
    peso: float
    salario: float
    email: str

def main(page: ft.Page):

    # propriedades da pagina
    page.title = "Dados do Usuario"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variaveis de saida
    titulo_saida = ft.Text(weight="bold")
    nome_saida = ft.Text()
    idade_saida = ft.Text()
    peso_saida = ft.Text()
    salario_saida = ft.Text()
    email_saida = ft.Text()

    def preenche_variaveis_saida_usuario(e):
        titulo_saida.value = "Dados do usuario\n"
        nome_saida.value = f"Nome: {usuario.nome.value}"
        idade_saida.value = f"Idade: {usuario.idade.value} anos"
        peso_saida.value = f"Peso: {usuario.peso.value} kg"
        salario_saida.value = f"Salario: R$ {usuario.salario.value}"
        email_saida.value = f"Email: {usuario.email.value}"
        page.update()

    # instancia da classe
    usuario = Usuario(
        nome="",
        idade=0,
        peso=0.0,
        salario=0.0,
        email=""
    )

    usuario.nome = ft.TextField(label="Nome completo", width=500)
    usuario.idade = ft.TextField(label="Idade", suffix_text="anos", width=100)
    usuario.peso = ft.TextField(label="Peso", suffix_text="kg", width=100)
    usuario.email = ft.TextField(label="Email", width=700)
    usuario.salario = ft.TextField(label="Salario", prefix_text="R$ ", width=100, on_submit=preenche_variaveis_saida_usuario)

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do usuario", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        usuario.nome,
        usuario.email,
        usuario.idade,
        usuario.peso,
        usuario.salario,
        ft.ElevatedButton("Enviar", on_click=preenche_variaveis_saida_usuario),
        titulo_saida,
        nome_saida,
        idade_saida,
        peso_saida,
        salario_saida,
        email_saida
    )

ft.app(main)
