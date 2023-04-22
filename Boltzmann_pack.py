import os

from dev_utils import build
from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))

build.build(
    withconsole=True,
    path=os.path.abspath("Boltzmann.py"),
    file_dict=["assets"],
    companyname="Cshtarn",
    product_version="0.0.1",
    icon=global_path.get_proj_abs_path("assets/Boltzmann_icon.png"),
    plugin_dict=["numpy", "pyside6"],
    include_package_dict=None,
)
