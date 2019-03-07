#!/usr/bin/env python

pipeline="""{
  "pipeline": [
    {
        "type": "readers.las",
        "filename": "https://github.com/PDAL/data/blob/master/autzen/stadium-utm.laz?raw=true"
    },
    {
        "type": "filters.sort",
        "dimension": "Z"
    }
  ]
}"""



import pdal
r = pdal.Pipeline(pipeline)
r.validate()
r.execute()
arrays = r.arrays


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from io import BytesIO

def make_plot(dimensions, filename, dpi=300):
    figure_position = 1
    row = 1
    fig = plt.figure(figure_position, figsize=(6, 8.5), dpi=dpi)
    keys = dimensions.dtype.fields.keys()

    for key in keys:
        dimension = dimensions[key]
        ax = fig.add_subplot(len(keys), 1, row)

        n, bins, patches = ax.hist( dimension, 30,
                                    normed=0,
                                    facecolor='grey',
                                    alpha=0.75,
                                    align='mid',
                                    histtype='stepfilled',
                                    linewidth=None)

        ax.set_ylabel(key, size=10, rotation='horizontal')
        ax.get_xaxis().set_visible(False)
        ax.set_yticklabels('')
        ax.set_yticks((),)
        ax.set_xlim(min(dimension), max(dimension))
        ax.set_ylim(min(n), max(n))
        row = row + 1
        figure_position = figure_position + 1
    output = BytesIO()
    plt.savefig(output,format="PNG")

    o = open(filename, 'wb')
    o.write(output.getvalue())
    o.close()
    return True


make_plot(arrays[0], 'histogram.png')