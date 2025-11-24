Simulador de Depreciación de Activos

Repositorio: RuttenAsphodel/valorfuturo

Descripción: Este proyecto permite calcular la depreciación de activos a lo largo del tiempo mediante distintos métodos (según se defina) — ideal para análisis contable o financiero.

Contenido del repositorio

depreciation_simulator.py — Script principal que contiene la lógica del simulador.

requirements.txt — Dependencias necesarias para ejecutar el proyecto.

Implementacion Simulador Depreciacion.docx — Documento de implementación/planificación (puedes verlo para detalles de diseño).

README.md — Este archivo.

Tecnologías usadas

Python (100% del código). 
GitHub

Bibliotecas listadas en requirements.txt (por ejemplo: pandas, numpy — asegúrate de revisar ese archivo).

Instalación / Preparación del entorno

Clona este repositorio:

git clone https://github.com/RuttenAsphodel/valorfuturo.git
cd valorfuturo


(Opcional) Crea un entorno virtual para aislar dependencias:

python3 -m venv venv
source venv/bin/activate   # en Linux/Mac
venv\Scripts\activate      # en Windows


Instala las dependencias:

pip install -r requirements.txt


Verifica que la instalación fue correcta ejecutando el script principal.

Uso

Ejecuta el simulador con:

python depreciation_simulator.py


Dentro del script puedes modificar entradas como: valor inicial del activo, vida útil, método de depreciación, etc. Asegúrate de revisar los comentarios del código para entender cómo ajustar los parámetros.

Configuración (parámetros principales)

Aquí algunos parámetros clave que puedes modificar en depreciation_simulator.py:

Valor inicial del activo.

Fecha de adquisición.

Vida útil (años).

Método de depreciación (lineal, decreciente, etc).

Valor residual (si aplica).

Periodicidad de cálculo (anual, mensual, etc).

(Revisa el código para ver cómo se implementan esos métodos concretos).

Ejemplos de salida

No se han incluido capturas de pantalla en este README. Puedes agregar ejemplos de salida aquí para facilitar el uso por otros usuarios.

Contribuciones

Si deseas contribuir:

Haz un fork del repositorio.

Crea una nueva branch para tu feature/fix.

Haz commit de tus cambios con mensajes claros.

Envía un pull request describiendo qué mejoras añadiste.

Licencia

(Si no tienes aún una licencia, considera agregar una — por ejemplo MIT, Apache 2.0, etc.)
Por defecto, este proyecto no especifica una licencia. Asegúrate de definirla si lo vas a hacer público.

Contacto / Autor

Proyecto creado por Rutten Asphodel.
Para dudas, puedes abrir un Issue en el repositorio o contactarme vía GitHub.
