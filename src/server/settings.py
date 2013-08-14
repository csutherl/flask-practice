import logging
import pprint
import os
import yaml

# CustomLogging
# create console handler and set level to info
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# set formatter
console.setFormatter(formatter)
# End CustomLogging

flask_config = {}

settings_log = logging.getLogger(name="settings")
settings_log.setLevel(logging.DEBUG)
settings_log.addHandler(console)

pp = pprint.PrettyPrinter(indent=4)

settings_filename = '.flask-settings.yml'
settings_fs_locs = ["{}/{}".format(os.path.expanduser("~"), settings_filename), "".join(settings_filename)]

settings_loaded = False
for the_path in settings_fs_locs:
    settings_log.debug("Attempting to load {}".format(the_path))
    try:
        with open(the_path, 'r') as f:
            prop_list = yaml.load(f.read())
            for key, value in prop_list.items():
                flask_config[key] = value

            settings_log.debug("Settings loaded from %s" % the_path)
            settings_loaded = True
            break
    except (OSError, IOError) as e:
        settings_log.warn("{} {}".format(e.strerror, the_path))


if not settings_loaded:
    settings_log.error("Could not find settings file in {}".format(','.join(settings_fs_locs)))
    exit()

# INFO = 20
# DEBUG = 10
try:
    console.level = flask_config['logging_level']
except:
    flask_config['logging_level'] = 20  # default to info
    console.level = flask_config['logging_level']
