"""
This is a script
that shows how to use code cells.
"""

# %% Import some stuff
import matplotlib.pyplot as plt
import numpy as np

# %% Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
# a comment
# %% Set up plot
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

# %% Show plot
# fig.savefig("test.png")
plt.show()

chr(65)
range(26)
# %% Letters
LETTERS = [chr(i + 65) for i in range(26)]
letters = [chr(i + 97) for i in range(26)]
a, b, *end = letters
*_, y, z = letters

# %% names: interests dictionary
d = {
    'Mike': 'genomics',
    'Becky': 'physics',
    'Diane': 'metabolomics'
}

d = dict(Martin='Zumba', Martin2='Zumba')

# %% Search dictionary for close matches
import difflib


def search_dict(query, dictionary, cutoff=0.8):
    return [key for key, value in dictionary.items() if
            value in difflib.get_close_matches(query, dictionary.values(), cutoff=cutoff)]


matches = search_dict('omics', d, cutoff=0.55)
# %%
import pathlib

pathlib.Path('interested_in_.txt').write_text('\n'.join(matches))

# %%
