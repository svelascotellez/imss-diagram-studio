FROM mcr.microsoft.com/powershell:lts-ubuntu-22.04

# Instalar dependencias base del sistema, Python y herramientas de auditoría
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    gnupg \
    ca-certificates \
    python3 \
    python3-pip \
    python3-venv \
    chromium-browser \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Instalar k6 para benchmarks de resiliencia y SLAs (Gate 9)
RUN gpg -k && \
    gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69 || true && \
    echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | tee /etc/apt/sources.list.d/k6.list && \
    apt-get update && apt-get install -y --no-install-recommends k6 || true && \
    rm -rf /var/lib/apt/lists/*

# Preinstalar módulo Pester 6 en PowerShell Core
RUN pwsh -Command "Install-Module -Name Pester -MinimumVersion 5.3.0 -Force -SkipPublisherCheck -Scope AllUsers"

# Configurar alias y entorno de trabajo
ENV PYTHONUNBUFFERED=1
WORKDIR /workspace

CMD ["pwsh"]

