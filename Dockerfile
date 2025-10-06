# Usa una imagen oficial de Python como imagen base
FROM python:3.11-slim

# Instala las dependencias del sistema que WeasyPrint necesita
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libcairo2 \
    libgdk-pixbuf-xlib-2.0-0 \
    libpangoft2-1.0-0 \
    --no-install-recommends

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 5000 para que la aplicación sea accesible
EXPOSE 5000

# Define el comando para ejecutar la aplicación con Gunicorn
# Escuchará en todas las interfaces de red en el puerto 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]