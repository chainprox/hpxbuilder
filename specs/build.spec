# -*- mode: python -*-

import os
import sys

from hpxbuilder import utils

block_cipher = None


a = Analysis([utils.get_chainprox_exec_path()],
             binaries=[],
             datas=[
                (utils.get_chainprox_templates_dir_path(), "templates"),
                (utils.get_chainprox_media_dir_path(), "media"),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=utils.get_exec_name(),
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon=utils.get_app_icon_path())
