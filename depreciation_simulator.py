import tkinter as tk # Importar módulo Tkinter
from tkinter import ttk, messagebox # Importar módulos de Tkinter
from matplotlib.figure import Figure # Importar Figure de Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Importar backend de Tkinter para Matplotlib
import math # Importar módulo math para cálculos logarítmicos

# Clase principal de la aplicación
class AppDepreciacion:
    # Constructor de la clase
    def __init__(self, root):
        self.root = root
        self.root.title("ValorFuturo: Simulador de Depreciación Exponencial")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configurar estilo
        self.root.configure(bg='#f0f0f0')
        
        # Frame principal
        main_frame = tk.Frame(root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="ValorFuturo: Simulador de Depreciación Exponencial",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame de entrada de datos
        input_frame = tk.LabelFrame(
            main_frame,
            text="Parámetros de Depreciación",
            font=("Arial", 11, "bold"),
            bg='#f0f0f0',
            padx=20,
            pady=15
        )
        input_frame.grid(row=1, column=0, columnspan=2, sticky='ew', pady=(0, 10))
        
        # Valor Inicial
        tk.Label(
            input_frame,
            text="Valor Inicial ($):",
            font=("Arial", 10),
            bg='#f0f0f0'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.valor_inicial = tk.Entry(input_frame, font=("Arial", 10), width=20)
        self.valor_inicial.grid(row=0, column=1, padx=10, pady=5)
        self.valor_inicial.insert(0, "10000")
        
        # Tasa de Depreciación
        tk.Label(
            input_frame,
            text="Tasa de Depreciación Anual (%):",
            font=("Arial", 10),
            bg='#f0f0f0'
        ).grid(row=1, column=0, sticky='w', pady=5)
        
        self.tasa_depreciacion = tk.Entry(input_frame, font=("Arial", 10), width=20)
        self.tasa_depreciacion.grid(row=1, column=1, padx=10, pady=5)
        self.tasa_depreciacion.insert(0, "20")
        
        # Años a Proyectar
        tk.Label(
            input_frame,
            text="Años a Proyectar:",
            font=("Arial", 10),
            bg='#f0f0f0'
        ).grid(row=2, column=0, sticky='w', pady=5)
        
        self.anos_proyectar = tk.Entry(input_frame, font=("Arial", 10), width=20)
        self.anos_proyectar.grid(row=2, column=1, padx=10, pady=5)
        self.anos_proyectar.insert(0, "10")
        
        # Botón Calcular
        self.btn_calcular = tk.Button(
            input_frame,
            text="Calcular y Graficar",
            command=self.calcular_y_graficar,
            font=("Arial", 11, "bold"),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.btn_calcular.grid(row=3, column=0, columnspan=2, pady=15)
        
        # Separador
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=2, column=0, columnspan=2, sticky='ew', pady=10
        )
        
        # Frame para cálculo inverso (logarítmico)
        inverse_frame = tk.LabelFrame(
            main_frame,
            text="Cálculo Inverso: ¿Cuánto tiempo para alcanzar un valor?",
            font=("Arial", 11, "bold"),
            bg='#f0f0f0',
            padx=20,
            pady=15
        )
        inverse_frame.grid(row=3, column=0, columnspan=2, sticky='ew', pady=(0, 10))
        
        tk.Label(
            inverse_frame,
            text="Valor Futuro Deseado ($):",
            font=("Arial", 10),
            bg='#f0f0f0'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.valor_futuro = tk.Entry(inverse_frame, font=("Arial", 10), width=20)
        self.valor_futuro.grid(row=0, column=1, padx=10, pady=5)
        self.valor_futuro.insert(0, "5000")
        
        self.btn_calcular_tiempo = tk.Button(
            inverse_frame,
            text="Calcular Tiempo Necesario",
            command=self.calcular_tiempo,
            font=("Arial", 10, "bold"),
            bg='#2ecc71',
            fg='white',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.btn_calcular_tiempo.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.resultado_tiempo = tk.Label(
            inverse_frame,
            text="",
            font=("Arial", 10, "italic"),
            bg='#f0f0f0',
            fg='#27ae60'
        )
        self.resultado_tiempo.grid(row=2, column=0, columnspan=2)
        
        # Frame para el gráfico
        graph_frame = tk.Frame(main_frame, bg='white')
        graph_frame.grid(row=4, column=0, sticky='nsew', padx=(0, 5))
        
        # Crear figura de Matplotlib
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('Años', fontsize=10) # Eje X
        self.ax.set_ylabel('Valor ($)', fontsize=10) # Eje Y
        self.ax.set_title('Curva de Depreciación Exponencial', fontsize=12, fontweight='bold')
        self.ax.grid(True, alpha=0.3)
        
        # Canvas para el gráfico
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Frame para la tabla
        table_frame = tk.Frame(main_frame, bg='white')
        table_frame.grid(row=4, column=1, sticky='nsew', padx=(5, 0))
        
        # Crear Treeview para la tabla
        self.tree = ttk.Treeview(
            table_frame,
            columns=('Año', 'Valor'),
            show='headings',
            height=15
        )
        
        self.tree.heading('Año', text='Año')
        self.tree.heading('Valor', text='Valor ($)')
        
        self.tree.column('Año', width=80, anchor='center')
        self.tree.column('Valor', width=120, anchor='center')
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configurar peso de las columnas para que sean responsivas
        main_frame.columnconfigure(0, weight=2)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
    
    # Método para calcular y graficar la depreciación
    def calcular_y_graficar(self):
        try:
            # Obtener valores de entrada
            V0 = float(self.valor_inicial.get()) # Valor inicial
            r = float(self.tasa_depreciacion.get()) / 100  # Convertir porcentaje a decimal / Tasa de depreciación
            anos = int(self.anos_proyectar.get()) # Años a proyectar
            
            # Validaciones
            if V0 <= 0:
                messagebox.showerror("Error", "El valor inicial debe ser mayor que 0")
                return
            if r <= 0 or r >= 1:
                messagebox.showerror("Error", "La tasa debe estar entre 0% y 100%")
                return
            if anos <= 0:
                messagebox.showerror("Error", "Los años deben ser mayor que 0")
                return
            
            # Calcular valores usando la fórmula: V(t) = V₀ * (1 - r)^t
            anos_lista = list(range(anos + 1)) # Lista de años
            valores_lista = [] # Arreglo para almacenar los valores calculados
            
            for t in anos_lista:
                V_t = V0 * ((1 - r) ** t) # Fórmula de depreciación exponencial
                valores_lista.append(V_t) # Agregar valor calculado a la lista
            
            # Limpiar gráfico anterior
            self.ax.clear()
            self.ax.set_xlabel('Años', fontsize=10)
            self.ax.set_ylabel('Valor ($)', fontsize=10)
            self.ax.set_title('Curva de Depreciación Exponencial', fontsize=12, fontweight='bold')
            self.ax.grid(True, alpha=0.3)
            
            # Graficar
            self.ax.plot(anos_lista, valores_lista, 'b-o', linewidth=2, markersize=5, label='Valor del activo')
            self.ax.fill_between(anos_lista, valores_lista, alpha=0.3)
            self.ax.legend()
            
            # Formato del eje Y con separador de miles
            self.ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
            
            self.canvas.draw()
            
            # Actualizar tabla
            # Limpiar tabla anterior
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Llenar tabla con nuevos datos
            for ano, valor in zip(anos_lista, valores_lista): # Recorrer años y valores
                self.tree.insert('', 'end', values=(ano, f'${valor:,.0f}')) # Insertar datos en la tabla
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

    # Método para calcular el tiempo necesario para alcanzar un valor futuro dado
    def calcular_tiempo(self):
        try:
            # Obtener valores
            V0 = float(self.valor_inicial.get()) # Valor inicial
            r = float(self.tasa_depreciacion.get()) / 100 # Convertir porcentaje a decimal / Tasa de depreciación
            V_futuro = float(self.valor_futuro.get()) # Valor futuro deseado
            
            # Validaciones
            if V0 <= 0 or V_futuro <= 0:
                messagebox.showerror("Error", "Los valores deben ser mayores que 0")
                return
            if V_futuro >= V0:
                messagebox.showerror("Error", "El valor futuro debe ser menor que el valor inicial")
                return
            if r <= 0 or r >= 1:
                messagebox.showerror("Error", "La tasa debe estar entre 0% y 100%")
                return
            
            # Calcular tiempo usando logaritmos: t = log(V(t)/V₀) / log(1-r)
            t = math.log(V_futuro / V0) / math.log(1 - r) # Tiempo necesario
            
            # Mostrar resultado
            self.resultado_tiempo.config(
                text=f"El activo alcanzará ${V_futuro:,.0f} en {t:.2f} años" 
            )
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")


# Importar pyplot para el formatter
import matplotlib.pyplot as plt

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AppDepreciacion(root)
    root.mainloop()
