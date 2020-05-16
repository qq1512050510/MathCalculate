import matplotlib
import matplotlib.cm as cm
from matplotlib import pyplot as plt


lst = [1.9378076554115014, 1.2084586588892861, 1.2133096565896173, 1.2427632053442292,
       1.1809971732733273, 0.91960143581348919, 1.1106310149587162, 1.1106310149587162,
       1.1527004351293346, 0.87318084435885079, 1.1666132876686799, 1.1666132876686799]

minima = min(lst)
maxima = max(lst)

norm = matplotlib.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
mapper = cm.ScalarMappable(norm=norm, cmap=cm.Greys_r)

#for v in lst:
   # print(mapper.to_rgba(v))
