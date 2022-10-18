import os
import helpers.config as config

def make_shell_script():
    code = f"""#!/bin/bash
cd {config.BASE_DIR}
source {os.path.join(config.VENV, 'bin', 'activate')}
python app.py
# xdg-open http://{config.HOST}:{config.PORT}
"""
    with open(config.EXEC_FILE_PATH, 'w') as file:
        file.write(code)

    os.system(f'chmod +x {config.EXEC_FILE_PATH}')


def make_virtual_env():
    if not os.isdir(config.VENV):
        os.system(f'python3 -m venv {config.VENV}')
        pip = os.path.join(config.VENV, 'bin', 'pip')
        requirements = os.path.join(config.BASE_DIR, 'requirements.txt')
        os.system(f'{pip} install -r {requirements})


def bashrc_add_alias():
    new_suffix = f'{config.ALIAS}_bk'
    bashrc_path = os.path.join(config.HOME, '.bashrc')
    bashrc_path_backup = os.path.join(config.HOME, f'.bashrc.{new_suffix}')

    if not bashrc_path.endswith(new_suffix):
        os.system(f'cp "{bashrc_path}" "{bashrc_path_backup}"')
    else:
        raise Exception('File .bashrc was already backuped.')

    with open(os.path.join(config.HOME, '.bashrc'), 'a') as file:
        alias = f'alias {config.BASHRC_ALIAS}=bash "{config.EXEC_FILE_PATH}"'
        file.write(alias)


if __name__ == '__main__':
    make_virtual_env()
    make_shell_script()
    bashrc_add_alias()
