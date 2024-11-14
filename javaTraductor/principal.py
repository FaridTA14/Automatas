from antlr4 import *
from javaTraductorLexer import javaTraductorLexer
from javaTraductorParser import javaTraductorParser
from generadorJava import generadorJava

def main():
    # Leer el archivo de entrada
    input_file = input("Ingrese el nombre del archivo Py a traducir: ")
    
    try:
        with open(input_file, 'r') as file:
            py_code = file.read()
            
        # Crear el input stream con el código Python
        input_stream = InputStream(py_code)
        
        # Crear lexer y parser
        lexer = javaTraductorLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = javaTraductorParser(token_stream)
        
        # Generar árbol de parseo
        tree = parser.program()
        
        # Crear walker para recorrer el árbol
        walker = ParseTreeWalker()
        
        # # Procesar el árbol con el listener y generar código Java
        listener = generadorJava()
        walker.walk(listener, tree)
        
        # Obtener el código Java generado
        java_code = listener.getJavaCode()
        
        # Crear el archivo Java
        output_file = input_file.replace('.txt', '.java').replace('.py', '.java')
        with open(output_file, 'w') as file:
            file.write(java_code)
            
        # Imprimir el código Java generado en la consola
        print("\nCódigo Java generado:")
        print("----------------------")
        print(java_code)
        print("\nArchivo Java generado:", output_file)
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")

if __name__ == '__main__':
    main()
