import os
import json

try:
    with open('config.json', 'r') as fp:
        json_config = json.load(fp)

except FileNotFoundError:
    with open('config.json', 'r') as fp:
        json_config = {
            "name": "App_Name",
            "host": "0.0.0.0",
            "port": 5100,
        }
        json.dump(json_config, fp)


APP_NAME = json_config['name']

PORT = json_config['port']
HOST = json_config['host']

HOME = os.environ['HOME']
WORKING_DIR = os.path.join(HOME, f".{APP_NAME.lower()}")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

EXEC_FILE = 'run.sh'
EXEC_FILE_PATH = os.path.join(BASE_DIR, EXEC_FILE)

VENV = os.path.join(BASE_DIR, 'flask_venv')
VIEW_DIR = os.path.join(BASE_DIR, 'views')
BASHRC_ALIAS = f'flapp-{APP_NAME.lower()}'
