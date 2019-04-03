from sklearn import datasets

import K_Means, Plot

blobs=datasets.make_blobs()[0]
centers, clusters, colors, color_labels=K_Means.k_means(blobs, 3)
Plot.plot(blobs, centers, colors, color_labels)