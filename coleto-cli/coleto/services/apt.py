import subprocess

from coleto.models.packages import Package


def search(query: str) -> list[Package]:
    """
    Busca paquetes utilizando APT.
    """
    try:
        result = subprocess.run(
            ["apt", "search", query],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode != 0:
            return []

        return _parse_search_output(result.stdout)

    except Exception as e:
        print(f"Error en apt.search(): {e}")
        return []


def _parse_search_output(output: str) -> list[Package]:
    """
    Convierte la salida de `apt search` en una lista de Package.
    """

    packages: list[Package] = []

    lines = output.splitlines()

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if "/" in line:
            name = line.split("/")[0]

            description = ""

            if i + 1 < len(lines):
                description = lines[i + 1].strip()

            packages.append(
                Package(
                    name=name,
                    description=description,
                )
            )

        i += 1

    return packages

def install(package: str) -> bool:
    """
    Instala un paquete usando APT.
    """

    try:
        result = subprocess.run(
            [
            "sudo",
            "apt",
            "install",
            "-y",
            package,
            ],
            timeout=600,
        )

        return result.returncode == 0
    
    except Exception:
        return False