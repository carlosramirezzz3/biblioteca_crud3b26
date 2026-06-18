from dao.libro_dao import LibroDAO

def main():
    try:
        Libro_dao = LibroDAO()
        lista = Libro_dao.obtener_todo()  # Aquí recibes la lista de libros
        
        if len(lista) == 0:  
            print("No hay libros registrados")
        else:
            for libro in lista:  
                print(f"id:{libro.id} Nombre:{libro.titulo}  Autor:{libro.autor}  Isbn:{libro.isbn}   Disponible:{libro.disponible}")
                
        print("\n Conexion exitosa con la base de datos ")
    except Exception as e:
        print("Error")
        print(e)

if __name__ == "__main__":
    main()