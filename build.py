import os
from sys import platform
import tarfile

from PyQt5.pyrcc_main import processResourceFile

import PyInstaller.config
from PyInstaller.__main__ import run


from hpxbuilder import utils as hpxbuilder_utils
from hpxbuilder import utils


def compress_app():
    compressed_name = utils.get_compressed_name()
    compressed_fpath = os.path.join(utils.get_dist_dir(),
                                    '%s.tar.gz' % compressed_name)

    with tarfile.open(compressed_fpath, 'w:gz') as tar:
        src_path = os.path.join(utils.get_dist_dir(), utils.get_exec_name())
        arcname = os.path.join(compressed_name, 'bin',  utils.get_exec_name())
        tar.add(src_path, arcname)


def process_build():
    platform_name = platform.lower()

    PyInstaller.config.CONF['workpath'] = utils.get_dist_dir()

    platform_spec_file =os.path.join(utils.get_builder_base(), "specs", "%s_build.spec" %platform_name)
    if not os.path.exists(platform_spec_file):
        platform_spec_file = os.path.join(utils.get_builder_base(), "specs", "build.spec")

    run([platform_spec_file])

    if platform.lower() == "linux":
        compress_app()


def compile_imgs():
    media_dir = hpxbuilder_utils.get_chainprox_media_dir_path()
    chainprox_dir = hpxbuilder_utils.get_hpxqt_dir()
    qrc_files = [os.path.join(media_dir, 'images', 'images.qrc')]
    hpximg_file = os.path.join(chainprox_dir, 'hpximg.py')

    processResourceFile(qrc_files, hpximg_file, False)


if __name__ == "__main__":
    compile_imgs()
    process_build()
