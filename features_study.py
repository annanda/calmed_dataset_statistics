import os.path
import pathlib
import glob

import pandas as pd
from conf import dataset_n_features_folder, ANNOTATIONS, FEATURES, SESSIONS


def concatenate_train_data_per_session(annotation, modality, feature, session):
    files, read_folder = get_files_list(annotation, modality, feature, session)
    write_folder = pathlib.Path(read_folder).parent

    dfs = []
    for file in files:
        df = pd.read_pickle(file)
        dfs.append(df)

    result = pd.concat(dfs)
    result.to_csv(os.path.join(write_folder, f'{feature}_{session}_train.csv'), index=False)
    print('done!')


def concatenate_train_data_per_session_audio(annotation, modality, feature, session, feature_group):
    files, read_folder = get_files_list(annotation, modality, feature, session, feature_group)
    write_folder = pathlib.Path(read_folder).parent

    dfs = []
    for file in files:
        df = pd.read_pickle(file)
        dfs.append(df)

    result = pd.concat(dfs)
    result.to_csv(os.path.join(write_folder, f'{feature_group}_{feature}_{session}_train.csv'), index=False)
    print('done!')


def get_files_list(annotation, modality, feature, session, feature_group=None):
    if modality == 'audio':
        read_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                                   'functionals', feature_group, feature, session)
    elif modality == 'video':
        read_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                                   feature, session)
    files = glob.glob(os.path.join(read_folder, "*_train.pkl"))
    return files, read_folder


def generate_video_train_features():
    for annotation in ANNOTATIONS:
        for feature in FEATURES['video']:
            for session in SESSIONS:
                concatenate_train_data_per_session(annotation, 'video', feature, session)


def generate_audio_train_features():
    concatenate_train_data_per_session_audio('parents', 'audio', 'pitch', 'session_01_01', 'frequency')


if __name__ == '__main__':
    # generate_video_train_features()
    generate_audio_train_features()

'/Users/annanda/PycharmProjects/dataset_statistics/datasets/features_n_labels/parents/audio/individuals/non_sequential/functionals/frequency/pitch/session_01_01'
'/Users/annanda/PycharmProjects/dataset_statistics/datasets/features_n_labels/parents/audio/individuals/non_sequential/funcionals/frequency/pitch/session_01_01'