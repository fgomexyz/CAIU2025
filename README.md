# Promedio CAIU

Aplicación de escritorio con Tkinter para calcular promedios de notas del CAIU.

## 📌 Qué hace

- Permite ingresar 4 notas por curso (Filosofía, Fragata, Lingüística, Herramientas tecnológicas).
- Valida notas en rango 0..20.
- Calcula promedio de cada curso y promedio general.
- Muestra resultados en la interfaz gráfica.

## 🚀 Archivos clave

- `main.py`: GUI principal.
- `promedio_utils.py`: funciones de lógica (parseo y cálculo).
- `test_promedio_utils.py`: pruebas unitarias con pytest.
- `dist/PromedioCAIU.exe`: ejecutable empaquetado (generado con PyInstaller).

## 🧭 Uso local

1. Activar entorno virtual:
   ```powershell
   .\.venv\Scripts\activate
   ```
2. Ejecutar app:
   ```powershell
   python main.py
   ```
3. Ingresar notas en cada curso separadas por comas. Ejemplo:
   `18, 17.5, 16, 19`
4. Presionar `Calcular promedio`.

## ✅ Pruebas automatizadas

1. Instalar dependencias (si no están):
   ```powershell
   python -m pip install -r requirements.txt
   ```
   Si no existe requirements, solo:
   ```powershell
   python -m pip install pytest
   ```
2. Ejecutar tests:
   ```powershell
   python -m pytest -q
   ```

## 📦 Empaquetado en exe

Ya está generado en `dist/PromedioCAIU.exe`.

Para volver a construir:

```powershell
python -m PyInstaller --onefile --windowed --name "PromedioCAIU" main.py
```

## 🧩 Estructura recomendada

- `main.py`: interfaz y eventos.
- `promedio_utils.py`: lógica independiente para tests.
- `test_promedio_utils.py`: pruebas.
- `.github/workflows/python-app.yml`: CI en GitHub Actions.

## 💡 Mejores prácticas

- Mantener la lógica separada de la GUI para poder testear.
- Usar validaciones de datos (rango 0..20, 4 notas exactas).
- Empaquetar y distribuir `dist/PromedioCAIU.exe` para usuarios sin Python.

---

`Promedio CAIU` - Proyecto de cálculo de promedio para CAIU 2025.
