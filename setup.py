from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("gera_senha.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Gera_Senha.exe",
    options = options,
    version = "1.0.26.01.23",
    author = "Thiago G.",
    description = 'App gerador de senhas complexas',
    executables = executables
)

## COMANDO PARA EXECUTAR: python.exe .\setup.py build




'''
SCRIPT ORIGINAL DA DOCUMENTAÇÃO DO CX-FREEZE

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="guifoo",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("guifoo.py", base=base)],
)
'''