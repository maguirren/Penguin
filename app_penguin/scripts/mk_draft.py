import subprocess
from pathlib import Path
from .get_config import *
from datetime import datetime


def create_draft(filename: str):
    # Define el blog por defaul y crea la carpeta drafts si no existe
    path_site = get_site_path()
    draft_path = path_site / "drafts"
    draft_path.mkdir(parents=True, exist_ok=True)
    
    # Crea el titulo del archivo con la current time
    current_time = datetime.now().strftime('%Y-%m-%d')
    file_path = draft_path / f"{current_time}-{filename.replace(' ','-')}.md"

    # Verifica si el archivo ya existe
    if file_path.exists():
        print(f"❌ Error: el draft '{file_path.name}' ya existe en {file_path.parent}")
        return
    
    # Crea un header yaml que luego sera procesado
    header = f"""---
title: {filename}
date: {current_time}
draft: true
---
"""

    # Crea el archivo y escribe el header y el titulo
    file_path.write_text(header + f'\n# {filename}\n', encoding="utf-8")

    print(f"✅ Draft '{file_path.name}' creado en {file_path.parent}")



    # Abre el archivo con neovim
    subprocess.run(['nvim', str(file_path)])
