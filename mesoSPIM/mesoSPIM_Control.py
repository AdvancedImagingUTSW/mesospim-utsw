import time
import logging
import os
import sys
import importlib.util
from PyQt5 import QtWidgets
from src.mesoSPIM_MainWindow import mesoSPIM_MainWindow

'''
mesoSPIM_control.py
========================================
The core module of the mesoSPIM software
'''

timestr = time.strftime("%Y%m%d-%H%M%S")
logging_filename = timestr + '.log'
logging.basicConfig(filename='log/'+logging_filename, level=logging.INFO, format='%(asctime)-8s:%(levelname)s:%(threadName)s:%(thread)d:%(module)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)
logger.info('mesoSPIM-control started')
logger.info('Modules loaded')

def load_config():
    '''
    Import microscope configuration at startup
    '''

    ''' This needs an placeholder QApplication to work '''
    cfg_app = QtWidgets.QApplication(sys.argv)
    current_path = os.path.abspath('./config')
    global_config_path = r'C:\Users\ASLM\Desktop\mesoSPIM-utsw\mesoSPIM\config\mesospim_config.py'

    if global_config_path != '':
        ''' Using importlib to load the config file '''
        spec = importlib.util.spec_from_file_location('module.name', global_config_path)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        logger.info(f'Configuration file loaded: {global_config_path}')
        return config
    else:
        ''' Application shutdown '''
        warning = QtWidgets.QMessageBox.warning(None,'Shutdown warning',
                'No configuration file selected - shutting down!',
                QtWidgets.QMessageBox.Ok)
        sys.exit()

    sys.exit(cfg_app.exec_())

def stage_referencing_check(cfg):
    if cfg.stage_parameters['stage_type'] == 'PI_rotzf_and_Galil_xy' or cfg.stage_parameters['stage_type'] == 'PI_rotz_and_Galil_xyf':
        warning = QtWidgets.QMessageBox.warning(None,'Sample z reference movement necessary!',
                'Please move the XYZ stage to position where a reference z movement (to the midpoint of the movement range) is safe!',
                QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        if warning == QtWidgets.QMessageBox.Cancel:
            shutdown_message = QtWidgets.QMessageBox.warning(None,'Shutdown warning',
                    'No reference movement - shutting down!',
                    QtWidgets.QMessageBox.Ok)
            sys.exit()
        else:
            return True
    else:
        return True

def main():
    logging.info('mesoSPIM Program started.')
    cfg = load_config()
    app = QtWidgets.QApplication(sys.argv)
    stage_referencing_check(cfg)
    ex = mesoSPIM_MainWindow(cfg)
    ex.show()
    ex.display_icons()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
