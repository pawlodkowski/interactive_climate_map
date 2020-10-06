"""In the terminal, run:
``bokeh serve --show bokeh_tutorial_solution.py``
"""

import pandas as pd
import geopandas as gpd

from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
from bokeh.palettes import brewer
from bokeh.models import LinearColorMapper, ColorBar, Slider, HoverTool
from bokeh.layouts import widgetbox, column
from bokeh.io import curdoc

SHAPEFILE = '../data/ne_110m_admin_0_countries.shp'

df = pd.read_csv('../data/all_country_temp_data_CLEAN.csv')
df = df.groupby(['country', 'year'])[['monthly_anomaly']].mean().reset_index()

gdf = gpd.read_file(SHAPEFILE)[['ADMIN', 'geometry']]
gdf.columns = ['country', 'geometry']

gdf = pd.merge(left=gdf, right=df, how='left', on='country')

# OPTIMIZED CODE
# Prepare dictionary ahead of time for quicker indexing.
# get_geojson function afterwards no longer needed!
YEAR_DICT = {}
for yr in range(1900, 2014):
    YEAR_DICT[yr] = gdf[gdf['year'] == yr].to_json()

# def get_geojson(yr):
#     """Input a year (int) and return corresponding slice of the GeoDataFrame, converted to GeoJSON"""
#     gdf_year = gdf[gdf['year'] == yr]
#     json_data = gdf_year.to_json()
#     return json_data

# geosource = GeoJSONDataSource(geojson = get_geojson(2000))
geosource = GeoJSONDataSource(geojson=YEAR_DICT[2000])
slider = Slider(title='Year', start=1900, end=2013, step=1, value=1900)
hover = HoverTool(tooltips=[('Country', '@country'),
                            ('Temp. Anomaly', '@monthly_anomaly')])

p = figure(title='Avg. Monthly Temperature Anomaly for Year 2000',
           plot_height=600,
           plot_width=1000,
           #            tools=[hover]
           )
p.tools.append(hover)

palette = brewer['RdBu'][9]

color_mapper = LinearColorMapper(
    palette=palette, low=-3, high=3, nan_color='#d9d9d9')

color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=20, border_line_color=None,
                     location=(0, 0), orientation='horizontal')

p.patches('xs', 'ys', source=geosource, fill_color={'field': 'monthly_anomaly', 'transform': color_mapper},
          line_color='black', line_width=0.25)

p.add_layout(color_bar, 'below')


def update_plot(attr, old, new):
    """Change properties / attributes of the datasource and title depending on slider value / position."""
    yr = slider.value
    # new_data = get_geojson(yr) ### <--- OLD, SLOW CODE
    # <----OPTIMIZED CODE. Faster indexing with dictionary.
    new_data = YEAR_DICT[yr]
    geosource.geojson = new_data
    p.title.text = f'Avg. Monthly Temperature Anomaly for Year {yr}'


slider.on_change('value', update_plot)

# Make a column layout of widgetbox(slider) and plot, and add it to the current document
curdoc().add_root(column(p, widgetbox(slider)))

# from bokeh.io import output_notebook, show

# output_notebook()
# show(column(p,widgetbox(slider)))
