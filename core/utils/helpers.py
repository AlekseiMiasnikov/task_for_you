from os import getcwd, scandir, walk
from os.path import exists, join
from pathlib import Path

from download_chromedriver import get_stable_chromedriver_version


def get_current_folder(folder: str) -> str:
    current = getcwd()

    def find_folder(path: str or Path) -> str:
        for _, folders, _ in walk(path):
            if folder in folders:
                return join(path, folder)
        else:
            return find_folder(path=Path(path).parent)

    return find_folder(path=current)


def get_fixtures():
    files_list = []
    for root, dirs, files in walk(get_current_folder(folder="fixtures")):
        for file in files:
            if ".pyc" in file:
                continue
            root_folder = (
                root[root.find("fixtures") :].replace("\\", ".").replace("/", ".")
            )
            file_name = file[: len(file) - 3]
            files_list.append(f"{root_folder}.{file_name}")
    return files_list


def get_driver_path() -> str:
    driver_path = join(Path(__file__).parent.parent, "files", "chromedriver")

    if not exists(driver_path):
        return get_stable_chromedriver_version()

    return [
        file.path for file in scandir(driver_path) if file.name != "driver_version.json"
    ][0]
