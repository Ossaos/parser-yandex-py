import parse_har
import os
from config import _INPUT_DIR_, _OUTPUT_DIR_
# for every item in input that has an .har extension name
# run parser


def parse_input(input_dir, output_dir):
    cwd = os.getcwd()
    input_dir = os.path.join(cwd, input_dir)
    contents = os.listdir(input_dir)
    for file in contents:
        if file[-4:] == ".har":
            har_dict = parse_har.open_har(os.path.join(input_dir, file))
            df = parse_har.har_to_pdDf(har_dict)
            parse_har.save_to_excel(df, file, save_to=output_dir)


if __name__ == "__main__":
    parse_input(_INPUT_DIR_, _OUTPUT_DIR_)
