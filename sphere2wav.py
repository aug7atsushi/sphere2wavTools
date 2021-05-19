import argparse
import glob
import os
import re
import subprocess

def func(args):
    for i, inputFilePath in enumerate(glob.glob(os.path.join(args.input_dir, '**'), recursive=True)):
        if re.search('.wv\d', inputFilePath):
            # filename = os.path.split(inputFilePath)[1]
            # filename = re.sub('.wv[0-9]','.wav',filename)
            outFilePath = re.sub('.wv[0-9]','.wav',inputFilePath)
            # outFilePath = os.path.join(args.input_dir, filename)
            print(i, inputFilePath, outFilePath)
            result = subprocess.run(['./sph2pipe_v2.5/sph2pipe', inputFilePath, outFilePath])
            os.remove(inputFilePath)


def main():
    parser = argparse.ArgumentParser(description='Convert sphere format(wv1|wv2) to wav format', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input_dir', help='path where sphere format files are placed', required=True)
    # parser.add_argument('-o', '--output_dir', help='path where wav format files are placed', required=True)
    parser.set_defaults(func=func)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()