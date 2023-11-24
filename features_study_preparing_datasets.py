import os.path
import pathlib
import glob

import pandas as pd
from conf import dataset_n_features_folder, ANNOTATIONS, FEATURES, SESSIONS, LLD_PARAMETER_GROUP, PARTICIPANTS


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
    print(f'done {feature_group}_{feature}_{session}!')


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
    for annotation in ANNOTATIONS:
        for feature_group in LLD_PARAMETER_GROUP.keys():
            for feature in LLD_PARAMETER_GROUP[feature_group]:
                for session in SESSIONS:
                    concatenate_train_data_per_session_audio(annotation, 'audio', feature, session, feature_group)


def get_path(annotation, modality, feature, session=None, feature_group=None, participant=None):
    if modality == 'audio':
        read_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                                   'functionals', feature_group, feature)
    elif modality == 'video':
        read_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                                   feature)
    if not participant:
        file_to_read = glob.glob(os.path.join(read_folder, f"*{session}_train.csv"))
    else:
        sessions = f'session_{participant}'
        file_to_read = glob.glob(os.path.join(read_folder, f"*{sessions}_*.csv"))
    return file_to_read


def concat_all_data_per_feature(annotation, modality, feature, feature_group=None):
    all_sessions_data = []
    for participant in PARTICIPANTS.keys():
        session_participant = get_path(annotation, modality, feature, feature_group=feature_group,
                                       participant=participant)
        for file in session_participant:
            pd_session_participant = pd.read_csv(file)
            all_sessions_data.append(pd_session_participant)
    result = pd.concat(all_sessions_data)

    if modality == 'audio':
        write_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                                    'functionals', feature_group, feature)
    elif modality == 'video':
        write_folder = os.path.join(dataset_n_features_folder, annotation, modality, 'individuals', 'non_sequential',
                                    feature)

    result.to_csv(os.path.join(write_folder, f'{feature_group}_{feature}_all_data_train.csv'), index=False)
    print(f'done concatenating {feature}!')


def concatenate_all_train_data_per_feature_audio():
    for annotation in ANNOTATIONS:
        for feature_group in LLD_PARAMETER_GROUP.keys():
            for feature in LLD_PARAMETER_GROUP[feature_group]:
                concat_all_data_per_feature(annotation, 'audio', feature, feature_group)


def concatenate_all_train_data_per_feature_video():
    for annotation in ANNOTATIONS:
        for feature in FEATURES['video']:
            concat_all_data_per_feature(annotation, 'video', feature)


if __name__ == '__main__':
    # file_to_read = get_path('specialist', 'audio', 'jitter', feature_group='frequency', participant='02')
    # print(file_to_read)
    # concat_all_data_per_feature('parents', 'audio', 'jitter', feature_group='frequency')
    # concatenate_all_train_data_per_feature_audio()
    # concatenate_all_train_data_per_feature_video()
    pass
