import flet as ft


def main(page: ft.Page):

    # propriedades da pagina
    page.title = "Eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variaveis
    texto_entrada = ft.TextField(label="Digite seu texto")
    texto_saida = ft.Text()

    # funcoes
    def exibir_texto_saida(e):
        texto_saida.value = texto_entrada.value
        page.update()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("App Evento", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        texto_entrada,
        ft.ElevatedButton("Enviar", on_click=exibir_texto_saida),
        texto_saida
    )


ft.app(main)
