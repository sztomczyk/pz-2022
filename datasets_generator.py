
import argparse
from argparse import ArgumentParser
from csr_generator import generate_csr_matrix
import numpy as np


def generate_datasets():
    density_from = float(args.get('df'))
    density_to = float(args.get('dt'))
    step = float(args.get('st'))
    size = int(args.get('si'))
    path = str(args.get('path'))

    for n in np.arange(density_from, density_to + step, step):
        generate_csr_matrix(size, n, f'{path}/{size}x{size}_{"{:.1f}".format(n).replace(".", "_")}')


if "__main__" == __name__:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-df", help="density from", default="0.1")
    parser.add_argument("-dt", help="density to", default="1")
    parser.add_argument("-st", help="step", default="0.1")
    parser.add_argument("-si", help="size", default="4")
    parser.add_argument("-path", help="path where datasets should be generated", default="./generated")
    args: dict = vars(parser.parse_args())

    generate_datasets()
