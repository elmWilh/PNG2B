import importlib
import os
import subprocess
import sys

from app_meta import APP_NAME, APP_VERSION

REQUIRED_LIBS = [
    "pygame",
    "numpy",
    "pyaudio",
    "pywin32",
]


def install_package(package):
    print(f"Installing {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Please install it manually.")
        sys.exit(1)


def check_and_install():
    print(f"Starting {APP_NAME} v{APP_VERSION}")
    for lib in REQUIRED_LIBS:
        print(f"Checking library: {lib}...")
        try:
            if lib == "pywin32":
                import win32api
                import win32gui
            else:
                importlib.import_module(lib)
        except ImportError:
            print(f"Library {lib} was not found. Installing...")
            install_package(lib)


if __name__ == "__main__":
    check_and_install()

    main_path = os.path.join(os.path.dirname(__file__), "main.pyw")
    if not os.path.exists(main_path):
        print("main.pyw was not found.")
        sys.exit(1)

    python_executable = sys.executable
    if sys.platform.startswith("win") and python_executable.endswith("python.exe"):
        python_executable = python_executable.replace("python.exe", "pythonw.exe")

    subprocess.Popen([python_executable, main_path])
