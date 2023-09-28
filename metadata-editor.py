import tkinter as tk
from tkinter import filedialog, Label, Entry, Button
import subprocess
import shutil

# Ruta al ejecutable de ExifTool
exiftool_path = "C:/Users/USER/Downloads/exiftool-12.67/exiftool.exe"

selected_image_paths = []  # Almacena las rutas de las imágenes seleccionadas
downloaded_image_names = []  # Almacena los nombres de las imágenes descargadas

def open_files():
    global selected_image_paths
    selected_image_paths = filedialog.askopenfilenames()
    if selected_image_paths:
        print("Imágenes seleccionadas:", selected_image_paths)

def modify_metadata():
    nuevo_asunto = asunto_entry.get()
    nuevas_etiquetas = etiquetas_entry.get()
    nueva_latitud = latitud_entry.get()
    nueva_longitud = longitud_entry.get()
    
    # Verificar si se proporcionaron valores válidos para los archivos de imagen
    if not selected_image_paths:
        print("Error: No se han seleccionado imágenes.")
        return
    
    for selected_image_path in selected_image_paths:
        # Modificar metadatos con ExifTool
        command = [
            exiftool_path,
            '-ImageDescription=' + nuevo_asunto,
            '-Keywords=' + nuevas_etiquetas,
            '-GPSLatitude=' + nueva_latitud,
            '-GPSLongitude=' + nueva_longitud,
            '-overwrite_original',  # Evita la creación de archivos de respaldo
            selected_image_path  # La imagen seleccionada
        ]

        try:
            subprocess.run(command, check=True)
            print(f"Metadatos modificados con éxito para: {selected_image_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error al modificar los metadatos para {selected_image_path}: {e}")

    enable_download_button()

def enable_download_button():
    download_button.config(state=tk.NORMAL)

def download_images():
    global downloaded_image_names
    if not selected_image_paths:
        print("Error: No se han seleccionado imágenes.")
        return

    for selected_image_path in selected_image_paths:
        downloaded_image_name = filedialog.asksaveasfilename(defaultextension=".jpg")
        if downloaded_image_name:
            try:
                # Copia la imagen seleccionada directamente al archivo descargado
                shutil.copy(selected_image_path, downloaded_image_name)

                # Obtén el nombre del archivo sin la extensión
                file_name_without_extension = downloaded_image_name.rsplit(".", 1)[0]

                # Obtén solo el nombre del archivo sin la ruta
                file_name = file_name_without_extension.split("/")[-1]

                # Cambiar el metadato 'Título' al nombre del archivo sin la extensión
                command = [
                    exiftool_path,
                    '-Title=' + file_name,
                    '-overwrite_original',  # Evita la creación de archivos de respaldo
                    downloaded_image_name  # El archivo descargado
                ]

                subprocess.run(command, check=True)

                print(f"Imagen descargada con éxito como: {downloaded_image_name}")
            except (shutil.Error, subprocess.CalledProcessError) as e:
                print(f"Error al copiar o modificar la imagen {selected_image_path}: {e}")


window = tk.Tk()
window.title("Modificar Metadatos de Imágenes")

asunto_label = Label(window, text="Asunto:")
asunto_label.pack()

asunto_entry = Entry(window)
asunto_entry.pack()

etiquetas_label = Label(window, text="Etiquetas (separadas por comas):")
etiquetas_label.pack()

etiquetas_entry = Entry(window)
etiquetas_entry.pack()

latitud_label = Label(window, text="Latitud:")
latitud_label.pack()

latitud_entry = Entry(window)
latitud_entry.pack()

longitud_label = Label(window, text="Longitud:")
longitud_label.pack()

longitud_entry = Entry(window)
longitud_entry.pack()

open_button = Button(window, text="Seleccionar Imágenes", command=open_files)
open_button.pack()

modify_button = Button(window, text="Modificar Metadatos", command=modify_metadata)
modify_button.pack()

download_button = Button(window, text="Descargar Imágenes", command=download_images, state=tk.DISABLED)
download_button.pack()

window.mainloop()
