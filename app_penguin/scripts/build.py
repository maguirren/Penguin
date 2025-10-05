from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import yaml
import markdown
import shutil
from .get_config import *

# path del sitio
DEFAULT_SITE = get_site_path()
# path de los borradores
DRAFTS_PATH = DEFAULT_SITE / "drafts"
# path de los posts no servidos(aun editable)
POSTS_MD_PATH = DEFAULT_SITE / "posts"
# ruta de las plantillas
TEMPLATE_PATH = DEFAULT_SITE / ".templates"
# ruta del blog
BLOG_PATH = DEFAULT_SITE / "blog"
# path de los posts a servir
POSTS_HTML_PATH = DEFAULT_SITE / "blog" / "posts"
# ruta de imagenes o assets
STATICS_PATH = DEFAULT_SITE / "blog" / "statics"


env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

# Retorna lista con las rutas de los borradores
def get_md_file():
    files = []
    for filename in DRAFTS_PATH.glob("*.md"):
        filepath = DRAFTS_PATH / filename
        files.append(filepath)
    return files


# Elimina todos los archivos existentes en el blog
def remove_existing_file():
    if BLOG_PATH.exists() and BLOG_PATH.is_dir():
        for file in BLOG_PATH.rglob("*"):
            if file.is_file():
                file.unlink()


# Retorna lista de diccionarios con el contenido de cada borrador
def get_data(filepath):
    all_data = []
    for file in filepath:
        file_path = Path(file)
        file_content = file_path.read_text(encoding="utf-8")

        if file_content.startswith('---'):
            parts = file_content.split('---', 2)
            data = yaml.safe_load(parts[1])
            content = parts[2].strip() if len(parts) > 2 else ''

            final_result = data | {"content": content}
            all_data.append(final_result)
    return all_data


# Convierte cada borrador .md en un archivo .html
def create_posts(data: list):
    post_template = env.get_template('single-post.html')
    for item in data:
        if item['draft'] == False:
            item['content'] = markdown.markdown(item['content'])
            rendered_html = post_template.render(item)
            filename = POSTS_HTML_PATH / f"{item['title'].replace(' ', '-')}.html"
            filename.write_text(rendered_html)
        else:
            pass


# Crea el index.html
# crea una lista de los posts
def create_index(data: list):
    index_template = env.get_template('index.html')
    index_filename = BLOG_PATH / 'index.html'
    rendered_html = index_template.render(posts=[p for p in data if not p['draft']])
    index_filename.write_text(rendered_html)

def build():
    files = get_md_file()
    all_data = get_data(files)
    
    remove_existing_file()

    create_posts(all_data)

    create_index(all_data)

    # copia el about.html de los templates
    about = TEMPLATE_PATH / 'about-me.html'
    shutil.copy(about, BLOG_PATH)

