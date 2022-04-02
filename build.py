import os
from sys import platform as _platform

from PyQt5.pyrcc_main import processResourceFile

from hpxbuilder import utils as hpxbuilder_utils


def build_p2app():
    from mac import build
    build.process()


def build_pyinstaller():
    from win import build
    build.process()


def compile_imgs():
    media_dir = hpxbuilder_utils.get_chainprox_media_dir_path()
    chainprox_dir = hpxbuilder_utils.get_hpxqt_dir()
    qrc_files = [os.path.join(media_dir, 'images', 'images.qrc')]
    hpximg_file = os.path.join(chainprox_dir, 'hpximg.py')

    processResourceFile(qrc_files, hpximg_file, False)


if __name__ == "__main__":
    compile_imgs()
    if _platform == "darwin":
        build_p2app()
    else:
        build_pyinstaller()
