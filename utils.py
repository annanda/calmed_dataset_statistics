import pandas as pd

COLOURS = ['green', 'yellow', 'red', 'blue']
EMOTIONS = ['green', 'yellow', 'red', 'blue']

# reading all the datasets
############################################
# PARENTS DATA
############################################

# session 1.1
df_11_1 = pd.read_csv('datasets/parents/session_01_01/session_01_01_01.csv')
df_11_2 = pd.read_csv('datasets/parents/session_01_01/session_01_01_02.csv')
df_11_3 = pd.read_csv('datasets/parents/session_01_01/session_01_01_03.csv')
df_11_4 = pd.read_csv('datasets/parents/session_01_01/session_01_01_04.csv')
df_11_5 = pd.read_csv('datasets/parents/session_01_01/session_01_01_05.csv')
df_11_6 = pd.read_csv('datasets/parents/session_01_01/session_01_01_06.csv')
df_11_7 = pd.read_csv('datasets/parents/session_01_01/session_01_01_07.csv')
dataframes_11 = [df_11_1, df_11_2, df_11_3, df_11_4, df_11_5, df_11_6, df_11_7]

# session 2.1
df_21_1 = pd.read_csv('datasets/parents/session_02_01/session_02_01_01.csv')
df_21_2 = pd.read_csv('datasets/parents/session_02_01/session_02_01_02.csv')
df_21_3 = pd.read_csv('datasets/parents/session_02_01/session_02_01_03.csv')
df_21_4 = pd.read_csv('datasets/parents/session_02_01/session_02_01_04.csv')
df_21_5 = pd.read_csv('datasets/parents/session_02_01/session_02_01_05.csv')
df_21_6 = pd.read_csv('datasets/parents/session_02_01/session_02_01_06.csv')
dataframes_21 = [df_21_1, df_21_2, df_21_3, df_21_4, df_21_5, df_21_6]

# session 2.2
df_22_1 = pd.read_csv('datasets/parents/session_02_02/session_02_02_01.csv')
df_22_2 = pd.read_csv('datasets/parents/session_02_02/session_02_02_02.csv')
df_22_3 = pd.read_csv('datasets/parents/session_02_02/session_02_02_03.csv')
df_22_4 = pd.read_csv('datasets/parents/session_02_02/session_02_02_04.csv')
df_22_5 = pd.read_csv('datasets/parents/session_02_02/session_02_02_05.csv')
df_22_6 = pd.read_csv('datasets/parents/session_02_02/session_02_02_06.csv')
dataframes_22 = [df_22_1, df_22_2, df_22_3, df_22_4, df_22_5, df_22_6]

# session 3.1
df_31_1 = pd.read_csv('datasets/parents/session_03_01/session_03_01_01.csv')
df_31_2 = pd.read_csv('datasets/parents/session_03_01/session_03_01_02.csv')
df_31_3 = pd.read_csv('datasets/parents/session_03_01/session_03_01_03.csv')
df_31_4 = pd.read_csv('datasets/parents/session_03_01/session_03_01_04.csv')
df_31_5 = pd.read_csv('datasets/parents/session_03_01/session_03_01_05.csv')
df_31_6 = pd.read_csv('datasets/parents/session_03_01/session_03_01_06.csv')
df_31_7 = pd.read_csv('datasets/parents/session_03_01/session_03_01_07.csv')
dataframes_31 = [df_31_1, df_31_2, df_31_3, df_31_4, df_31_5, df_31_6, df_31_7]

# session 3.2
df_32_1 = pd.read_csv('datasets/parents/session_03_02/session_03_02_01.csv')
df_32_2 = pd.read_csv('datasets/parents/session_03_02/session_03_02_02.csv')
df_32_3 = pd.read_csv('datasets/parents/session_03_02/session_03_02_03.csv')
df_32_4 = pd.read_csv('datasets/parents/session_03_02/session_03_02_04.csv')
df_32_5 = pd.read_csv('datasets/parents/session_03_02/session_03_02_05.csv')
df_32_6 = pd.read_csv('datasets/parents/session_03_02/session_03_02_06.csv')
dataframes_32 = [df_32_1, df_32_2, df_32_3, df_32_4, df_32_5, df_32_6]

