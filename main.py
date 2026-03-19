from tkinter import *
from tkinter import ttk, font, messagebox

class App:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Promedio CAIU 2025")
        self.raiz.geometry("520x380")
        self.raiz.resizable(False, False)

        style = ttk.Style(self.raiz)
        style.configure("TFrame", background="#eef2ff")
        style.configure("TLabel", background="#eef2ff", font=("Segoe UI", 10))
        style.configure("Titulo.TLabel", font=("Segoe UI", 14, "bold"), foreground="#1f2937")
        style.configure("TButton", font=("Segoe UI", 10, "bold"))

        cursos = ["Filosofía", "Fragata", "Lingüística", "Herramientas tecnológicas"]
        self.vars = [StringVar() for _ in cursos]
        self.course_avg_vars = [StringVar(value="0.00") for _ in cursos]
        self.result_var = StringVar(value="0.00")

        cont = ttk.Frame(self.raiz, padding=14)
        cont.grid(row=0, column=0, sticky="nsew")

        ttk.Label(cont, text="Promedio de notas CAIU 2025", style="Titulo.TLabel").grid(row=0, column=0, columnspan=4, pady=(0, 8), sticky="w")
        ttk.Label(cont, text="Ingrese 4 notas separadas por comas por curso (ej: 18, 17, 19, 16)", font=("Segoe UI", 9), foreground="#334155").grid(row=1, column=0, columnspan=4, pady=(0, 10), sticky="w")

        for i, curso in enumerate(cursos):
            ttk.Label(cont, text=f"{curso}:").grid(row=2+i, column=0, sticky="e", padx=(0, 8), pady=4)
            ttk.Entry(cont, textvariable=self.vars[i], width=28).grid(row=2+i, column=1, sticky="w", pady=4)
            ttk.Label(cont, text="Promedio:").grid(row=2+i, column=2, sticky="e", padx=(10,4))
            ttk.Label(cont, textvariable=self.course_avg_vars[i], font=("Segoe UI",10,"bold"), foreground="#0f4c81").grid(row=2+i, column=3, sticky="w")

        btn_frame = ttk.Frame(cont)
        btn_frame.grid(row=6, column=0, columnspan=3, pady=12)
        ttk.Button(btn_frame, text="Calcular promedio", command=self.calcular).grid(row=0, column=0, padx=4)
        ttk.Button(btn_frame, text="Limpiar", command=self.borrar).grid(row=0, column=1, padx=4)
        ttk.Button(btn_frame, text="Salir", command=self.raiz.destroy).grid(row=0, column=2, padx=4)

        ttk.Label(cont, text="Promedio general:", font=("Segoe UI", 10, "bold")).grid(row=7, column=0, sticky="e", pady=(10,0))
        ttk.Label(cont, textvariable=self.result_var, font=("Segoe UI", 11, "bold"), foreground="#0f4c81").grid(row=7, column=1, sticky="w", columnspan=2, pady=(10,0))

        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)

    def calcular(self):
        promedios = []
        for idx, var in enumerate(self.vars):
            texto = var.get().strip()
            if texto == "":
                messagebox.showerror("Error", "Debes ingresar 4 notas por cada curso.")
                return

            partes = [x.strip() for x in texto.split(",") if x.strip() != ""]
            if len(partes) != 4:
                messagebox.showerror("Error", f"Curso {idx+1}: ingresa exactamente 4 notas separadas por comas.")
                return

            try:
                notas = [float(x) for x in partes]
            except ValueError:
                messagebox.showerror("Error", f"Curso {idx+1}: ingresa solo números.")
                return

            if any(n < 0 or n > 20 for n in notas):
                messagebox.showerror("Error", f"Curso {idx+1}: notas deben estar entre 0 y 20.")
                return

            avg = round(sum(notas) / 4, 2)
            self.course_avg_vars[idx].set(f"{avg:.2f}")
            promedios.append(avg)

        promedio_general = round(sum(promedios) / len(promedios), 2)
        self.result_var.set(f"{promedio_general:.2f}")

    def borrar(self):
        for v in self.vars:
            v.set("")
        for v in self.course_avg_vars:
            v.set("0.00")
        self.result_var.set("0.00")

if __name__ == "__main__":
    App().raiz.mainloop()