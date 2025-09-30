import subprocess
from pathlib import Path
from .get_config import *


def edit_draft(query: Optional[str] = None):
    drafts_dir = get_site_path() / "drafts"
    drafts = list(drafts_dir.glob("*.md"))

    if not drafts:
        print("⚠️ No hay drafts creados todavía.")
        return
    
    if query:
        drafts = [d for d in drafts if query.lower() in d.name.lower()]
    
    if not drafts:
        print(f"❌ No se encontraron drafts que coincidan con '{query}'")
        return

    if len(drafts) == 1:
        file_to_edit = drafts[0]
    else:
        print('Varios drafts encontrados:')
        for i, d in enumerate(drafts, 1):
            print(f"{i}) {d.name}")
        choice = input("Selecciona numero: ")
        try:
            file_to_edit = drafts[int(choice)-1]
        except (ValueError, IndexError):
            print("❌Seleccion invalida")
            return

    print(f"✍️ Editando {file_to_edit}")
    subprocess.run(['nvim', str(file_to_edit)])

