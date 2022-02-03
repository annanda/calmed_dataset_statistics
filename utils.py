import pandas as pd

COLOURS = ['green', 'yellow', 'red', 'blue']


def get_value_counts(df_input):
    counts = df_input['emotion_zone'].value_counts()
    count_values_emotions = {'green': 0, 'blue': 0, 'yellow': 0, 'red': 0, 'video_part': None}

    for key in count_values_emotions.keys():
        try:
            count_values_emotions[key] = int(counts[key])
        except KeyError:
            count_values_emotions[key] = 0

    count_values_emotions['video_part'] = df_input['video_part'].iloc[0]
    return count_values_emotions


def generate_dic_to_plot(df_input):
    count_values = get_value_counts(df_input)

    keys = ['green', 'yellow', 'red', 'blue']
    vals = [count_values[k] for k in keys]
    total = df_input['emotion_zone'].describe()['count']
    percents = [(count_values[k] / total) * 100 for k in keys]
    return keys, vals, percents


def add_column_to_frames(frames):
    i = 1
    for frame in frames:
        frame['video_part'] = i
        i = i + 1
    return frames


def concat_and_save_frames(frames, file_name):
    result = pd.concat(frames)
    result.to_pickle(f"./{file_name}.pkl")

##################################
# Only run the lines below when needing to create a new dataset
##################################

# frames_with_video_part = add_column_to_frames(frames_original)
# concat_and_save_frames(frames_with_video_part, "dataset_session_01")
