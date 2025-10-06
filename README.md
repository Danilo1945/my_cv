# CV Interactivo

Este es un proyecto simple de una aplicación web para mostrar un currículum vitae (CV) de forma interactiva. La aplicación está construida con Python y Flask, y permite descargar el CV en formato PDF.

## Características

- Muestra un CV interactivo en una página web.
- Permite descargar el CV en formato PDF.
- Diseño moderno y limpio utilizando Tailwind CSS.

## Tecnologías Utilizadas

- **Backend:** Python, Flask
- **Generación de PDF:** WeasyPrint
- **Frontend:** HTML, Tailwind CSS
- **Contenerización:** Docker, Docker Compose

## Cómo Ejecutar el Proyecto

### Ejecución Local (sin Docker)

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**
    Asegúrate de tener `pip` instalado.
    ```bash
    pip install -r requirements.txt
    ```
    También necesitarás instalar las dependencias de WeasyPrint en tu sistema. En sistemas Debian/Ubuntu, puedes hacerlo con:
    ```bash
    sudo apt-get install libpango-1.0-0
    ```

4.  **Configurar la aplicación Flask:**
    ```bash
    export FLASK_APP=app.py
    ```

5.  **Ejecutar la aplicación:**
    ```bash
    flask run
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000`.

### Ejecución con Docker

Si tienes Docker y Docker Compose instalados, puedes ejecutar el proyecto fácilmente con un solo comando:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2.  **Ejecutar con Docker Compose:**
    ```bash
    docker-compose up
    ```
    La aplicación estará disponible en `http://localhost:5000`.

