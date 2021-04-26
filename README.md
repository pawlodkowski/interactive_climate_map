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
much to learn the syntax of these -- _quite complex_ -- libraries (that is why
a lot of boilerplate code is mostly already set up for you), but rather to learn
some concepts behind interactive, browser-based visualization libraries in Python
(as opposed to "static" libraries like matplotlib or seaborn) and to get a _taste_
of what is possible with these libraries. Plus, knowing more advanced data visualization
tools generally makes you a better Data Scientist.

Here is a quick, high-level overview of the 3 libraries found in this repo
that you can use for plotting nice interactive choropleth maps:

| Library          | Difficulty | Has Web Server / Back-End? | Front-End Framework |                                          Features / Comments                                           |
| ---------------- | :--------: | :------------------------: | :-----------------: | :----------------------------------------------------------------------------------------------------: |
| [Folium][1]      |    Easy    |             No             |     Leaflet.js      |                                        Easy-to-use. Maps only.                                         |
| [Plotly][2]      |   Medium   |             No             |      Plotly.js      |             Comprehensive vizualization library; includes many types of graphs and charts              |
| [Plotly/Dash][3] |    Hard    |        Yes (Flask)         |      React.js       | Powerful framework for building entire web applications (back- and front-end). Built on top of Plotly. |
| [Bokeh][4]       |    Hard    |       Yes (Tornado)        |       BokehJS       |    Powerful interactive visualization library (also back- and front-end). Older / more established.    |

### Final Results

##### Folium

![folium_demo.gif](img/folium_demo.gif)

##### Plotly

![plotly_demo.gif](img/plotly_demo.gif)

##### Bokeh

![bokeh_demo.gif](img/bokeh_demo.gif)

### And what about [GeoPandas][5]?

GeoPandas is not an interactive visualization library (though
it can be used to plot simple, static maps); rather, it's a powerful library used for working
with geospatial data in Python.

Each of the 3 tutorials begin with the exact same steps:
using GeoPandas to read in a _shapefile_ and convert it to a so-called "[GeoDataFrame](https://geopandas.org/reference/geopandas.GeoDataFrame.html)" (the library is built on top of Pandas)
so that we can perform all the convenient data wrangling operations we're already used to, such
as filtering, grouping, and merging.

The fundamental difference between a regular Pandas
_DataFrame_ and a specialized _GeoDataFrame_, however, is that the the latter understands
geometric data types such as Points, Lines, and Polygons, and can easily perform geometric /
spatial operations on them.

And what's really nice for us, is once the GeoDataFrame is in
the shape and format we want, we can easily export it to a [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) file -- a data format that most interactive, JavaScript-based visualization
libraries (like the 3 above) require for making maps.

Using GeoPandas (for pre-processing) and one of the 3 visualization libraries (for making maps)
is a powerful combination that provides a nice introduction into the field of
[GIS](https://en.wikipedia.org/wiki/Geographic_information_system), without having
to invest a lot of time in using full-blown solutions like [QGIS](https://en.wikipedia.org/wiki/QGIS)
or any of the proprietary [ESRI](https://en.wikipedia.org/wiki/Esri) products.

### Getting Started

Clone this repository and navigate inside:

```bash
git clone https://github.com/pawlodkowski/interactive_climate_map.git

cd interactive_climate_map/
```

#### Option A: Running in Docker (Recommended)

If you have Docker, you can execute all the code and follow the tutorial using a custom Docker container that is running Jupyter Lab and has all dependencies installed. This will spare you from having to install any libraries on your machine / avoid any potential installation issues (e.g. *geopandas*).

*NOTE: The custom Docker Image is still being tweaked, and has only been tested so far on the Plotly tutorial!*

To try it out, first build the image:

```bash
docker build -t geo_notebook .
```

Then run the container:

```bash
docker run -it --rm -p 8888:8888 -v "$PWD":/home/jovyan/work geo_notebook
```

Find the appropriate URL from the command-line instructions (e.g. `http://127.0.0.1:8888/lab?token=xxxxx`) and open it in your web-browser. 

#### Option B: Running locally

If you'd prefer to run the tutorials locally without Docker, simply launch Jupyter Notebook (or Lab) at the root of the repository, e.g.:

```bash
jupyter lab
```

Keep in mind, however, that you will need to install the python libraries (e.g. *geopandas*, *plotly*) yourself. You will find installation instructions as you follow the tutorials.

### Browse the different tutorials

Pick one (or more) of the libraries you'd like to try out, and then navigate
into its respective sub-directory:

1. [folium/](folium/)
2. [plotly/](plotly/)
3. [bokeh/](bokeh/)

_Note that the the content for Plotly/Dash is also included in [plotly/](plotly/) directory.
However, the tutorial for it is not yet written; though I've included some helpful resources
on how to get started_.

Once you've navigated to the appropriate directory, open up the corresponding Jupyter Notebook
(`.ipynb`) file. Follow the step-by-step tutorial with the notebook, which includes:

- Installation Instructions
  - You can ignore this if you are already running through Docker.
- Data Wrangling with GeoPandas (Steps 1-4)
  - **This is done as an in-class exercise**. Also, these steps are identical
    for each of the tutorials.
- Making the Interactive Choropleth Map (Steps 5-end)
  - **This is done as a self-guided activity** after the lesson (though
    a teacher will of course be available in the classroom for debugging support!)

### Data

The data for this particular lesson is **synthetic** / **fake!** It was originally scraped from [Berkeley Earth](http://berkeleyearth.lbl.gov/country-list/), but then regenerated based a simple polynomial trend and monthly seasonality modeled from the original data source & injected with random noise. Hence, the data in this repo is somewhat realistic but not authentic.

- This was done in the interest of protecting the original data source / preventing its redistribution.

### Credits

Most of the code here was either written or adapted (from outside sources, e.g. library documentation, published tutorials) by **Paul Wlodkowski**, Data Science Instructor @ Spiced Academy in Berlin. 

Some parts of the tutorials were based off code snippets made by fellow colleagues at Spiced Academy. More detailed credits can be found in the respective Jupyter Notebooks.

### License

Work in this repository is published under the conditions of the MIT license. 

---

[1]: https://python-visualization.github.io/folium/
[2]: https://plotly.com/python/
[3]: https://plotly.com/dash/
[4]: https://bokeh.org/
[5]: https://geopandas.org/
