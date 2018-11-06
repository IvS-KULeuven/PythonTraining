# Example of global figure settings
# https://matplotlib.org/users/customizing.html

# based on matplotlib 2.0.2
# some options might not be available in older versions
# Note: matplotlib 3.0.0 already exists! Use this one.
import matplotlib.pyplot as plt

font = {'size': 40}
text = {'usetex': True}
lines = {'linewidth': 8, 'markersize': 8, 'markeredgewidth': 1, 'scale_dashes': True}
axes = {'xmargin': 0}
markers = {'fillstyle': 'none'}
# savefig = {'dpi': 220, 'format': 'png', 'transparent': True,'bbox': 'tight'}
savefig = {'format': 'pdf', 'transparent': False, 'bbox': 'tight'}
figure = {'figsize': (16, 9)}
legend = {'markerscale': 1.5, 'numpoints': 1, 'fontsize': 'xx-small',
          'frameon': False, 'handlelength': 3.1, 'handletextpad': 0.8,
          'columnspacing': 1.5}
xtick = {'top': True}
ytick = {'right': True}


plt.rc('font', **font)
plt.rc('markers', **markers)
plt.rc('text', **text)
plt.rc('lines', **lines)
plt.rc('savefig', **savefig)
plt.rc('figure', **figure)
plt.rc('legend', **legend)
plt.rc('axes', **axes)
plt.rc('xtick', **xtick)
plt.rc('ytick', **ytick)
plt.rc('xtick.major', size=10, width=1.5)
plt.rc('xtick.minor', size=5, width=1.5)
plt.rc('ytick.major', size=10, width=1.5)
plt.rc('ytick.minor', size=5, width=1.5)