# session 4.1
df_41_1 = pd.read_csv('datasets/parents/session_04_01/session_04_01_01.csv')
df_41_2 = pd.read_csv('datasets/parents/session_04_01/session_04_01_02.csv')
df_41_3 = pd.read_csv('datasets/parents/session_04_01/session_04_01_03.csv')
df_41_4 = pd.read_csv('datasets/parents/session_04_01/session_04_01_04.csv')
df_41_5 = pd.read_csv('datasets/parents/session_04_01/session_04_01_05.csv')
dataframes_41 = [df_41_1, df_41_2, df_41_3, df_41_4, df_41_5]

# session 4.2
df_42_1 = pd.read_csv('datasets/parents/session_04_02/session_04_02_01.csv')
df_42_2 = pd.read_csv('datasets/parents/session_04_02/session_04_02_02.csv')
df_42_3 = pd.read_csv('datasets/parents/session_04_02/session_04_02_03.csv')
df_42_4 = pd.read_csv('datasets/parents/session_04_02/session_04_02_04.csv')
df_42_5 = pd.read_csv('datasets/parents/session_04_02/session_04_02_05.csv')
dataframes_42 = [df_42_1, df_42_2, df_42_3, df_42_4, df_42_5]

# all data
whole_data = pd.read_csv('datasets/parents/all_data.csv')
all_train_data = pd.read_csv('datasets/parents/all_data_train.csv')
all_dev_data = pd.read_csv('datasets/parents/all_data_dev.csv')
all_test_data = pd.read_csv('datasets/parents/all_data_test.csv')

############################################
# SPECIALIST DATA
############################################


# session 1.1
df_11_1_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_01.csv')
df_11_2_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_02.csv')
df_11_3_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_03.csv')
df_11_4_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_04.csv')
df_11_5_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_05.csv')
df_11_6_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_06.csv')
df_11_7_specialist = pd.read_csv('datasets/specialist/session_01_01/session_01_01_07.csv')
dataframes_11_specialist = [df_11_1_specialist, df_11_2_specialist, df_11_3_specialist, df_11_4_specialist,
                            df_11_5_specialist, df_11_6_specialist, df_11_7_specialist]

# session 2.1
df_21_1_specialist = pd.read_csv('datasets/specialist/session_02_01/session_02_01_01.csv')
df_21_2_specialist = pd.read_csv('datasets/specialist/session_02_01/session_02_01_02.csv')
df_21_3_specialist = pd.read_csv('datasets/specialist/session_02_01/session_02_01_03.csv')
df_21_4_specialist = pd.read_csv('datasets/specialist/session_02_01/session_02_01_04.csv')
df_21_5_specialist = pd.read_csv('datasets/specialist/session_02_01/session_02_01_05.csv')
df_21_6_specialist = pd.read_csv('datasets/specialist/session_02_01/session_02_01_06.csv')
dataframes_21_specialist = [df_21_1_specialist, df_21_2_specialist, df_21_3_specialist, df_21_4_specialist,
                            df_21_5_specialist, df_21_6_specialist]

# session 2.2
df_22_1_specialist = pd.read_csv('datasets/specialist/session_02_02/session_02_02_01.csv')
df_22_2_specialist = pd.read_csv('datasets/specialist/session_02_02/session_02_02_02.csv')
df_22_3_specialist = pd.read_csv('datasets/specialist/session_02_02/session_02_02_03.csv')
df_22_4_specialist = pd.read_csv('datasets/specialist/session_02_02/session_02_02_04.csv')
df_22_5_specialist = pd.read_csv('datasets/specialist/session_02_02/session_02_02_05.csv')
df_22_6_specialist = pd.read_csv('datasets/specialist/session_02_02/session_02_02_06.csv')
dataframes_22_specialist = [df_22_1_specialist, df_22_2_specialist, df_22_3_specialist, df_22_4_specialist,
                            df_22_5_specialist, df_22_6_specialist]

# session 3.1
df_31_1_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_01.csv')
df_31_2_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_02.csv')
df_31_3_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_03.csv')
df_31_4_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_04.csv')
df_31_5_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_05.csv')
df_31_6_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_06.csv')
df_31_7_specialist = pd.read_csv('datasets/specialist/session_03_01/session_03_01_07.csv')
dataframes_31_specialist = [df_31_1_specialist, df_31_2_specialist, df_31_3_specialist, df_31_4_specialist,
                            df_31_5_specialist, df_31_6_specialist, df_31_7_specialist]

