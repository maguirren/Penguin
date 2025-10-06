from pathlib import Path
import subprocess
from .get_config import get_site_path


DEFAULT_SITE = get_site_path()
BLOG_PATH = DEFAULT_SITE / 'public'
GIT_DIR = BLOG_PATH / '.git'

def deploy_to_github():
    if not BLOG_PATH.exists():
        print(f"Error: la ruta {BLOG_PATH} no existe.")
        return

    if not GIT_DIR.exists():
        print("Error: no estas dentro de un repositorio Git.")
        return

    commit_message = input("Ingresa un mensaje para el commit_(por defecto 'update'): ") or "update"

    print(f"🧭 Ejecutando Git en: {BLOG_PATH.resolve()}")
    print(f"📁 Contiene .git: {GIT_DIR.exists()}")
    
    try:
        subprocess.run(["git", "add", "."], check=True, cwd=BLOG_PATH)
        subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=BLOG_PATH)
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=BLOG_PATH)
        print("Blog deployado exitosamente ")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Git: {e}")
