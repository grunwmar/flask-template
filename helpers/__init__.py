import helpers.config

def assure():

    if os.path.isfile('.assured'):
        return None

    if not os.path.isdir(config.WORKING_DIR):
        os.mkdir(config.WORKING_DIR)


    if not os.path.isfile('.assure'):
        with open('.assured', 'w') as fp:
            fp.write('assured')
