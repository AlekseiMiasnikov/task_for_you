import json
from os import chmod, mkdir, scandir
from os.path import exists, join
from pathlib import Path

from get_chrome_driver import GetChromeDriver


def get_stable_chromedriver_version() -> str:
    """
    Проверка стабильной версии драйвера.

    :return: Путь до драйвера
    """
    get_driver = GetChromeDriver()

    files = str(join(Path(__file__).parent, "files"))
    driver_path = join(Path(__file__).parent, "files", "chromedriver")
    driver_version = join(driver_path, "driver_version.json")
    driver = join(driver_path, "chromedriver")

    current_version = get_driver.matching_version()

    # Проверка существования файлов
    if not exists(files):
        mkdir(files)

    # Проверка существования папки с драйвером
    if not exists(driver_path):
        mkdir(driver_path)

    # Проверка существования файла с версией драйвера
    if exists(driver_version):
        with open(driver_version, "r") as file:
            downloaded_version = json.load(file)["version"]
    else:
        open(driver_version, "x")
        with open(driver_version, "w") as file:
            config = {
                "version": current_version,
            }
            json.dump(config, file)
        chmod(driver_version, 0o755)
        downloaded_version = current_version

    # Проверка версии текущего драйвера или существования драйвера
    if downloaded_version != current_version or not exists(driver):
        get_driver.install(output_path=driver_path)
        with open(driver_version, "w") as file:
            config = {
                "version": current_version,
            }
            json.dump(config, file)

    return [file.path for file in scandir(driver_path) if file.name != "driver_version.json"][0]


if __name__ == "main":
    print(get_stable_chromedriver_version())
