
import argparse
from argparse import ArgumentParser
from csr_generator import generate_csr_matrix


def generate_datasets():
    range_from = int(args.get('rf'))
    range_to = int(args.get('rt'))
    step = int(args.get('s'))
    density = float(args.get('d'))
    path = str(args.get('path'))

    for n in range(range_from, range_to + step, step):
        generate_csr_matrix(n, density, f'{path}/{n}x{n}_{str(density).replace(".", "_")}')


if "__main__" == __name__:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-rf", help="range from", default="10")
    parser.add_argument("-rt", help="range to", default="100")
    parser.add_argument("-s", help="step", default="10")
    parser.add_argument("-d", help="density", default="0.5")
    parser.add_argument("-path", help="path where datasets should be generated", default="./generated")
    args: dict = vars(parser.parse_args())

    generate_datasets()
