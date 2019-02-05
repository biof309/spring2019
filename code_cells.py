# %% Plot
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()



#%% Letters
[chr(i+65) for i in range(26)]


#%% names: interests dictionary
d = {
       'Mike': 'genomics',
       'Becky': 'physics',
       'Diane': 'metabolomics'
       }

#%% Search dictionary for close matches
import difflib
def search_dict(query, dictionary, cutoff=0.8):
       return [key for key, value in dictionary.items() if value in difflib.get_close_matches(query, dictionary.values(), cutoff=cutoff)]
matches = search_dict('omics', d, cutoff=0.55)
#%%
import pathlib
pathlib.Path('interested_in_.txt').write_text(matches)
