import os
import zipfile

from setuptools import setup
from hpxbuilder import utils


def compress_app():
    app_dir = os.path.join(utils.get_dist_dir(),
                           '%s.app' % utils.get_exec_name())
    compressed_fpath = os.path.join(utils.get_dist_dir(),
                                    '%s.zip' % utils.get_compressed_name())

    with zipfile.ZipFile(compressed_fpath, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(app_dir):
            root = os.path.abspath(root)
            for f in files:
                src_path = os.path.join(root, f)
                arcname = src_path.split('dist/')[1]
                zf.write(src_path, arcname)
                print('Compressing %s' % os.path.join(root, f))


def process():
    import sys
    sys.argv.append("py2app")

    OPTIONS = {
        'argv_emulation':True,
        'packages': [],
        'resources': [
            utils.get_chainprox_media_dir_path(),
            utils.get_chainprox_templates_dir_path()],
        'iconfile': utils.get_app_icon_path(),
        'plist': {'CFBundleIconFile': 'icon.icns'},
    }

    setup(
        app=[utils.get_chainprox_exec_path()],
        data_files=[],
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )

    compress_app()


if __name__ == "__main__":
    process()
