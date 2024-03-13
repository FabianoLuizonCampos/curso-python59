# Utilizando a bilbioteca Flet
# pip install flet

import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Meu Primeiro Programa em Flet"     
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    def somar(e):
        numero = int(txt_numero.value) + 1
        txt_numero.value = str(numero)
        pagina.update()

    def subtrair(e):
        numero = int(txt_numero.value) - 1
        txt_numero.value = str(numero)
        pagina.update()

    btn_mais = ft.IconButton(ft.icons.ADD, on_click=somar)
    btn_menos = ft.IconButton(ft.icons.REMOVE, on_click=subtrair)

    txt_numero = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)

    pagina.add(
        ft.Row (
            [
                btn_menos,
                txt_numero,
                btn_mais
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
    )
    

ft.app(target=main)