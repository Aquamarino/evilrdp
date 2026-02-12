from PyInstaller.utils.hooks import get_module_file_attribute, copy_metadata
from PyInstaller.compat import is_win, is_darwin, is_linux
import os

# Hook for Pillow's ImageQt module
# This module requires PyQt5 to be available

datas = []
hiddenimports = ['PIL._imaging']
