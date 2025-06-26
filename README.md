# Trabajo-Final-Phyton
Este proyecto es un conjunto de aplicaciónes de consola en Python realizado para Tecno 3F.

## 📦 Requisitos

- Python 3.x

---

# 🧾 Sistema de Gestión de Tickets en Python

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar tickets de soporte de forma sencilla. El sistema fue construido en 3 versiones progresivas, mejorando en cada una la forma de almacenar y acceder a los tickets.

---

## 🔁 Estructura del Menú

El menú principal incluye tres opciones:

1. **Alta Ticket** – Permite crear un nuevo ticket ingresando: nombre, sector, asunto y problema.
2. **Leer Ticket** – Permite visualizar tickets ya registrados.
3. **Salir** – Cierra el programa con confirmación.

---

## 🧩 Versiones del Proyecto

### ✅ Versión 1: Archivos individuales `.ticket`

- Cada ticket se guarda como un archivo binario independiente (ej: `1234.ticket`).
- Se utiliza `pickle` para guardar y leer cada archivo individualmente.
- Se pide al usuario recordar el número del ticket para poder consultarlo más tarde.

🧪 Tecnologías utilizadas:
- `pickle`
- `os.path.isfile()`
- Archivos `.ticket` individuales

---

### ✅ Versión 2: Almacenamiento unificado `tickets.pkl`

- Todos los tickets se almacenan en un **único archivo binario** llamado `tickets.pkl`.
- Al iniciar el programa, se cargan todos los tickets a memoria desde ese archivo.
- Se sigue pidiendo al usuario que memorice el número del ticket generado para consultarlo.

🧪 Ventajas:
- Gestión centralizada de tickets.
- Más eficiente que la versión con archivos separados.

---

### ✅ Versión 3: Lectura interactiva desde `tickets.pkl`

- Expande la funcionalidad de la versión 2.
- Al leer un ticket, el usuario **ve una lista de todos los tickets disponibles** con nombre y asunto.
- Se selecciona el ticket deseado desde un menú numerado.
- Mejora la experiencia de usuario y evita tener que recordar el número manualmente.

🧪 Novedades:
- Interfaz por consola más intuitiva
- Listado dinámico de tickets cargados

---

## 🖼️ Cómo se ve

<img alt="Menu" src="Preview\menu.png" width="500" />
<img alt="Lista" src="Preview\lista.png" width="500" />
<img alt="Ticket 1" src="Preview\imagen_ticket_1.png" width="500" />
<img alt="Ticket 2" src="Preview\imagen_ticket_2.png" width="500" />
<img alt="Salir" src="Preview\salir.png" width="500" />

---
---

<h3 align="center">Mis redes sociales:</h3>
<p align="center">
<a href="https://www.youtube.com/c/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="shinigamy19" height="35" width="35" title="Mi canal de Youtube" /></a>
<a href="https://twitch.tv/shinigamy_19" target="_blank" rel="noopener"><img align="center" src="https://img.icons8.com/external-justicon-flat-justicon/64/external-twitch-social-media-justicon-flat-justicon.png" alt="px9fcpbp3T" height="30" width="30" title="Mi canal de Twitch"/></a>
<a href="https://kick.com/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://img.freepik.com/premium-vector/kick-logo-vector-download-kick-streaming-icon-logo-vector-eps_691560-10814.jpg" alt="px9fcpbp3T" height="30" width="30" title="Mi canal de Kick"/></a>
<a href="https://discord.gg/px9fcpbp3T" target="_blank" rel="noopener"><img align="center" src="https://www.notebookcheck.org/fileadmin/Notebooks/News/_nc3/discord.jpeg" alt="Mi Server de Discord" title="Mi Server de Discord" height="30" width="30" style="border-radius: 4px 4px 4px 4px"  /></a>
<a href="https://instagram.com/shinigamy19_art" target="_blank" rel="noopener"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" alt="shinigamy19_art" title="Mi instagram de Artista" height="30" width="30" /></a>
<a href="https://instagram.com/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" title="Mi Intagram Personal" alt="shinigamy19" height="30" width="30" /></a>
<a href="https://www.tiktok.com/@shinigamy_19" target="_blank" rel="noopener"><img align="center" src="https://cdn4.iconfinder.com/data/icons/logos-brands-in-colors/2500/tiktok-icon-white-512.png" alt="shinigamy19" title="Mi Tiktok" height="30" width="30" style="border-radius: 4px 4px 4px 4px" /></a>
<a href="https://linkedin.com/in/eros-benitez" target="_blank" rel="noopener"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png" alt="eros-benitez" title="Mi LinkedIn" height="30" width="30" style="border-radius: 4px 4px 4px 4px" /></a>
<a href="https://www.behance.net/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/behance.svg" alt="shinigamy19" title="Mi Behance" height="30" width="30" /></a>
<a href="https://shinigamy19.itch.io/" target="_blank" rel="noopener"><img align="center" src="https://static.itch.io/images/app-icon.svg" alt="shinigamy19" title="Mi perfil de Itch" height="30" width="30" style="border-radius: 4px 4px 4px 4px" /></a>
<a href="https://fb.com/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="shinigamy19" title="Mi facebook" height="30" width="30" /></a>
<a href="mailto:erosbenitezd@gmail.com" target="_blank" rel="noopener"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Gmail_Icon_%282013-2020%29.svg/2560px-Gmail_Icon_%282013-2020%29.svg.png" alt="shinigamy19" title="Mi Mail" height="30" width="35" /></a>

<div>
<h3 align="center">Donaciones:</h3>
<p align="center">
<a href="https://ceneka.net/mp/d/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://github.com/Shinigamy19/repo-svg-iconos/blob/main/Logos/Mercado%20Pago.png?raw=true" alt="shinigamy19" height="35" width="35" title="Donaciones Por Mercado Pago" /></a>
<a href="https://www.paypal.me/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Paypal_2014_logo.png" alt="px9fcpbp3T" height="30" width="30" title="Donaciones Por PayPal"/></a>
<a href="https://www.patreon.com/shinigamy19" target="_blank" rel="noopener"><img align="center" src="https://github.com/Shinigamy19/repo-svg-iconos/blob/main/Logos/Patreon.png" alt="px9fcpbp3T" height="30" width="30" title="Donaciones Por Patreon"/></a>

</p>
<p align="center">
<a href='https://cafecito.app/shinigamy19' rel='noopener' target='_blank'><img srcset='https://cdn.cafecito.app/imgs/buttons/button_6.png 1x, https://cdn.cafecito.app/imgs/buttons/button_6_2x.png 2x, https://cdn.cafecito.app/imgs/buttons/button_6_3.75x.png 3.75x' src='https://cdn.cafecito.app/imgs/buttons/button_6.png' alt='Invitame un café en cafecito.app' title="Donaciones Por Cafecito"/></a></p>
</div>

