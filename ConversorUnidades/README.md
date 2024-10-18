# Conversor de Moneda USD a CRC

**Propietario:** Tifanny Muñoz

## Descripción

# Instrucciones de Uso

Ejecutar el Script:
- Abrir la terminal.
- Navegar hasta el directorio donde se encuentra el script.

Interacción con la Aplicación:
- Al abrir la aplicación, se verá un campo donde se puede ingresar el monto en dólares (USD).
- Ingrese la cantidad que desea convertir y presione el botón Convertir. 
- Si quiere limpiar el campo de entrada y el resultado mostrado, simplemente presione el botón Limpiar.
- Si decide cerrar la aplicación, aparecerá una ventana emergente preguntándo si realmente desea salir. Puede confirmar o cancelar esta acción.

# Explicación de la Implementación del Código

El código está diseñado como una aplicación gráfica utilizando la biblioteca Tkinter de Python. 
- Tasa de Conversión: Se fija un valor al cual se le da el nombre de tasa de conversiones, utilizada para convertir de dólares (USD) a colones (CRC). 
- Clase ConversorMoneda: La lógica de la aplicación se encapsula en la clase ConversorMoneda, que contiene varios métodos: 
1- Método __init__: Este es el constructor de la clase que inicializa la ventana principal. Configura el título, tamaño y comportamiento de la ventana.
2- Método crear_widgets: quí se crean y organizan todos los widgets de la interfaz gráfica, como etiquetas, campos de entrada y botones. Utiliza el método grid() para colocarlos de manera estructurada.
3- Método convertir: Este método se activa al presionar el botón Convertir. Primero, verifica si el campo de entrada está vacío o si el valor ingresado es negativo o no numérico. Si todo es correcto, realiza la conversión y muestra el resultado.
4- Método limpiar: Limpia el campo de entrada y el resultado mostrado en la etiqueta.
5- Método confirmar_salida: Este método se llama al intentar cerrar la ventana, mostrando una ventana emergente que pide confirmación para salir.
6- Método estilizar_widgets: Aplica un estilo uniforme a todos los widgets de la ventana, como cambiar el color de fondo y la fuente.
- Ejecución de la Aplicación: El bloque final del código ejecuta la aplicación, Aquí se crea la ventana principal y se inicia el bucle principal de Tkinter, que mantiene la aplicación en ejecución y esperando interacciones del usuario.

# Fotos de la implementación: 
![Conversión regular con resultado esperado](https://github.com/user-attachments/assets/0e4e1a54-13ec-4387-a378-8050afaff75b)
![Valor inválido ingresado para la conversión con el mensaje de error](https://github.com/user-attachments/assets/b9231e0d-1989-47e2-ac13-17956be97b65)
![Ventana emergente al cerrar la ventana](https://github.com/user-attachments/assets/d2b549ee-1225-4249-9b07-fad79df41c69)







