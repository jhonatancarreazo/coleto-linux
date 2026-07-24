from coleto.models.packages import Package


def filter_packages(
    packages: list[Package],
    search: str | None = None,
    limit: int | None = None,
) -> list[Package]:
    """
    Filtra una lista de paquetes por nombre y limita la cantidad de resultados.
    """

    if search:
        packages = [
            package
            for package in packages
            if search.lower() in package.name.lower()
        ]

    if limit is not None:
        packages = packages[:limit]

    return packages