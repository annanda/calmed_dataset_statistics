import os.path
import pathlib
import glob

import pandas as pd

EMOTIONS = ['blue', 'green', 'red', 'yellow']
SESSIONS = ['session_01_01', 'session_02_01', 'session_02_01']
PARTICIPANTS = {1: ['session_01_01'], 2: ['session_02_01', 'session_02_01']}
ANNOTATIONS = ['parents', 'specialist']

main_folder = pathlib.Path(__file__).parent
dataset_n_features_folder = os.path.join(main_folder, 'datasets', 'features_n_labels')


def concatenate_train_data_per_session(annotation, modality, feature, session):
    read_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                               feature, session)
    write_folder = pathlib.Path(read_folder).parent

    files = glob.glob(os.path.join(read_folder, "*_train.pkl"))
    dfs = []
    for file in files:
        df = pd.read_pickle(file)
        dfs.append(df)

    result = pd.concat(dfs)
    result.to_csv(os.path.join(write_folder, f'{feature}_{session}_train.csv'), index=False)
    print('hi')


if __name__ == '__main__':
    concatenate_train_data_per_session('parents', 'video', 'AU', 'session_01_01')
