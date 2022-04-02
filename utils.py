import platform

import hpxqt
import hpxbuilder
import os
import inspect


def get_hpxbuilder_dir():
    return os.path.dirname(inspect.getfile(hpxbuilder))


def get_builder_base():
    return get_hpxbuilder_dir()


def get_dist_dir():
    return os.path.join(get_builder_base(), 'dist')


def get_hpxqt_version():
    return hpxqt.__version__


def get_compressed_name():
    _os = platform.system().lower()
    compressed_name_map = {
        'darwin': 'chainprox-{version}-osx',
        'linux': 'chainprox-{version}-x86_64-linux-gnu'
    }
    return compressed_name_map[_os].format(version=get_hpxqt_version())


def get_exec_name():
    if platform.system().lower() == 'windows':
        return 'chainprox-{version}-win64'.format(version=get_hpxqt_version())
    return 'chainprox'


def get_hpxqt_dir():
    return os.path.dirname(inspect.getfile(hpxqt))


def get_chainprox_exec_path():
    return os.path.join(get_hpxqt_dir(), "chainprox.py")


def get_chainprox_media_dir_path():
    return os.path.join(get_hpxqt_dir(), "media")


def get_chainprox_templates_dir_path():
    return os.path.join(get_hpxqt_dir(), "templates")


def get_app_icon_path():
    _os = platform.system().lower()
    icons_map = {
        'darwin': 'icon.icns',
        'windows': 'icon.ico',
        'linux': 'icon.png'
    }
    return os.path.join(get_builder_base(), 'icons', icons_map[_os])
