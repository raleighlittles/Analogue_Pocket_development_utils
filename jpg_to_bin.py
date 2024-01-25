import argparse
import os
import PIL



def convert_img_to_bin(img_filepath):



if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()
    argparse_parser.add_argument("-i", "--input-jpg-file", type=str, required=True, help="The JPG file to convert to a BIN file")

    argparse_args = argparse_parser.parse_args()

    input_jpg_filepath = argparse_args.input_jpg_file

    if os.path.exists(input_jpg_filepath):
        pass

    else:
        raise FileNotFoundError(f"JPG file not found: '{input_jpg_filepath}'")
    