import numpy as np

'''
mesoSPIM configuration file.
'''

waveformgeneration = 'NI'  # 'DemoWaveFormGeneration' or 'NI'

acquisition_hardware = {'master_trigger_out_line': 'PXI6259/port0/line1',
                        'camera_trigger_source': '/PXI6259/PFI0',
                        'camera_trigger_out_line': '/PXI6259/ctr0',
                        'galvo_etl_task_line': 'PXI6259/ao0:3',
                        'galvo_etl_task_trigger_source': '/PXI6259/PFI0',
                        'laser_task_line': 'PXI6733/ao0:7',
                        'laser_task_trigger_source': '/PXI6259/PFI0'}

'''
Human interface device (Joystick)
'''
sidepanel = 'Demo'  # 'Demo' or 'FarmSimulator'

laser = 'NI'
laserdict = {'445 nm': 'PXI6733/port0/line2',
             '488 nm': 'PXI6733/port0/line3',
             '515 nm': 'PXI6733/port0/line4',
             '561 nm': 'PXI6733/port0/line5',
             '594 nm': 'PXI6733/port0/line6',
             '647 nm': 'PXI6733/port0/line7'}

laser_designation = {'445 nm': 0,
                     '488 nm': 1,
                     '515 nm': 2,
                     '561 nm': 3,
                     '594 nm': 4,
                     '647 nm': 5,
                     'Empty 0': 6,
                     'Empty 1': 7
                     }

galvo_etl_designation = {'Galvo-L': 0,
                         'Galvo-R': 1,
                         'ETL-L': 2,
                         'ETL-R': 3,
                         }
# 'Demo' or 'NI'
shutter = 'NI'
shutterdict = {'shutter_left': 'PXI6259/port0/line0',
               'shutter_right': 'PXI6259/port2/line0'}

shutteroptions = ('Left', 'Right', 'Both')

camera = 'HamamatsuOrca'  # 'DemoCamera' or 'HamamatsuOrca' or 'PhotometricsIris15'
camera_parameters = {'x_pixels': 2304,
                     'y_pixels': 2304,
                     'x_pixel_size_in_microns': 6.5,
                     'y_pixel_size_in_microns': 6.5,
                     'subsampling': [1, 2, 4],
                     'camera_id': 0,
                     'sensor_mode': 12,  # 12 for progressive
                     'defect_correct_mode': 2,
                     'binning': '1x1',
                     'readout_speed': 1,
                     'trigger_active': 1,
                     'trigger_mode': 1,  # it is unclear if this is the external lightsheeet mode - how to check this?
                     'trigger_polarity': 2,  # positive pulse
                     'trigger_source': 2,  # external
                     }

binning_dict = {'1x1': (1, 1), '2x2': (2, 2), '4x4': (4, 4)}

stage_parameters = {'stage_type': 'PI',  # 'DemoStage' or 'PI' or other configs found in mesoSPIM_serial.py
                    'startfocus': 70700,
                    'y_load_position': 90000,
                    'y_unload_position': 10000,
                    'x_max': 50000,
                    'x_min': 2000,
                    'y_max': 100000,
                    'y_min': 2000,
                    'z_max': 50000,
                    'z_min': 2000,
                    'f_max': 100000,
                    'f_min': 2000,
                    'theta_max': 360,
                    'theta_min': 0,
                    'x_rot_position': 2000,
                    'y_rot_position': 2000,
                    'z_rot_position': 2000,
                    }

