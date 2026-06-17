from database.conexion import Conexion
from models.libro import Libro
 
class LibroDAO:
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELEC * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registro in registro :
            libro = Libro(
                id = registro[0],
                titulo= registro[1],
                autor= registro[2],
                isbn= registro[3],
                disponible= registro[4],
            )
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros
    def insertar(self,libro):    
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO libro(titulo,autor,isbn,disponible)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible
        
        ))
        conexion.commit()
        cursor.close()
        conexion.close()
        
 