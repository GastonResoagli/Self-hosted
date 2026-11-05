# Self-hosted
Este repositorio contiene la configuración y arquitectura completa de un laboratorio práctico de red y monitoreo de servicios autoalojados (*self-hosted*). Utiliza **Homepage** como cuadro de mando centralizado para supervisar microservicios en contenedores Docker y servidores externos en tiempo real.


⚙️ Requisitos Previos
Docker Desktop (con WSL 2 habilitado en Windows o entorno Linux nativo).

Docker Compose v2+.

🚀 Instalación y Despliegue
1 - Clonar el repositorio:

2 - Configurar el archivo .env:
Crea un archivo .env en la raíz del proyecto indicando la IP de tu equipo host: HOST_IP=192.168.1.XX

3- Desplegar con Docker Compose:
docker compose up -d --build

4- Acceder al Dashboard:
Abre tu navegador web e ingresa a: http://localhost:3000
