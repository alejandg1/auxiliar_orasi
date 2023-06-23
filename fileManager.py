import os
import shutil

# directorio actual
nowDir = os.getcwd()
# directorio del usuario
user_dir = os.path.expanduser("~")
# funciones
# TODO quiza tambien borre esto
# directorio raiz del sistema
# rootDir = os.path.abspath("/")
# TODO borrar pq no lo usa el programa----     directorio de documentos según el lenguaje del sistema
""" documentos_path = ""
sys_lang = locale.setlocale(0)
if ("es" in sys_lang):
    documentos_path = os.path.join(os.path.expanduser("~"), "Documentos/")
elif ("en" in sys_lang):
    documentos_path = os.path.join(os.path.expanduser("~"), "Documents/")
else: """
"""     print(f"Idioma no soportado {sys_lang}")
print(documentos_path)

 """


def copyfiles():
    path = input("ingrese la ruta de el o los archivos a copiar>> ")
    dirdestino = input(
        "ingrese la ruta en la que quiere copiar los archivos>>  ")
    # comprobar si existen las rutas ingresadas
    if (os.path.exists(path)):
        # evaluar la ruta pertenece a un directorio o a un archivo
        if (os.path.isdir(path)):
            # iterar entre los archivos existentes en el directorio
            for file in os.listdir(path):
                # comprobar que es un archivo valido
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path):
                    # copiar archivos
                    shutil.copy(file_path, dirdestino)
        else:
            if (os.path.exists(dirdestino)):
                # copia archivos o directorio completo ingresado
                shutil.copy(path, dirdestino)
                print("archivos copiados")
            else:
                print("el directorio de destino no existe o fué mal escrito")

    else:
        print("el directorio de origen no existe o fué mal escrito")


def ls(path):
    return [file.name for file in os.scandir(path) if file.is_file()]


def searchfiles():
    count = 0
    search = input("que archivo desea buscar?  ")
    ruta = input("desea buscarlo en una ruta especifica o en todo el sistema? si no especifica una ruta se realizará la busqueda en todos los ficheros del usuario   ")
    # evaluar si la ruta ingresada no es nula
    if (ruta != ""):
        path = ruta
    else:
        # si la ruta ingresada no es valida realiza la bisqueda en el directorio del usuario
        path = user_dir
    # comprobar si la ruta ingresada es valida
    if (os.path.exists(path)):
        print("buscando...")
        # recorre archivos y directorios dentro de la ruta parametro
        for raiz, dirs, files in os.walk(path):
            for file in files:
                if search in file:
                    count += 1
                    # imprime ruta de los archivos que coincidan con la busqueda
                    print(
                        "------------------------------------------------------------")
                    print(os.path.join(raiz, file))
                    pass
                else:
                    pass
        print(f"coincidencias encontradas = {count}")
    else:
        print("ruta no encontrada")


# rutas de subcarpetas
music_path = os.getcwd()+"/music/"
documents_path = os.getcwd()+"/documents/"
images_path = os.getcwd()+"/images/"


def orgfiles():
    # arreglos para especificar las extenciones o formatos de cata tipo de archivo
    music_format = []
    document_format = []
    image_format = []
    ruta = input("ingrese la ruta en la que desea ordenar archivos>>  ")
    if os.path.exists(ruta):
        print("organizando archivos")
        # obtiene los archivos que se encuentran dentro de una ruta ingresada
        archivos = [arch.name for arch in os.scandir(ruta) if arch.is_file()]
        # comprobar existencia de las carpetas
        #! moviendo archivos de musica
        if (os.path.exists(music_path)):
            for archivo in archivos:
                # comprobar si la extensión del archivo está en el arreglo
                nombre, ext = os.path.splitext(archivo)
                if ext in music_format:
                    shutil.move(os.path.join(
                        ruta, archivo), music_path)
        else:
            # crear carpeta musica en el directorio ingresado
            os.mkdir(music_path)
        #! moviendo archivos de documentos
        if (os.path.exists(documents_path)):
            for archivo in archivos:
                # comprobar si la extensión del archivo está en el arreglo
                nombre, ext = os.path.splitext(archivo)
                if ext in document_format:
                    shutil.move(os.path.join(
                        ruta, archivo), documents_path)
        else:
            os.mkdir(documents_path)
        #! moviendo archivos de imagenes
        if (os.path.exists(images_path)):
            for archivo in archivos:
                # comprobar si la extensión del archivo está en el arreglo
                nombre, ext = os.path.splitext(archivo)
                if ext in image_format:
                    shutil.move(os.path.join(
                        ruta, archivo), images_path)
        else:
            os.mkdir(images_path)
        print("-----------------------------")
        print("archivos organizados")
    else:
        print("ruta ingresada no valida o mal escrita")


def menu():
    opcion = "1"
    while opcion != "0":
        print("""1) copiar archivos de un directorio a otro
                 2) busqueda de archivos
                 3) organizar archivos de musica, imagenes y documentos """)
        opcion = input("ingrese el número de la acción que desea realizar>> ")
        if opcion == "1":
            copyfiles()
        elif (opcion == "2"):
            searchfiles()
        elif (opcion == "3"):
            orgfiles()
        elif (opcion == "0"):
            break
        else:
            print("opción no valida ")


menu()
