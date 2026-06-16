# 📊 AYS - Información del Servidor

## 🎯 Descripción

Esta aplicación Flask muestra información en tiempo real del servidor donde se ejecuta:
- Nombre del host
- Fecha y hora actual
- Espacio total y libre en disco
- Salida del comando `top` (actualización automática cada 4 segundos)

---

> **English version below**

# 📊 AYS - Server Information

## 🎯 Description

This Flask application shows real‑time information about the server where it runs:
- Host name
- Current date and time
- Total and free disk space
- Output of the `top` command (auto‑refresh every 4 seconds)

---

## 🚀 Instalación

### Opción 1: Con Podman (recomendado)
```bash
# Clonar el repositorio
git clone https://github.com/niunmango/ays-info-servidor.git
cd ays-info-servidor

# Construir la imagen
podman build -t ays-info-servidor .

# Ejecutar el contenedor
podman run -d -p 5000:5000 --name servidor-info ays-info-servidor
```

### Opción 2: Con Docker (alternativa)
```bash
# Clonar el repositorio
git clone https://github.com/niunmango/ays-info-servidor.git
cd ays-info-servidor

# Construir la imagen
docker build -t ays-info-servidor .

# Ejecutar el contenedor
docker run -d -p 5000:5000 --name servidor-info ays-info-servidor
```

### Opción 3: Sin contenedor (desarrollo local)
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

## 🐳 Uso de la imagen desde GitHub Container Registry

### Con Podman (recomendado)
```bash
# Descargar la imagen más reciente
podman pull ghcr.io/niunmango/ays-info-servidor:latest

# Ejecutar
podman run -d -p 5000:5000 ghcr.io/niunmango/ays-info-servidor:latest
```

### Con Docker (alternativa)
```bash
# Descargar la imagen más reciente
docker pull ghcr.io/niunmango/ays-info-servidor:latest

# Ejecutar
docker run -d -p 5000:5000 ghcr.io/niunmango/ays-info-servidor:latest
```

Luego acceder a: http://localhost:5000

## ⚙️ CI/CD con GitHub Actions

El pipeline se activa automáticamente en cada `push` a la rama `main`:
1. **Build**: Construye la imagen Docker.
2. **Push**: Publica la imagen a `ghcr.io`.
3. **Test**: Verifica que el contenedor funcione en el puerto 5000.

### Endpoint del pipeline

| Job   | Descripción |
|-------|-------------|
| `build` | Build and push the image to GHCR |
| `test`  | Validate the container responds on port 5000 |

## 📝 API Endpoints

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal con información del servidor |
| `/health`| Health check endpoint |
| `/top` | Salida cruda del comando `top` |

## 🛠️ Tecnologías utilizadas

- **Python 3.12**
- **Flask 3.x**
- **Gunicorn** (servidor WSGI para producción)
- **Docker**
- **GitHub Actions**

## 📋 Requisitos

- Docker (para usar la imagen construida)
- O Python 3.12+ con `pip` (para desarrollo local)

## 📜 Licencia

Este proyecto está licenciado bajo **GPLv3**.

---

**Proyecto creado por:** niunmango
**Modificado por:** Hermes Agent (CURZAS – UNCo)
