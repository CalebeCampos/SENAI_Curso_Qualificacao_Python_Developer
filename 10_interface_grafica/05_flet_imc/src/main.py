import flet as ft


def main(page: ft.Page):

    # funcao do evento
    def calcular_imc(e):
        # verifica se o peso foi informado
        if not peso.value:
            peso.error_text = "Informe o peso"
            page.update()
        else:
            peso.error_text = None
            page.update()
        # verifica se a altura foi informada
        if not altura.value:
            altura.error_text = "Informe a altura"
            page.update()
        else:
            altura.error_text = None
            # calcula o imc
            peso.value = float(peso.value.replace(",", "."))
            altura.value = float(altura.value.replace(",", "."))
            imc = peso.value / (altura.value ** 2)
            dialogo_modal.title.value = f"Seu IMC é {imc:.2f}"
            # diagnostico
            if imc < 18.5:
                dialogo_modal.content.value = "Você está abaixo do peso."
            elif imc < 25:
                dialogo_modal.content.value = "Você está com o peso normal."
            elif imc < 30:
                dialogo_modal.content.value = "Você está com sobrepeso."
            elif imc < 35:
                dialogo_modal.content.value = "Você está com obesidade grau I."
            elif imc < 40:
                dialogo_modal.content.value = "Você está com obesidade grau II."
            else:
                dialogo_modal.content.value = "Você está com obesidade grau III."
            
            # abre a caixa de dialogo modal
            page.open(dialogo_modal)

            # limpa os campos
            peso.value = None
            altura.value = None

            page.update()

    # propriedades da pagina
    page.title = "IMC - Calculadora"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variaveis
    peso = ft.TextField(label="Peso (kg)", suffix_text="kg")
    altura = ft.TextField(label="Altura (m)", suffix_text="m", on_submit=calcular_imc)

    # caixa de dialogo
    dialogo_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("Fechar", on_click=lambda e: page.close(dialogo_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # barra de titulo
    page.appbar = ft.AppBar(title=ft.Text("IMC", size=16), center_title=True)

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("IMC - Indice de Massa Corporal", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True
        ),
        ft.ResponsiveRow(
            [
                ft.Container(peso, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(altura, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)
