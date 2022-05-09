# python csr_generator.py -s {rozmiar} -d {gestosc np 0.5} -o {nazwa pliku}

from scipy import stats, io
from scipy.sparse import random
from numpy.random import default_rng
import argparse
from argparse import ArgumentParser


def generate_csr_matrix(m_size=None, m_density=None, f_output=None):
    matrix_size = m_size if m_size else int(args.get('s'))
    density = m_density if m_density else float(args.get('d'))
    output = f_output if f_output else args.get('o')

    rng = default_rng()
    rvs = stats.poisson(100, loc=0).rvs

    matrix = random(matrix_size, matrix_size, density=density, random_state=rng, data_rvs=rvs)

    # print(matrix.A)
    io.mmwrite(output, matrix.toarray())


if "__main__" == __name__:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-s", help="matrix size", default="4")
    parser.add_argument("-d", help="density", default="0.5")
    parser.add_argument("-o", help="output file", default="./generated/4x4_0_5")
    args: dict = vars(parser.parse_args())

    generate_csr_matrix()
