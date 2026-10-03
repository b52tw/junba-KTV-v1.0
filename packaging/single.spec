# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('PySide6.QtMultimedia')
a = Analysis(['main.py'], pathex=['.'], binaries=[], datas=[], hiddenimports=hiddenimports, hookspath=[], runtime_hooks=[], excludes=[], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.datas, [], name='Junba_KTV_MultiTrack_v1.0', debug=False, bootloader_ignore_signals=False, strip=False, upx=False, console=False, version='packaging/version_info.txt')
