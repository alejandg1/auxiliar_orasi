import os
import shutil
import locale

# directorio actual
nowDir=od.getcwd()
# directorio raiz del sistema
rootDir=os.path.abspath("/")
# directorio del usuario
directorio_usuario = os.path.expanduser("~")
# directorio de documentos según el lenguaje del sistema
documentos_path=""
sys_lang=locale.getdefaultlocale()[0]
if("es" in sys_lang):
    documentos_path=os.path.join(os.path.expanduser("~"),"Documentos/")
elif("en" in sys_lang):
    documentos_path=os.path.join(os.path.expanduser("~"),"Documents/")
else:
    print(f"Idioma no soportado {sys_lang}")
print(documentos_path)


# funciones
def copyFiles(dir,dirdestino):
    # comprobar si existen las rutas ingresadas
    if (os.path.exist(dir)):
        if (os.path.exist(dirdestino)):
        # copia archivos o directorio completo ingresado
            shutil.copy(r'{dir}',r'{dirdestino}')
        else:
            print("el directorio de destino no existe")
            
    else:
        print("el directorio de origen no existe")


def searchFiles(search,ruta=rootDir):
    # recorre archivos y directorios dentro de la ruta parametro
    for raiz,dirs,files in os.walk(ruta):
        for file in files:
            if search in file:
            # imprime ruta de los archivos que coincidan con la busqueda
                print(os.path.join(raiz,file))


# rutas de subcarpetas
music_path=documentos_path+"music/"
documents_path=documentos_path+"documents/"
images_path=documentos_path+"images/"
def orgFiles(ruta=nowDir):
    # obtiene los archivos que se encuentran dentro de una ruta ingresada
    archivos=[arch.name for arch in os.scandir(ruta) if arch.is_file(())]
    if (os.path.exist(music_path)):
        ## falta ordenar los archivos esos en las carpetas  y crear las carpetas is es q no exixsten
        pass
    if (os.path.exist(documents_path)):
        pass
    if (os.path.exist(images_path)):
        pass



