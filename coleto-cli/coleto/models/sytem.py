from dataclasses import dataclass


@dataclass (slots=True)
class SystemInfo:
    os_name: str
    version: str
    architecture: str
    python_version: str
    host_name: str
    user_name: str