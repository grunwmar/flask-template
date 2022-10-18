from importlib import import_module
import sys
import os
import helpers.config as config


for module_name in os.listdir(config.VIEW_DIR):
    view_dir = os.path.basename(config.VIEW_DIR)
    if module_name.endswith('_view.py'):
        name, ext = os.path.splitext(module_name)
        globals()[name] = import_module(f'views.{name}')
