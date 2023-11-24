import os.path
import pathlib
import glob

import pandas as pd

from conf import dataset_n_features_analysis_folder, CLASSES_NAME_TO_NUMBERS_DICT


def represent_class_by_numbers(dataframe):
    dataframe['emotion_zone'] = dataframe.apply(get_class_number, axis=1)
    return dataframe


# def represent_class_by_names(dataframe):
#     dataframe['emotion_zone'] = dataframe.apply(get_class_name, axis=1)
#     return dataframe


def get_class_number(df_row):
    emotion = df_row['emotion_zone']
    return CLASSES_NAME_TO_NUMBERS_DICT[emotion]


# Datasets
# Parents
# video
parents_all_data_video_2d_eye = pd.read_csv(
    os.path.join(dataset_n_features_analysis_folder, 'parents', 'video', '2d_eye_landmark_all_data_train.csv'))

parents_all_data_video_3d_eye = pd.read_csv(
    os.path.join(dataset_n_features_analysis_folder, 'parents', 'video', '3d_eye_landmark_all_data_train.csv'))

# audio

# Specialist
