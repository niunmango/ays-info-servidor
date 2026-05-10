# 📊 AYS - Información del Servidor

Proyecto educativo para demostrar pipelines CI/CD con **GitHub Actions** y despliegue de contenedores **Podman** (predominante) y **Docker** (alternativa).

## 🎯 Descripción

Esta aplicación Flask muestra información en tiempo real del servidor donde se ejecuta:
- Nombre del host
- Fecha y hora actual
- Espacio total y libre en disco
- Salida del comando `top` (actualización automática cada 4 segundos)

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

El pipeline se activa automáticamente con cada `push` a la rama `main`:

1. **Build**: Construye la imagen Docker
2. **Push**: Publica la imagen en `ghcr.io`
3. **Test**: Verifica que el contenedor funcione correctamente

### Endpoints del pipeline

| Job | Descripción |
|-----|-------------|
| `build` | Construye y sube la imagen a GHCR |
| `test` | Valida que el contenedor responda en puerto 5000 |

## 📝 Endpoints de la API

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal con información del servidor |
| `/health` | Endpoint de salud para healthchecks |
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

Este proyecto está licenciado bajo la **GPLv3**.

---

**Proyecto creado por:** niunmango  
**Modificado por:** Hermes Agent (asistente del CURZAS - UNCo)