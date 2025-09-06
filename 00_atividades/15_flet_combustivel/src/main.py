# pip install flet
# pip install pyinstaller
# pip install pillow

# comando para gerar o executavel
# flet pack .\00_atividades\15_flet_combustivel\src\main.py --name=combustivel_app --icon .\00_atividades\15_flet_combustivel\src\assets\icon_bomba_combustivel.png
# apos execucao do comando acima, o executavel sera gerado na pasta dist

import flet as ft


def main(page: ft.Page):

    # funcao do evento
    def indicar_combustivel_mais_vantajoso(e):

        # verifica se o valor da gasolina foi informado
        if not valor_gasolina.value:
            valor_gasolina.error_text = "Informe o valor da gasolina"
            page.update()
        else:
            valor_gasolina.error_text = None
            page.update()

        # verifica se o valor do etanol foi informada
        if not valor_etanol.value:
            valor_etanol.error_text = "Informe o valor do etanol"
            page.update()
        else:
            valor_etanol.error_text = None

            # calcula a vantajosidade
            valor_gasolina.value = float(valor_gasolina.value.replace(",", "."))
            valor_etanol.value = float(valor_etanol.value.replace(",", "."))

            resultado_divisao = valor_etanol.value / valor_gasolina.value
            dialogo_modal.title.value = f"O resultado da divisao do valor do etanol pelo valor da gasolina é: {resultado_divisao:.2f}"

            if resultado_divisao <= 0.7:
                dialogo_modal.content.value = "O ETANOL é mais vantajoso."
            else:
                dialogo_modal.content.value = "A GASOLINA é mais vantajosa."
            
            # abre a caixa de dialogo modal
            page.open(dialogo_modal)

            # limpa os campos
            valor_gasolina.value = None
            valor_etanol.value = None

            page.update()

    # propriedades da pagina
    page.title = "Combustivel - Indicação"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variaveis
    valor_gasolina = ft.TextField(label="Valor da gasolina", prefix_text="R$")
    valor_etanol = ft.TextField(label="Valor da etanol", prefix_text="R$", on_submit=indicar_combustivel_mais_vantajoso)

    # caixa de dialogo
    dialogo_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("Fechar", on_click=lambda e: page.close(dialogo_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # barra de titulo
    page.appbar = ft.AppBar(title=ft.Text("Verificar antajosidade", size=16), center_title=True)

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Indicar vantajosidade dos combustiveis", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True
        ),
        ft.ResponsiveRow(
            [
                ft.Container(valor_gasolina, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(valor_etanol, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Verificar", on_click=indicar_combustivel_mais_vantajoso),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)
