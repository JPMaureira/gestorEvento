# gestorEvento

# Gestor de Eventos

Gestor de Eventos es una aplicación web desarrollada en Django para gestionar eventos. Permite a los usuarios agregar, editar, eliminar y buscar eventos.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/gestor-eventos.git

2. **Accede al directorio del proyecto::**
cd gestor-eventos

3. **Crea y activa un entorno virtual:**
python -m venv venv
source venv/bin/activate  # En sistemas basados en Unix
# o
venv\Scripts\activate  # En sistemas Windows

4. **nstala las dependencias**
pip install -r requirements.txt

**Configuración**
**Copia el archivo de configuración de ejemplo:**
cp config/settings_local.example.py config/settings_local.py


**Edita config/settings_local.py según sea necesario.**


**Base de Datos**
**Aplica las migraciones:**

python manage.py migrate

**Crea un superusuario:**
python manage.py createsuperuser


**Ejecución**
**Inicia el servidor de desarrollo:**

python manage.py runserver


