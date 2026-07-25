import os
import shutil
import subprocess


def is_root() -> bool:
    return os.geteuid() == 0


def has_sudo() -> bool:
    return shutil.which("sudo") is not None


def run_privileged(command: list[str], timeout: int = 300):

    cmd = command

    if not is_root():

        if not has_sudo():
            raise PermissionError(
                "Se requieren privilegios de administrador."
            )

        cmd = ["sudo"] + command

    return subprocess.run(
        cmd,
        timeout=timeout,
    )