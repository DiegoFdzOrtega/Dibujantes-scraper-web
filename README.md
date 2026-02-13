# 🎨 Sistema de Gestión de Incidencias & Scraper de Artistas

Este repositorio combina un sistema de gestión de reportes técnicos con una infraestructura de scraping para portfolios de dibujantes. Es un proyecto integral que abarca desde la captura de datos (Scraping) hasta su visualización y administración (Flask/XML).

## 🚀 Componentes del Proyecto

### 1. Terminal de Gestión (Frontend)
Interfaz inspirada en consolas industriales para el reporte de incidencias técnicas.
* **Tecnologías:** HTML5, CSS3 (Efecto CRT/Scanline), JavaScript.
* **Funcionalidad:** Formulario de envío de datos estructurados con feedback en consola.

### 2. Scraping & Backend (Python)
Motor de extracción de datos orientado a comunidades de artistas y dibujantes.
* **Tecnologías:** Python, BeautifulSoup4, Flask.
* **Funcionalidad:**
    * Extracción automática de nombres, portfolios y categorías de arte.
    * Servidor Flask para servir los datos scrapeados.
    * Generación dinámica de reportes en formatos JSON y XML.

### 3. Almacenamiento y Estructura (Markup)
* **XML/DTD:** Base de datos persistente con reglas de validación de esquemas.
* **XSLT:** Transformación de datos en crudo a vistas HTML profesionales.
* **RSS:** Feed de actualizaciones para novedades de la plataforma.

## 📂 Estructura de Archivos

```text
├── scraper/              # Scripts de Python (BS4 + Flask)
├── frontend/             # Interfaz de la terminal (HTML/CSS)
├── data/                 # Archivos XML, DTD y XSLT
├── novedades.rss         # Canal de noticias del sistema
└── README.md             # Documentación
