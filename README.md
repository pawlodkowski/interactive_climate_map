# Making Interactive Choropleth Maps with Temperature Data

In this tutorial, you have the option to explore up to 3 different visualization
libraries in Python, with the task of generating an interactive [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map) of
temperature data.

This activity pairs nicely with time series analysis of temperature data, since this
kind of data can easily be plotted on a map (assuming you can aggregate data on a
country name level).

This repository contains step-by-step, fill-in-the-blank instructions for reading, manipulating, and generating geographic data in **GeoPandas**, and visualizing this data with
the library of your choice:

1. **Folium**
2. **Plotly**
3. **Bokeh**

Of course, you can try all 3 of them. The goal of these tutorials is not so
much to learn the syntax of these -- *quite complex* -- libraries (that is why
a lot of boilerplate code is mostly already set up for you), but rather to learn
some concepts behind interactive, browser-based visualization libraries in Python
(as opposed to "static" libraries like matplotlib or seaborn) and to get a *taste*
of what is possible with these libraries. Plus, knowing more advanced data visualization
tools generally makes you a better Data Scientist.

Here is a quick, high-level overview of the 3 libraries found in this repo
that you can use for plotting nice interactive choropleth maps:

| Library | Difficulty | Has Web Server / Back-End? | Front-End Framework | Features / Comments |
| - | :--: | :--: | :--: | :--: |
| [Folium][1] | Easy | No | Leaflet.js | Easy-to-use. Maps only. |
| [Plotly][2] | Medium | No | Plotly.js | Comprehensive vizualization library; includes many types of graphs and charts |
| [Plotly/Dash][3] | Hard | Yes (Flask) | React.js | Powerful framework for building entire web applications (back- and front-end). Built on top of Plotly. |
| [Bokeh][4] | Hard | Yes (Tornado) | BokehJS | Powerful interactive visualization library (also back- and front-end). Older / more established. |

### And what about [GeoPandas][5]?

GeoPandas is not an interactive visualization library (though
it can be used to plot simple, static maps); rather, it's a powerful library used for working
with geospatial data in Python.

Each of the 3 tutorials begin with the exact same steps:
using GeoPandas to read in a *shapefile* and convert it to a so-called [GeoDataFrame](https://geopandas.org/reference/geopandas.GeoDataFrame.html) (the library is built on top of Pandas)
so that we can perform all the convenient data wrangling operations we're already used to, such
as filtering, grouping, and merging.

The fundamental difference between a regular Pandas
*DataFrame* and a speciazlied *GeoDataFrame*, however, is that the the latter understands
geometric data types such as Points, Lines, and Polygons, and can easily perform geometric /
spatial operations on them.

And what's really nice for us, is once the GeoDataFrame is in
the shepe and format we want, we can easily export it to a [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) file -- a data format that most interactive, JavaScript-based visualization
libraries (like the 3 above) require for making maps.

Using GeoPandas (for pre-processing) and one of the 3 visualization libraries (for making maps)
is a powerful combination that provides a nice introduction into the field of
[GIS](https://en.wikipedia.org/wiki/Geographic_information_system), without having
to invest a lot of time in using full-blown solutions like [QGIS](https://en.wikipedia.org/wiki/QGIS)
or any of the proprietary [ESRI](https://en.wikipedia.org/wiki/Esri) products.



[1]: https://python-visualization.github.io/folium/

[2]: https://plotly.com/python/

[3]: https://plotly.com/dash/

[4]: https://bokeh.org/

[5]: https://geopandas.org/
