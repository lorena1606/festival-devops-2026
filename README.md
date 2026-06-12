# Festival DevOps Music Fest

Este proyecto consiste en el despliegue de una plataforma web para la gestión de un festival de música, estructurado bajo una arquitectura de microservicios contenerizados utilizando Docker y Docker Compose.

Tecnologías Utilizadas
Frontend: HTML5, CSS3 y JavaScript.
Backend: Python con el microframework Flask.
DevOps & Contenedores: Docker (Dockerfiles independientes para servicios) y Docker Compose.
Control de Versiones: Git y GitHub utilizando la metodología Git Flow básico.

Arquitectura y Despliegue con Docker

El sistema se compone de dos servicios principales que se comunican de forma aislada dentro de una red nativa de Docker:

1. Frontend: Servidor web que expone la interfaz de usuario de la landing page.
2. Backend: API en Flask que gestiona los servicios internos de la aplicación.

## Instrucciones para ejecutar el entorno local:

Para construir las imágenes personalizadas y levantar los servicios (junto con sus redes y volúmenes correspondientes), ejecuta el siguiente comando en la raíz del proyecto:

```bash
docker-compose up --build