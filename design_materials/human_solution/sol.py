import pandas
from core.tools.utils import file_utils as fu
from core.tools.preprocess import detection
from core.tools.preprocess import compression
from core.tools.measure import jump_lengths, home_location


def run1_2(input_file):
    table = pandas.read_csv(input_file, header="infer")
    grouped_table = table.groupby("uid")
    print(grouped_table.size())

def run1_3(input_file):
    table = pandas.read_csv(input_file, header="infer")
    table["datetime"] = pandas.to_datetime(table["datetime"])
    table["datetime"] = table["datetime"].dt.date
    grouped_table = table.groupby(["uid", "datetime"])
    user_date_count = dict()

    for uid, group in grouped_table:
        if uid[0] not in user_date_count:
            user_date_count[uid[0]] = 0
        user_date_count[uid[0]] += 1
    print(user_date_count)

def run1_4(input_file, output_file):
    ddf = detection.stop_detection(input_file, output_file, 10, 0.05)
    print(ddf)
    
def run1_5(input_file, output_file):
    cdf = compression.compression(input_file, output_file, 0.2)
    print(cdf)

def run1_6(input_file, output_file):
    array = jump_lengths.jump_lengths(input_file, output_file)
    print(array)

def run1_7(input_file, output_file):
    array = home_location.home_location(input_file, output_file)
    print(array)

def run1_8(input_file, output_file):
    array = home_location.home_location(input_file, output_file, 0.5)
    print(array)