# session 3.2
df_32_1_specialist = pd.read_csv('datasets/specialist/session_03_02/session_03_02_01.csv')
df_32_2_specialist = pd.read_csv('datasets/specialist/session_03_02/session_03_02_02.csv')
df_32_3_specialist = pd.read_csv('datasets/specialist/session_03_02/session_03_02_03.csv')
df_32_4_specialist = pd.read_csv('datasets/specialist/session_03_02/session_03_02_04.csv')
df_32_5_specialist = pd.read_csv('datasets/specialist/session_03_02/session_03_02_05.csv')
df_32_6_specialist = pd.read_csv('datasets/specialist/session_03_02/session_03_02_06.csv')
dataframes_32_specialist = [df_32_1_specialist, df_32_2_specialist, df_32_3_specialist, df_32_4_specialist,
                            df_32_5_specialist, df_32_6_specialist]

# session 4.1
df_41_1_specialist = pd.read_csv('datasets/specialist/session_04_01/session_04_01_01.csv')
df_41_2_specialist = pd.read_csv('datasets/specialist/session_04_01/session_04_01_02.csv')
df_41_3_specialist = pd.read_csv('datasets/specialist/session_04_01/session_04_01_03.csv')
df_41_4_specialist = pd.read_csv('datasets/specialist/session_04_01/session_04_01_04.csv')
df_41_5_specialist = pd.read_csv('datasets/specialist/session_04_01/session_04_01_05.csv')
dataframes_41_specialist = [df_41_1_specialist, df_41_2_specialist, df_41_3_specialist, df_41_4_specialist,
                            df_41_5_specialist]

# session 4.2
df_42_1_specialist = pd.read_csv('datasets/specialist/session_04_02/session_04_02_01.csv')
df_42_2_specialist = pd.read_csv('datasets/specialist/session_04_02/session_04_02_02.csv')
df_42_3_specialist = pd.read_csv('datasets/specialist/session_04_02/session_04_02_03.csv')
df_42_4_specialist = pd.read_csv('datasets/specialist/session_04_02/session_04_02_04.csv')
df_42_5_specialist = pd.read_csv('datasets/specialist/session_04_02/session_04_02_05.csv')
dataframes_42_specialist = [df_42_1_specialist, df_42_2_specialist, df_42_3_specialist, df_42_4_specialist,
                            df_42_5_specialist]

# all data
whole_data_specialist = pd.read_csv('datasets/specialist/all_data.csv')
all_train_data_specialist = pd.read_csv('datasets/specialist/all_data_train.csv')
all_dev_data_specialist = pd.read_csv('datasets/specialist/all_data_dev.csv')
all_test_data_specialist = pd.read_csv('datasets/specialist/all_data_test.csv')


def get_value_count_dict(df_input):
    counts = df_input['emotion_zone'].value_counts()
    count_values_emotions = {'green': 0, 'blue': 0, 'yellow': 0, 'red': 0, 'video_part': None}

    for key in count_values_emotions.keys():
        try:
            count_values_emotions[key] = int(counts[key])
        except KeyError:
            count_values_emotions[key] = 0

    count_values_emotions['video_part'] = df_input['video_part'].iloc[0]
    return count_values_emotions


def get_value_count_for_labels_dict(df_input):
    counts = df_input['emotion_zone'].value_counts()
    count_values_emotions = {'green': 0, 'blue': 0, 'yellow': 0, 'red': 0}

    for key in count_values_emotions.keys():
        try:
            count_values_emotions[key] = int(counts[key])
        except KeyError:
            count_values_emotions[key] = 0

    return [count_values_emotions]


def generate_dic_to_plot(df_input):
    count_values = get_value_count_dict(df_input)

    keys = ['green', 'yellow', 'red', 'blue']
    vals = [count_values[k] for k in keys]
    total = df_input['emotion_zone'].describe()['count']
    percents = [(count_values[k] / total) * 100 for k in keys]
    return keys, vals, percents


