"""Original source: http://bkanuka.com/articles/native-latex-plots/"""
import math

import matplotlib as mpl


mpl.use('pgf')


def figsize(scale):
    # Get this from LaTeX using \the\textwidth
    fig_width_pt = 469.755
    # Convert pt to inch
    inches_per_pt = 1.0 / 72.27
    # Aesthetic ratio (you could change this)
    golden_mean = (math.sqrt(5.0) - 1.0) / 2.0
    # Width in inches
    fig_width = fig_width_pt * inches_per_pt * scale
    # Height in inches
    fig_height = fig_width * golden_mean
    fig_size = [fig_width, fig_height]
    return fig_size


pgf_with_latex = {                      # setup matplotlib to use latex for output
    'pgf.texsystem': 'pdflatex',        # change this if using xetex or lautex
    'text.usetex': True,                # use LaTeX to write all text
    'font.family': 'serif',
    'font.serif': [],                   # blank entries should cause plots to inherit fonts from the document
    'font.sans-serif': [],
    'font.monospace': [],
    'axes.labelsize': 10,               # LaTeX default is 10pt font.
    'font.size': 10,
    'legend.fontsize': 8,               # Make the legend/label fonts a little smaller
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.figsize': figsize(0.8),     # default fig size of 0.8 textwidth
    'pgf.preamble': [
        r'\usepackage[utf8x]{inputenc}',    # use utf8 fonts becasue your computer can handle it :)
        r'\usepackage[T1]{fontenc}',        # plots will be generated using this preamble
    ]
}
mpl.rcParams.update(pgf_with_latex)


def new_fig(width):
    import matplotlib.pyplot as plt

    plt.clf()
    fig = plt.figure(figsize=figsize(width))
    ax = fig.add_subplot(111)
    return fig, ax


def save_fig(filename, dpi=200, tight=True):
    import matplotlib.pyplot as plt

    if tight:
        plt.tight_layout()

    plt.savefig('{}.pdf'.format(filename))
    plt.savefig('{}.pgf'.format(filename))
    plt.savefig('{}.png'.format(filename), dpi=dpi)
