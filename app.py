"""
AYS - Información del Servidor
===============================
Aplicación Flask que muestra información básica del servidor (hostname,
fecha/hora, uso de disco, procesos activos, memoria).

Pensada como proyecto educativo para demostrar pipelines CI/CD con
GitHub Actions y despliegue de contenedores Docker.

Uso:
    - Desarrollo:  python app.py
    - Producción:  gunicorn --bind 0.0.0.0:5000 --workers 2 app:app
"""

import datetime
import logging
import os
import platform
import shutil
import subprocess
import psutil

from flask import Flask, render_template, Response

# ---------------------------------------------------------------------------
# Configuración de logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Aplicación Flask
# ---------------------------------------------------------------------------
app = Flask(__name__)

# Número de workers para gunicorn (por defecto 2, configurable vía env)
WORKERS = int(os.environ.get("GUNICORN_WORKERS", 2))


def get_disk_usage() -> tuple[str, str]:
    """Devuelve el espacio total y libre del disco en formato legible."""
    total, used, free = shutil.disk_usage("/")

    def fmt(size_bytes: int) -> str:
        for unit in ("B", "KB", "MB", "GB", "TB"):
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} PB"

    return fmt(total), fmt(free)


def get_memory_info() -> tuple[str, str]:
    """Devuelve la memoria total y disponible del servidor en formato legible."""
    mem = psutil.virtual_memory()
    total = mem.total
    available = mem.available

    def fmt(size_bytes: int) -> str:
        for unit in ("B", "KB", "MB", "GB", "TB"):
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} PB"

    return fmt(total), fmt(available)


def get_top_output() -> str:
    """Ejecuta `top` en modo batch y devuelve la salida como texto."""
    try:
        return subprocess.check_output(
            ["top", "-bn1", "-o", "%CPU"],
            stderr=subprocess.DEVNULL,
        ).decode()
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        logger.warning("No se pudo ejecutar top: %s", exc)
        return "(no disponible)"


@app.route("/")
def index():
    """Página principal con información del servidor."""
    hostname = platform.node()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_space, free_space = get_disk_usage()
    mem_total, mem_available = get_memory_info()
    top_output = get_top_output()

    logger.info("Página servida para host=%s", hostname)

    return render_template(
        "index.html",
        hostname=hostname,
        current_date=current_date,
        total_space=total_space,
        free_space=free_space,
        mem_total=mem_total,
        mem_available=mem_available,
        top_output=top_output,
    )


@app.route("/health")
def health():
    """Endpoint de salud para healthchecks del contenedor."""
    return "OK", 200


@app.route("/top")
def top():
    """Retorna la salida de `top` como texto plano (para actualización vía JS)."""
    output = get_top_output()
    return Response(output, mimetype="text/plain")


# ---------------------------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Solo para desarrollo; en producción usar gunicorn
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
