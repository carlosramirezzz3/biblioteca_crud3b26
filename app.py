from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
def ver_libros():
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
def insertar_libro():
     print("INSERTAR UN NUEVO LIBRO")
     titulo = input("Escribe el titulo:")
     autor = int(input("Escribe el id del autor:"))
     isbn= input("Escribe el isbn:")
     disponible= True
     
     try:
          
          libro_dao = LibroDAO()
          ultimo_id= libro_dao.obtener_ultimo_id()+1
          libro = Libro( ultimo_id,titulo,autor,isbn,disponible)
          libro_dao.insertar(libro)
          print("Insercion del nuevo libro fue exitosa")
     except Exception as e:
         print("Error al insertar el libro")
         print(e)

def actualizar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        ver_libros()
        libro_dao.obtener_todo()
        id = int(input("Selecciona el id del autor:"))    
        titulo = input("Escribe el titulo:")
        autor = int(input("Escribe el id del autor:"))
        isbn= input("Escribe el isbn")
        disponible= bool(input("Escribe si esta disponible:"))
        libro = Libro(id,titulo,autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print("El libro fue actualizado con exito")
    except Exception as e:    
        print("Error al actualizar el libro")
        print(e)

def eliminar_libro():
     try:
         libro_dao = LibroDAO() 
         print("lista de libros disponibles")
         libro_dao.obtener_todo()
         id = int(input("Escribe el id del libro a eliminar:"))  
         libro_dao.eliminar(id)
         print(f"El libro {id} ha siso eliminado con exito ")
     except Exception as e:
         print(f"Error al eliminar el libro (id)")   
         print(e) 

def menu_libros():
     print("1. Ver todos los libros")
     print("2. Insertar un nuevo libro ")
     print("3. Actualizar un libro existente")
     print("4. Eliminar un libro existente")
     opcion = int(input("Selecciona una opcion (1-4):"))



     match opcion:
          case 1:
               ver_libros()
          case 2:
               insertar_libro()
          case 3:
               actualizar_libro()
          case 4:  
               eliminar_libro()      
    #metodos usuarios 
def ver_usuarios():
     try:
        Usuario_dao = UsuarioDAO()
        lista = Usuario_dao.obtener_todo()  
        
        if len(lista) == 0:  
            print("No hay usuarios registrados")
        else:
            for usuario in lista:  
               print(f"id:{usuario.id} Nombre:{usuario.nombre} Matricula:{usuario.matricula} Carrera:{usuario.carrera} Correo:{usuario.correo} Estatus:{usuario.activo}")
                
        print("\n Conexion exitosa con la base de datos ")
     except Exception as e:
        print("Error")
        print(e)   
def insertar_usuario():
     print("---Insertar nuevo usuario---")
     nombre = input("Escribe el nombre del usuario: ")
     matricula = input("Escribe la matricula:")
     carrera= int(input("Escribe el id de la carrera:"))
     correo= input("Ingrese el correo:")
     activo = True
     
     try:
          
          usuario_dao = UsuarioDAO()
          ultimo_id= usuario_dao.obtener_ultimo_id()+1
          usuario = Usuario( ultimo_id,nombre,matricula,carrera,correo,activo)
          usuario_dao.insertar(usuario)
          print("Insercion del nuevo usuario fue exitosa")
     except Exception as e:
         print("Error al insertar el usuario")
         print(e)

def actualizar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles")
        ver_usuarios()
        usuario_dao.obtener_todo()
        id = int(input("Selecciona el id del usuario:"))    
        nombre = input("Escribe el nombre del usuario :")
        matricula = input("Escribe el numero de la matricula:")
        carrera = int(input("Escribe el id de la carrera:"))
        correo= input("Escribe el correo nuevo: ")
        activo= bool(input("Escribe si el usuario esta activo:"))
        usuario = Usuario(id,nombre,matricula,carrera, correo, activo)
        usuario_dao.actualizar(usuario)
        print("El usuario fue actualizado con exito")
    except Exception as e:    
        print("Error al actualizar el usuario")
        print(e)
def eliminar_usuario():
     try:
         usuario_dao = UsuarioDAO() 
         print("lista de usuarios disponibles")
         usuario_dao.obtener_todo()
         id = int(input("Escribe el id del usuario a eliminar:"))  
         usuario_dao.eliminar(id)
         print(f"El usuario {id} ha siso eliminado con exito ")
     except Exception as e:
         print(f"Error al eliminar el usuario (id)")   
         print(e) 

     
def menu_usuarios():
     print("1. Ver todos los usuarios")
     print("2. Insertar un nuevo usuario ")
     print("3. Actualizar un usuario existente")
     print("4. Eliminar un usuario existente")
     opcion = int(input("Selecciona una opcion (1-4):"))



     match opcion:
          case 1:
               ver_usuarios()
          case 2:
               insertar_usuario()
          case 3:
               actualizar_usuario()
          case 4:  
               eliminar_usuario()      
    
    


def main():
     print("==BIBLIOTECA UNIVERSITARIA==")
     print("menu de opciones:")
     print("1-. Libros:")
     print("2-. Usuarios")
     opcion = int(input("Escribe tu opcion: "))
     match opcion:
          case 1: menu_libros()
          case 2: menu_usuarios()
print("Saliendo del sistema de biblioteca universitaria ....")
if __name__ == "__main__":
    main()