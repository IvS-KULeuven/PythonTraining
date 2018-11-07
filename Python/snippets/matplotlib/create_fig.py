# Examples to create figures

# Matplotlib is intended to use object orentied!
# Some concepts
#   Figure: The whole figure.
#   Axes: The 'plot' (where your data is displayed)
#   Axis: The number-line-objects (as in x-axis and y-axis)

# All plotting functions expect np.array or np.ma.masked_array as input.
# List will be converted internally. Pandas object might not work.
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.2)
y = np.sin(x)
y2 = 2 * np.sin(x)

# bad code
plt.plot(x, y)
plt.show()

# good code
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()

# easier good code
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# multiple subplots
fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
plt.show()


# you can do the same with line-objects
# this might help you for wanting to tune certain line settings
fig, ax = plt.subplots()
line, = ax.plot(x, y)  # comma is for creating a single tupple
line2, = ax.plot(x, y2)
line2.set_color('r')
plt.show()


# create functions to make your life easier
def create31fig():
    fig = plt.figure(figsize=(16, 27))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    plt.subplots_adjust(hspace=0.001)
    plt.subplots_adjust(wspace=0.001)
    ax1.set_xticklabels([])
    ax2.set_xticklabels([])
    xticklabels = ax1.get_xticklabels() + ax2.get_xticklabels()
    plt.setp(xticklabels, visible=False)
    # ax1.set_title(title)
    nbins = len(ax1.get_xticklabels())  # added
    ax2.yaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))  # added
    # ax2.set_ylabel(ylabel)
    ax3.yaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))  # added
    # ax3.set_xlabel(xlabel)

    return ax1, ax2, ax3
