import argparse
import os
import PIL
import pdb


def convert_bin_to_jpg(img_bin_filepath):

    with open(img_bin_filepath, mode='rb') as bin_file_obj:
        
        bin_file_bytes = bin_file_obj.read()

        for idx, byte_val in enumerate(bin_file_bytes):

            if byte_val != 255:
                pdb.set_trace()



if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()
    argparse_parser.add_argument("-i", "--input-bin-file", type=str, required=True, help="The BIN file to convert to a JPG file")

    argparse_args = argparse_parser.parse_args()

    input_bin_img_filepath = argparse_args.input_bin_file

    if os.path.exists(input_bin_img_filepath):

        convert_bin_to_jpg(input_bin_img_filepath)

    else:
        raise FileNotFoundError(f"JPG file not found: '{input_bin_img_filepath}'")
    