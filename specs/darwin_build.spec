# -*- mode: python ; coding: utf-8 -*-

import os
import sys

from hpxbuilder import utils

block_cipher = None

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis([utils.get_chainprox_exec_path()],
             pathex=[],
             binaries=[],
             datas=[
             (utils.get_chainprox_templates_dir_path(), "templates"),
                (utils.get_chainprox_media_dir_path(), "media"),],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='chainprox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='chainprox')

app = BUNDLE(coll,
             name='chainprox.app',
             icon=utils.get_app_icon_path(),
             bundle_identifier=None)
