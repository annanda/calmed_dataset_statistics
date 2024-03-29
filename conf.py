import pathlib
import os.path

from decouple import config

EMOTIONS = ['blue', 'green', 'red', 'yellow']
SESSIONS = ['session_01_01', 'session_02_01', 'session_02_02', 'session_03_01', 'session_03_02', 'session_04_01',
            'session_04_02']
PARTICIPANTS = {'01': ['session_01_01'], '02': ['session_02_01', 'session_02_01'],
                '03': ['session_03_01', 'session_03_02'], '04': ['session_04_01',
                                                                 'session_04_02']}
ANNOTATIONS = ['parents', 'specialist']
MODALITIES = ['video']
FEATURES = {
    'video': ['AU', '2d_eye_landmark', '3d_eye_landmark', 'face_2d_landmarks', 'face_3d_landmarks', 'gaze',
              'head_pose'],
    'audio': []}
LLD_PARAMETER_GROUP = {
    'frequency': ['pitch', 'jitter', 'formant_1-3_frequency', 'formant_1-3_bandwidth'],
    'energy_amplitude': ['shimmer', 'loudness', 'harmonics-to-noise_ratio'],
    'spectral_balance': ['alpha_ratio', 'hammarberg_index', 'spectral_slope',
                         'formant_1-3_relative_energy', 'harmonic_difference_H1–H2',
                         'Harmonic_difference_H1–A3', 'mfcc_1–4'],
    'temporal_features': ['temporal_features']
}

CLASSES_NAME_TO_NUMBERS_DICT = {
    'blue': 0,
    'green': 1,
    'red': 2,
    'yellow': 3
}

main_folder = pathlib.Path(__file__).parent
dataset_n_features_folder = os.path.join(main_folder, 'datasets', 'features_n_labels')
dataset_n_features_analysis_folder = os.path.join(main_folder, 'datasets', 'features_n_labels_analysis')
