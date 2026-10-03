# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('PySide6.QtMultimedia')
a = Analysis(['main.py'], pathex=['.'], binaries=[], datas=[], hiddenimports=hiddenimports, hookspath=[], runtime_hooks=[], excludes=[], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='Junba_KTV_MultiTrack_v1.0', debug=False, bootloader_ignore_signals=False, strip=False, upx=False, console=False, version='packaging/version_info.txt')
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, upx_exclude=[], name='Junba_KTV_MultiTrack_v1.0_Portable')
