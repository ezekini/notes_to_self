# to try
# columns='col' # will make multiple plots on that categorical
# a | b # will make two plots side by side

# https://altair-viz.github.io/user_guide/data.html
# DataFrames go into alt.Chart(df) but if we want .index we have to reset_index()
# and refer to it by the index's name (or `index`)
# https://github.com/altair-viz/altair/issues/271
# x='counts:Q' will plot counts on x axis as a Quantitative
# https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types
# Temporal, Ordinal, Nominal (discrete unordered category), Geojson
# Chart(df).mark_point for points, .mark_bar for bars
# https://altair-viz.github.io/user_guide/encoding.html#encoding-channels
# attributes include x, y, x2, y2, xError, latitude

# Note Pandas plotting not very useful
# import altair as alt
# pd.set_option('plotting.backend', 'altair')

# marks - https://altair-viz.github.io/user_guide/marks.html
# mark_line/mark_bar/mark_point

# Example:
# alt.Chart(cars).mark_point().encode(
#    x='Horsepower', # assumes :Q
#    y='Miles_per_Gallon', # assumed :Q
#    color='Origin',
#    shape='Origin',
#     tooltip=['Horsepower'])

# reset index, turn int counts into comma-separated values
# df_to_plot = df_seconds.reset_index().assign(nrows=[f'{v:,}' for v in df_seconds.index])
# alt.Chart(df_to_plot).mark_bar().encode(
# nrows has a new sort so specify the order seen in df_to_plot
#    x=alt.X('nrows', sort=df_to_plot.nrows.values),

# with mark_bar we can enable Bins, either `bin=True` for defaults or an alt.Bin object
# which includes nice binning, steps, base and other useful options
# x=alt.X('target:Q', bin=alt.Bin(maxbins=100)),

# set limits
#    y = alt.Y(col, scale=alt.Scale(domain=(min, max))
# https://altair-viz.github.io/user_guide/customization.html

# apply log scaling to y axis
#    y= alt.Y('seconds', scale= alt.Scale(type= 'log')),

# change scale to not start at 0
#    x=alt.X('Year_Built', scale=alt.Scale(zero=False)),

# set color for a binary column
#    color=alt.Color('is_duplicate:O', scale=alt.Scale(domain=[0, 1], range=['red', 'green']))


# add title and size for graph
# ).properties(
#    title='Parquet read times by row-count',
#    width=200,
#    height=200
# )

# https://altair-viz.github.io/user_guide/customization.html#adjusting-axis-labels
#     x=alt.X('x', axis=alt.Axis(format='%', title='percentage')),
# note format can be removed

# sorting of index gives correct order
# x=alt.X('index', sort=df2.index.values

# categoricals (e.g. from cut) raise a JSON encoding error, convert to string first

# Encodings are :O :Q :N :T :G https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types
