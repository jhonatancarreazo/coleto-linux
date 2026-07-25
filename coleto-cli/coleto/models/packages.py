from dataclasses import dataclass
@dataclass
class Package:
    name: str
    version: str = ""
    architecture: str = ""
    maintainer: str = ""
    installed_size: str = ""
    repository: str = ""
    description: str = ""