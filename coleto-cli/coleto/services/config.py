from __future__ import annotations

import json
from pathlib import Path

# Directorio donde Coleto guardara sus datos
DATA_DIR = Path.home() / ".coleto"
CONFIG_FILE = DATA_DIR / "config.json"

def _ensure_data_dir() -> None:

    """Crea la carpeta si no existe."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_config() -> dict:

    """Carga la configuración."""

    _ensure_data_dir()

    if not CONFIG_FILE.exists():

        return {}

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:

        return json.load(file)

def save_config(config: dict) -> None:

    """Guarda la configuración."""

    _ensure_data_dir()

    with open(CONFIG_FILE, "w", encoding="utf-8") as file:

        json.dump(config, file, indent=4, ensure_ascii=False)

def get(key: str, default=None):

    config = load_config()

    return config.get(key, default)

def set(key: str, value):

    config = load_config()

    config[key] = value

    save_config(config)