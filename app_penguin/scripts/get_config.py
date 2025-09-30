import json
from pathlib import Path
from typing import Optional


CONFIG_DIR = Path.home() / ".config" / "penguin"
CONFIG_FILE = CONFIG_DIR / "config.json"


# Cargar la configuracion del json.
# devuelve un diccionarion de python
def load_config():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    else:
        return {"sites": {}, "default_site": None}


# Convierte el dict de python en json
# guarda el texto en config.json
def save_config(config: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(config, indent=4), encoding="utf-8")


# Registra un sitio nuevo
# si no existe un default_site lo asigna al nuevo
def register_site(site_name: str, path: Path):
    config = load_config()
    config["sites"][site_name] = str(path)
    if config["default_site"] is None:
        config["default_site"] = site_name
    save_config(config)


# Obtener la ruta de un sitio
# devuelve un path con la ruta del sitio
def get_site_path(site_name: Optional[str] = None) -> Path:
    config = load_config()
    if site_name is None:
        site_name = config["default_site"]
    if site_name not in config["sites"]:
        raise ValueError(f"El sitio '{site_name}' no esta registrado")
    return Path(config["sites"][site_name])
