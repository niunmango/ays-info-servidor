# 📊 AYS - Server Information

Educational project to demonstrate CI/CD pipelines with **GitHub Actions** and container deployment using **Podman** (primary) and **Docker** (alternative).

## 🎯 Description

This Flask application shows real‑time information about the server where it runs:
- Host name
- Current date and time
- Total and free disk space
- Output of the `top` command (auto‑refresh every 4 seconds)

## 🚀 Installation

### Option 1: With Podman (recommended)

```bash
# Clone the repository
git clone https://github.com/niunmango/ays-info-servidor.git
cd ays-info-servidor

# Build the image
podman build -t ays-info-servidor .

# Run the container
podman run -d -p 5000:5000 --name server-info ays-info-servidor
```

### Option 2: With Docker (alternative)

```bash
# Clone the repository
git clone https://github.com/niunmango/ays-info-servidor.git
cd ays-info-servidor

# Build the image
docker build -t ays-info-servidor .

# Run the container
docker run -d -p 5000:5000 --name server-info ays-info-servidor
```

### Option 3: Without containers (local development)

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🐳 Using the image from GitHub Container Registry

### With Podman (recommended)

```bash
# Pull the latest image
podman pull ghcr.io/niunmango/ays-info-servidor:latest

# Run
podman run -d -p 5000:5000 ghcr.io/niunmango/ays-info-servidor:latest
```

### With Docker (alternative)

```bash
# Pull the latest image
docker pull ghcr.io/niunmango/ays-info-servidor:latest

# Run
docker run -d -p 5000:5000 ghcr.io/niunmango/ays-info-servidor:latest
```

Then open: http://localhost:5000

## ⚙️ CI/CD with GitHub Actions

The pipeline triggers automatically on every `push` to the `main` branch:
1. **Build**: Builds the Docker image.
2. **Push**: Publishes the image to `ghcr.io`.
3. **Test**: Verifies the container works on port 5000.

### Pipeline endpoints

| Job   | Description |
|-------|-------------|
| `build` | Build and push the image to GHCR |
| `test`  | Validate the container responds on port 5000 |

## 📝 API Endpoints

| Path | Description |
|------|-------------|
| `/`      | Main page showing server info |
| `/health`| Health check endpoint |
| `/top`   | Raw output of the `top` command |

## 🛠️ Technologies used

- **Python 3.12**
- **Flask 3.x**
- **Gunicorn** (WSGI server for production)
- **Docker**
- **GitHub Actions**

## 📋 Requirements

- Docker (to use the built image)
- Or Python 3.12+ with `pip` (for local development)

## 📜 License

This project is licensed under **GPLv3**.

---

**Project created by:** niunmango
**Modified by:** Hermes Agent (CURZAS – UNCo)
