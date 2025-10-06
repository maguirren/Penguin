from pathlib import Path
from importlib import resources
import shutil
from .get_config import *


def create_site(site_name: str):
    """
    Crea la carpeta del sitio en el directorio del usuario.

    Args:
        site_name (str): Nombre del directorio del sitio

    Estructura creada:
        - .templates
        - drafts
        - posts
        - public
        - public/posts
        - public/statics

    Copia plantillas desde el paquete a .templates
    """
    site_dir = Path.home() / site_name
    site_dir.mkdir(parents=True, exist_ok=True)
    register_site(site_name, site_dir)
    
    # Crea las carpetas
    for d in ['.templates', 'drafts', 'posts', 'public', 'public/statics', 'public/posts']:
        (site_dir / d).mkdir(parents=True, exist_ok=True)


    # Accede a los templates
    template_dir = resources.files("app_penguin.templates")

    # Itera sobre los archivos que vas a copiar
    for file_name in ['index.html', 'about.html', 'list_post.html', 'single_post.html']:
        src_file = template_dir / file_name

        with resources.as_file(src_file) as src_path:
            dst_file = site_dir / ".templates" / file_name
            shutil.copy(src_path, dst_file)
            print(f"Archivo copiado en {dst_file}")
    
