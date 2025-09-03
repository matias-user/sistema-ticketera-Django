# Sistema de ticketera MVC con Django

## Ejecutar proyecto
- Crear .env con las variables de entorno para Postgresql
`docker compose run web django-admin startproject tickets . `
`docker compose up --build`
- Cambiar en settings.py el engine a postgresql y agregar las variables de entorno

## Requerimientos App
- Un usuario genera un ticket.
- El ticket tiene cierto estado.
- El ticket lo puede ver el usuario.
- El ticket lo puede ver el equipo que resuelve.
- Debe haber un módulo de reportes.
- Modulo de notificaciones que tenga una interfaz tipo notificaciones.

## Módulos encontrados:
- **User**
- **Ticket**
- **Report**
- **Notification**

