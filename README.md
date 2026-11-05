# 🛡️ Laboratorio de Ciberseguridad en la Nube (Render & Docker)
**Asignatura:** Seguridad en redes y aplicaciones web (Unidad 2)  
**Estudiante:** Adrianys Maria Saumeth Padilla  
**Institución:** Institución Universitaria Digital de Antioquia - IU Digital  
**Docente Asesor:** Daniel Enrique Tordecilla Burgos  

---

## 📋 Descripción del Laboratorio
Este repositorio contiene la arquitectura modular para el despliegue de un laboratorio de ciberseguridad ofensiva/defensiva en la plataforma Cloud **Render**, utilizando contenedores **Docker**. 

El entorno consta de:
1. **00-servidor-dmz:** Servidor objetivo (víctima) protegido en DMZ simulada.
2. **01-ataque-dos:** Generación de ráfagas masivas de peticiones concurrentes HTTP.
3. **02-escaneo-puertos:** Reconocimiento de puertos comunes con `nc` (Netcat).
4. **03-fuerza-bruta-rutas:** Enumeración de directorios y endpoints sensibles.
5. **04-exfiltracion-dns:** Simulación de exfiltración de credenciales codificadas en base64 mediante consultas DNS (`nslookup`).
6. **05-cadena-suministro:** Inyección adversaria de script malicioso durante la fase de construcción de la imagen Docker.
7. **06-credential-stuffing:** Prueba automatizada de pares usuario/contraseña mediante peticiones HTTP Basic Auth.
8. **07-proxy-mitm:** Servidor proxy interceptor que captura cabeceras y modifica el contenido en tránsito (inyección HTML).

---

## 🚀 Despliegue en Render
1. Conectar este repositorio a **Render.com**.
2. Crear primero el servicio web Docker para `00-servidor-dmz` con el nombre `servidor-web-dmz-asaumeth`.
3. Obtener la URL pública de la DMZ (ejemplo: `https://servidor-web-dmz-asaumeth.onrender.com`).
4. Desplegar los módulos atacantes `01` al `07` indicando su respectivo *Root Directory*.
