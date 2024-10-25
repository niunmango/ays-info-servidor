
**Materia: Automatización y Scripting**

**Proyecto:
   Página en Python con Flask con información del servidor**

**Descripción:**

Este proyecto consiste en crear una página básica que muestre información del servidor en el que se ejecuta. La información que se muestra incluye el nombre del servidor, fecha y hora, espacio total de disco y libre.

**Instalación:**

1. Clonar el repositorio desde GitHub:

```
git clone https://github.com/niunmango/ays-info-servidor.git
```

2. Navegar a la carpeta del proyecto:

```
cd ays-info-servidor
```

**Uso:**

Para acceder a la página, armar el contenedor con:

```
docker build -t mi-contenedor .
```

Y luego lanzar una imagen con:

```
docker run -p 5000:5000 mi-contenedor -d
```

Acceder a http://localhost:5000

**Workflow:**

El proyecto también contiene un workflow de GitHub Actions que se utiliza para construir y publicar la imagen Docker del proyecto. El workflow se activa cuando se realiza un push a la rama `main` del repositorio.

El workflow realiza las siguientes acciones:

* Comprueba si el usuario tiene permisos para construir y publicar imágenes Docker.
* Comprueba si la imagen Docker ya existe. Si no existe, la construye.
* Publica la imagen Docker en el registro de contenedores de GitHub.
* Comprueba que un contenedor lanzado con la imagen creada sirve una página en el puerto 80

**Uso de imagen:**

La imagen generada se encuentra en: https://github.com/niunmango/ays-info-servidor/pkgs/container/ays-info-servidor

Puede lanzarse un contenedor usando:

```
docker run -d -p 5000:5000 ghcr.io/niunmango/ays-info-servidor:latest
```

Y luego acceder a http://localhost:5000

**Licencia:**

Este proyecto está licenciado bajo la licencia GPLv3.