# Documentación del Programa de Modificación de Metadatos de Imágenes

Este documento proporciona una descripción y documentación del código Python proporcionado. El código permite la modificación de metadatos en imágenes seleccionadas, incluyendo el asunto, etiquetas, latitud y longitud de coordenadas GPS. Además, ofrece la opción de descargar las imágenes modificadas.

## Resumen

El código realiza las siguientes acciones:

1. Permite al usuario seleccionar una o varias imágenes.
2. Modifica los metadatos de las imágenes seleccionadas, incluyendo el asunto, etiquetas, latitud y longitud, utilizando la herramienta ExifTool.
3. Ofrece la posibilidad de descargar las imágenes modificadas con los nuevos metadatos.

## Uso

Para utilizar este código, asegúrese de tener las siguientes configuraciones previas:

- Tener instalada la herramienta ExifTool y proporcionar la ruta al ejecutable de ExifTool en la variable `exiftool_path`.

A continuación, describimos las principales funciones y componentes del programa:

### Componentes de la Interfaz de Usuario

- **Asunto**: Permite al usuario ingresar un nuevo asunto para las imágenes seleccionadas.
- **Etiquetas (separadas por comas)**: Permite al usuario ingresar nuevas etiquetas para las imágenes seleccionadas.
- **Latitud**: Permite al usuario ingresar una nueva latitud para las coordenadas GPS de las imágenes seleccionadas.
- **Longitud**: Permite al usuario ingresar una nueva longitud para las coordenadas GPS de las imágenes seleccionadas.
- **Seleccionar Imágenes**: Abre una ventana de selección de archivos para que el usuario elija las imágenes que desea modificar.
- **Modificar Metadatos**: Aplica las modificaciones de metadatos a las imágenes seleccionadas.
- **Descargar Imágenes**: Permite al usuario descargar las imágenes modificadas con los nuevos metadatos.

### Flujo del Programa

1. El usuario selecciona una o varias imágenes haciendo clic en el botón "Seleccionar Imágenes". Se almacenan las rutas de las imágenes seleccionadas en la lista `selected_image_paths`.

2. El usuario ingresa los nuevos valores de asunto, etiquetas, latitud y longitud en los campos correspondientes de la interfaz de usuario.

3. Al hacer clic en el botón "Modificar Metadatos", se aplican las modificaciones de metadatos a todas las imágenes seleccionadas utilizando la herramienta ExifTool. Se actualizan los metadatos de asunto, etiquetas, latitud y longitud.

4. Después de modificar los metadatos, el botón "Descargar Imágenes" se habilita para permitir al usuario descargar las imágenes modificadas. Al hacer clic en este botón, se abre un cuadro de diálogo para seleccionar la ubicación de descarga y se guardan las imágenes modificadas con los nuevos metadatos.

## Gestión de Errores

El programa gestiona posibles errores de la siguiente manera:

- Si no se selecciona ninguna imagen y se intenta modificar metadatos, se muestra un mensaje de error.
- Si se produce un error al modificar los metadatos de una imagen, se muestra un mensaje de error específico para esa imagen.

## Conclusiones

Este programa proporciona una forma fácil de modificar los metadatos de imágenes seleccionadas, lo que puede ser útil en situaciones donde es necesario actualizar información de asunto, etiquetas o coordenadas GPS en lotes de imágenes. Además, permite descargar las imágenes modificadas para su uso posterior.

---

*Nota: Este documento es una documentación general del código proporcionado. Para detalles específicos sobre su implementación y configuración, se recomienda consultar directamente el código fuente y los comentarios incluidos en él.*