pi_parameters = {'controllername': 'C-884',
                 'stages': ('L-509.20DG10', 'L-509.40DG10', 'L-509.20DG10', 'M-060.DG', 'M-406.4PD', 'NOSTAGE'),
                 'refmode': ('FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'FRF',),
                 'serialnum': '119060508',
                 }

'''
Filterwheel configuration
For a DemoFilterWheel, no COMport needs to be specified, for a Ludl Filterwheel,
a valid COMport is necessary, e.g., 'COM53'.
'DemoFilterWheel' or 'Ludl' or 'Sutter'
'''

# Sutter
filterwheel_parameters = {'filterwheel_type': 'Sutter', 'COMport': 'COM1'}
filterdict = {'Empty-Alignment': 0,  # Every config should contain this
              'GFP - FF01-515/30-32': 1,
              'RFP - FF01-595/31-32': 2,
              'Far-Red - BLP01-647R/31-32': 3,
              'Blocked1': 4,
              'Blocked2': 5,
              'Blocked3': 6,
              'Blocked4': 7,
              'Blocked5': 8,
              'Blocked6': 9}

'''
Zoom configuration
'''

'''
For the DemoZoom, servo_id, COMport and baudrate do not matter. For a Dynamixel zoom,
these values have to be there
'''
zoom_parameters = {'zoom_type': 'DemoZoom',  # 'DemoZoom' or 'Dynamixel'
                   'servo_id': 4,
                   'COMport': 'COM38',
                   'baudrate': 1000000}

'''
The keys in the zoomdict define what zoom positions are displayed in the selection box
(combobox) in the user interface.
'''

zoomdict = {'0.63x': 3423,
            '0.8x': 3071,
            '1x': 2707,
            '1.25x': 2389,
            '1.6x': 2047,
            '2x': 1706,
            '2.5x': 1354,
            '3.2x': 967,
            '4x': 637,
            '5x': 318,
            '6.3x': 0}
'''
Pixelsize in micron
'''
pixelsize = {'0.63x': 10.169,
             '0.8x': 7.9,
             '1x': 6.27,
             '1.25x': 5.10,
             '1.6x': 3.999,
             '2x': 3.184,
             '2.5x': 2.568,
             '3.2x': 2.016,
             '4x': 1.623,
             '5x': 1.287,
             '6.3x': 1.038}

'''
Initial acquisition parameters

Used as initial values after startup

When setting up a new mesoSPIM, make sure that:
* 'max_laser_voltage' is correct (5 V for Toptica MLEs, 10 V for Omicron SOLE)
* 'galvo_l_amplitude' and 'galvo_r_amplitude' (in V) are correct (not above the max input allowed by your galvos)
* all the filepaths exist
* the initial filter exists in the filter dictionary above
'''

startup = {
    'state': 'init',  # 'init', 'idle' , 'live', 'snap', 'running_script'
    'samplerate': 100000,
    'sweeptime': 0.2,
    'position': {'x_pos': 0, 'y_pos': 0, 'z_pos': 0, 'f_pos': 0, 'theta_pos': 0},
    'ETL_cfg_file': 'C:/Users/ASLM/Desktop/mesoSPIM-utsw/mesoSPIM/config/etl_parameters/ETL-parameters.csv',
    'filepath' : 'C:/Users/ASLM/Desktop/Data/file.raw',
    'folder' : 'C:/Users/ASLM/Desktop/Data',
    'snap_folder': 'C:/Users/ASLM/Desktop/Data',
    'file_prefix': '',
    'file_suffix': '000001',
    'zoom': '1x',
    'pixelsize': 6.55,
    'laser': '488 nm',
    'max_laser_voltage': 10,
    'intensity': 10,
    'shutterstate': False,  # Is the shutter open or not?
    'shutterconfig': 'Right',  # Can be "Left", "Right","Both","Interleaved"
    'laser_interleaving': False,
    'filter': 'Empty-Alignment',
    'etl_l_delay_%': 7.5,
    'etl_l_ramp_rising_%': 85,
    'etl_l_ramp_falling_%': 2.5,
    'etl_l_amplitude': 0.7,
    'etl_l_offset': 2.3,
    'etl_r_delay_%': 2.5,
    'etl_r_ramp_rising_%': 5,
    'etl_r_ramp_falling_%': 85,
    'etl_r_amplitude': 0.65,
    'etl_r_offset': 2.36,
    'galvo_l_frequency': 99.9,
    'galvo_l_amplitude': 2.5,
    'galvo_l_offset': 0,
    'galvo_l_duty_cycle': 50,
    'galvo_l_phase': np.pi / 2,
    'galvo_r_frequency': 99.9,
    'galvo_r_amplitude': 2.5,
    'galvo_r_offset': 0,
    'galvo_r_duty_cycle': 50,
    'galvo_r_phase': np.pi / 2,
    'laser_l_delay_%': 10,
    'laser_l_pulse_%': 87,
    'laser_l_max_amplitude_%': 100,
    'laser_r_delay_%': 10,
    'laser_r_pulse_%': 87,
    'laser_r_max_amplitude_%': 100,
    'camera_delay_%': 10,
    'camera_pulse_%': 1,
    'camera_exposure_time': 0.01,
    'camera_line_interval': 0.000075,
    'camera_display_live_subsampling': 1,
    'camera_display_snap_subsampling': 1,
    'camera_display_acquisition_subsampling': 2,
    'camera_binning': '1x1',
    'camera_sensor_mode': 'ASLM',
    'average_frame_rate': 4.969,
}
