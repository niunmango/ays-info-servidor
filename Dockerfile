FROM python:3.11-slim-bookworm

WORKDIR /app

# Configurar variables de entorno para apt-get no interactivo
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema primero
RUN apt-get update && \
    apt-get install -y --no-install-recommends procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