def add_video_part_column_to_dataframes(dataframes):
    """ The list of dataframes needs to be sorted by video part
    :param dataframes: a sorted list of pandas dataframe
    :return: a list of pandas dataframes with one additional column.
    """
    # TODO fix this code to not depend on the order of the dataframes.
    i = 1
    for dataframe in dataframes:
        dataframe['video_part'] = i
        i = i + 1
    return dataframes


def create_whole_session_dict_values(dataframes):
    dataframes_list = []
    for dataframe in dataframes:
        dataframe_dict = get_value_count_dict(dataframe)
        dataframes_list.append(dataframe_dict)
    return dataframes_list


def concat_and_save_frames(frames, file_name):
    result = pd.concat(frames)
    result.to_pickle(f"./{file_name}.pkl")


def get_source_points_for_plot_from_session(session_id):
    desired_dfs_columns = []
    dataframes = 'dataframes_' + session_id
    dataframes = globals()[dataframes]
    dataframes = add_video_part_column_to_dataframes(dataframes)
    for df_session in dataframes:
        desired_dfs_columns.append(df_session[['time_of_video_seconds', 'emotion_zone', 'video_part']])

    merged_df = pd.concat(desired_dfs_columns)
    source_points = pd.melt(merged_df, id_vars=['emotion_zone', 'time_of_video_seconds'], value_vars=['video_part'])
    return source_points


def concatenate_save_data_session(session, annotation_type='parents'):
    train = pd.read_csv(f"datasets/{annotation_type}/{session}/{session}_train.csv")
    dev = pd.read_csv(f"datasets/{annotation_type}/{session}/{session}_dev.csv")
    test = pd.read_csv(f"datasets/{annotation_type}/{session}/{session}_test.csv")
    session_data = pd.concat([train, dev, test])
    session_data_clean = session_data[["session", "video_part", "time_of_video_seconds", "emotion_zone", "frametime"]]
    session_data_clean.to_csv(f"datasets/{annotation_type}/{session}.csv")


def concate_save_all_data(annotation_type='parents'):
    session_01_01 = pd.read_csv(f"datasets/{annotation_type}/session_01_01.csv")
    session_02_01 = pd.read_csv(f"datasets/{annotation_type}/session_02_01.csv")
    session_02_02 = pd.read_csv(f"datasets/{annotation_type}/session_02_02.csv")
    session_03_01 = pd.read_csv(f"datasets/{annotation_type}/session_03_01.csv")
    session_03_02 = pd.read_csv(f"datasets/{annotation_type}/session_03_02.csv")
    session_04_01 = pd.read_csv(f"datasets/{annotation_type}/session_04_01.csv")
    session_04_02 = pd.read_csv(f"datasets/{annotation_type}/session_04_02.csv")

    all_data = pd.concat(
        [session_01_01, session_02_01, session_02_02, session_03_01, session_03_02, session_04_01, session_04_02])
    all_data = all_data[["session", "video_part", "time_of_video_seconds", "emotion_zone", "frametime"]]
    all_data.to_csv(f"datasets/{annotation_type}/all_data.csv")


def concate_save_set_all_data(sessions, set_name, annotation_type='parents'):
    set_list = []
    for session in sessions:
        set_dataframe = pd.read_csv(f"datasets/{annotation_type}/{session}/{session}_{set_name}.csv")
        set_list.append(set_dataframe)
    sets_dataframe = pd.concat(set_list)
    sets_dataframe_clean = sets_dataframe[
        ["session", "video_part", "time_of_video_seconds", "emotion_zone", "frametime"]]
    sets_dataframe_clean.to_csv(f"datasets/{annotation_type}/all_data_{set_name}.csv")


if __name__ == '__main__':
    sessions = [
        'session_01_01',
        'session_02_01',
        'session_02_02',
        'session_03_01',
        'session_03_02',
        'session_04_01',
        'session_04_02',
    ]
    # for session in sessions:
    #     concatenate_save_data_session(session)
    # print('testing')
    concate_save_all_data()
    sets = ['train', 'dev', 'test']
    # for set_name in sets:
    #     concate_save_set_all_data(sessions, set_name)

##################################
# Only run the lines below when needing to create a new dataset
##################################

# frames_with_video_part = add_column_to_frames(frames_original)
# concat_and_save_frames(frames_with_video_part, "dataset_session_01")
