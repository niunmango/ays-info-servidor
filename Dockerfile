# Imagen base: Python 3.12-slim (más reciente y segura)
FROM python:3.12-slim-bookworm

# Etiquetas de versión para mejor trazabilidad
LABEL maintainer="Hermes Agent"
LABEL version="1.0.0"
LABEL description="Aplicación Flask para mostrar información del servidor"

# Variables de entorno
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (solo lo necesario)
RUN apt-get update && \
    apt-get install -y --no-install-recommends procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar y instalar dependencias de Python primero (mejor cacheo)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear usuario no root para seguridad
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Exponer puerto
EXPOSE 5000

# Health check para el contenedor
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Ejecutar con gunicorn (más adecuado para producción que Flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]