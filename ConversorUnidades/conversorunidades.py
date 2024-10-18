import tkinter as tk
from tkinter import messagebox


TASA_CONVERSION = 535.25  # Esta es la tasa que se utilizará para convertir USD a CRC

class ConversorMoneda:
    def __init__(self, root):
        # Aquí se configura la ventana principal de la app
        self.root = root
        self.root.title("Conversor USD a CRC")  # Titulo de la ventana
        self.root.geometry("400x250")  # Tamaño de la ventana
        self.root.resizable(False, False)  # No se puede cambiar el tamaño de la ventana

        # Creamos los widgets que se van a utilizar
        self.crear_widgets()

        # Cuando se intenta cerrar la ventana, se pide una confirmación
        self.root.protocol("WM_DELETE_WINDOW", self.confirmar_salida)

    def crear_widgets(self):
        """ Crear y organizar los widgets en la ventana """
        # Este es el texto que aparece pidiendo al usuario que ingrese el monto
        self.instruccion = tk.Label(self.root, text="Ingrese monto en dólares (USD):")
        self.instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

        # Campo de entrada para que el usuario escriba el monto en USD
        self.entrada = tk.Entry(self.root)
        self.entrada.grid(row=1, column=0, padx=10, pady=10)  

        # Botón que al presionarlo hace la conversión
        self.boton_convertir = tk.Button(self.root, text="Convertir", command=self.convertir, bg="lightblue", fg="black")
        self.boton_convertir.grid(row=1, column=1, padx=10, pady=(20, 10))  # se coloca al lado del campo de entrada

        # Etiqueta para mostrar el resultado de la conversión
        self.resultado = tk.Label(self.root, text="", font=("Arial", 14), fg="green")
        self.resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Aquí se muestra el resultado

        # Botón para limpiar el campo de entrada y el resultado
        self.boton_limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar, bg="lightgray", fg="black")
        self.boton_limpiar.grid(row=3, column=0, columnspan=2, padx=10, pady=(20, 10))  # se coloca al final

        # Se estabilizan los widgets para que se vean bien
        self.estilizar_widgets()

    def convertir(self):
        """ Convierte el monto de USD a CRC """
        valor_entrada = self.entrada.get()  # se obtiene el valor que ingresó el usuario
        if not valor_entrada:  # se verifica si el campo está vacío
            messagebox.showerror("Error", "El campo no puede estar vacío. Por favor, ingrese un monto.")
            return  # Si está vacío, se muestra  un error y no hacemos nada más
        try:
            monto_usd = float(valor_entrada)  # se intenta convertir el valor a float
            if monto_usd < 0:  # se verifica si el número es negativo
                raise ValueError  # Si es negativo, se lanza un error
            monto_crc = monto_usd * TASA_CONVERSION  # se hace la conversión
            self.resultado.config(text=f"{monto_crc:.2f} CRC")  # se muestra el resultado en la etiqueta
        except ValueError:  # Si hubo un error al convertir
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido y positivo.")  # se muestra el mensaje de error 

    def limpiar(self):
        """ Limpia los campos de entrada y resultado """
        self.entrada.delete(0, tk.END)  # Borra el texto del campo de entrada
        self.resultado.config(text="")  # Limpia el resultado mostrado

    def confirmar_salida(self):
        """ Confirma si el usuario desea cerrar la ventana """
        respuesta = messagebox.askyesno("Confirmar", "¿Seguro que quieres salir?")  # Preguntamos si realmente quiere salir
        if respuesta:  # Si la respuesta es sí
            self.root.destroy()  # se cierra la ventana

    def estilizar_widgets(self):
        """ Aplica estilo a todos los widgets de la ventana """
        self.root.configure(bg="white")  # se cambia el color de fondo de la ventana
        for widget in self.root.winfo_children():  # se itera sobre todos los widgets
            widget.config(font=("Arial", 12))  # se aplica un mismo tipo de letra

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()  # se crea la ventana principal
    app = ConversorMoneda(ventana)  # se inicia la clase que maneja la conversión
    ventana.mainloop()  # se ejecuta el bucle principal de la ventana
