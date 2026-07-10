import flet as ft

def main_window(page: ft.Page):

    #Configurar pagina 
    page.title = "Sistemas de Gestion de Biblioteca"
    page.window_width = 1100
    page.window_height =700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    #Elementos del contenedor principal 
    titulo = ft.Text(
        "Sistema de Gestion de Biblioteca",
        size = 24,
        weight= ft.FontWeight.BOLD
    )
    subtitulo = ft.Text(
        "Seleccione una opcion del menu",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )
    #Creacion del contenedor principal 
    contenido = ft.Container(
        content = ft.Colum(
            controls =[
                titulo,
                subtitulo
            ],
            spacing = 10,
        ),
        padding= 30,
        expand = True
    )
     #crear el menu lateral 
    menu_lateral = ft.Container(
         width= 220,
         bgcolor= ft.Colors.BLUE_GREY_900,
         padding= 20,
         content= ft.Colum(
             controls = [
                 ft.Text(
                     "Biblioteca",
                     size = 22,
                     weinht = ft.FrontWeight.BOLD,
                     color = ft.Colors.WHITE
                 ),
                 ft.Text(
                    "Sistema de Gestion",
                    size = 12,
                    color = ft.Colors.WHITE
                 ),
                 ft.Divider(color = ft.Colors.BLUE_GREY_700),
                 #Botones
                 ft.ElevatedButton(
                   "Libros"
                   icon =ft.Icons.BOOK,
                   width = 100  
                 ),
                   ft.ElevatedButton(
                   "Usuarios"
                   icon =ft.Icons.PERSON,
                   width = 100  
                 ),
                   ft.ElevatedButton(
                   "Prestamos"
                   icon =ft.Icons.SWAP_HORIZ,
                   width = 100  
                 ),
                   ft.ElevatedButton(
                   "Devoluciones"
                   icon =ft.Icons.KEYBOARD_RETURN,
                   width = 100  
                 ),
             ],
             spacing = 15
         )
     )
    
    #Layout de la pagina 
    layout = ft.Row(
        controls = [
        menu_lateral,
        contenido
        ],
        expand = True
    )

    page.add(layout)