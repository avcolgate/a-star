
# Importing the Library
  
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 8]
y = [1, 5, 2, 8, 3, 5, 2, 7]
plt.figure(figsize=(4, 3))

plt.plot(x, y)

# Selecting the axis-X making the bottom and top axes False.
plt.tick_params(axis='x', which='both', bottom=False,
				top=False, labelbottom=False)

# Selecting the axis-Y making the right and left axes False
plt.tick_params(axis='y', which='both', right=False,
				left=False, labelleft=False)

# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['right', 'top', 'bottom', 'left']:
	plt.gca().spines[pos].set_visible(False)
plt.show()
