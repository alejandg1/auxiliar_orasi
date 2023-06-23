import os
import shutil

# directorio actual
nowDir = os.getcwd()
# directorio del usuario
user_dir = os.path.expanduser("~")
# funciones

# borra contenido de la terminal


def clear():
    os.system("cls" if os.name == "nt" else "clear")


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
                    print("archivos copiados")
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


def orgfiles():
    # arreglos para especificar las extenciones o formatos de cata tipo de archivo
    music_format = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    document_format = ['.pdf', '.docx', '.xlsx', '.pptx', '.txt']
    image_format = ['.jpg', '.png', '.gif', '.bmp', '.svg']
    ruta = input("ingrese la ruta en la que desea ordenar archivos>>  ")
    if os.path.exists(ruta):
        # definir rutas de las carpetas dentro del directorio ingresado por usuario
        music_path = ruta+"/musica/"
        documents_path = ruta+"/documentos/"
        images_path = ruta+"/imagenes/"
        print("organizando archivos")
        # obtiene los archivos que se encuentran dentro de una ruta ingresada
        archivos = [arch.name for arch in os.scandir(
            ruta) if arch.is_file()]
        # comprobar existencia de las carpetas
        if (not (os.path.exists(music_path))):
            # crear carpeta musica en el directorio ingresado
            os.mkdir(music_path)
        if (not (os.path.exists(documents_path))):
            # crear carpeta musica en el directorio ingresado
            os.mkdir(documents_path)
        if (not (os.path.exists(images_path))):
            # crear carpeta musica en el directorio ingresado
            os.mkdir(images_path)
        #! moviendo archivos de imagenes
        for archivo in archivos:
            # comprobar si la extensión del archivo está en el arreglo
            nombre, ext = os.path.splitext(archivo)
            # ? moviendo archivos a sus respectivas carpetas
            if ext in image_format:
                shutil.move(os.path.join(
                    ruta, archivo), images_path)
            if ext in document_format:
                shutil.move(os.path.join(
                    ruta, archivo), documents_path)
            if ext in music_format:
                shutil.move(os.path.join(
                    ruta, archivo), music_path)
        print("-----------------------------")
        print("archivos organizados")
    else:
        print("ruta ingresada no valida o mal escrita")


def menu():
    try:
        while True:
            print("""
                    1) copiar archivos de un directorio a otro
                    2) busqueda de archivos
                    3) organizar archivos de musica, imagenes y documentos 
                    0) terminar ejecución
                    """)
            opcion = input(
                "ingrese el número de la acción que desea realizar>> ")
            if opcion == "1":
                clear()
                copyfiles()
            elif (opcion == "2"):
                clear()
                searchfiles()
            elif (opcion == "3"):
                clear()
                orgfiles()
            elif (opcion == "0"):
                clear()
                break
            else:
                print("opción no valida ")
    except:
        print("error del sistema")


menu()
