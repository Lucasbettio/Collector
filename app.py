# from src.engine.domains.files.base import FilesBase
from src.application.tkinter.app import Application
# from multiprocessing import freeze_support
# from src.interfaces.engine import Engine


if __name__ == "__main__":
    # freeze_support()
    # files = FilesBase()
    # files.create_main_files_structures()
    application = Application()
    application.run_app()
