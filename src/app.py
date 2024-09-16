import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
from plotly.graph_objs import Figure
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output, State
from typing import Any,List, Dict, Optional


# Assuming you have some data to be used for dropdown options and table columns
nps_types = ["Type1", "Type2", "Type3"]
table_columns = ["Column1", "Column2", "Column3"]
data = pd.DataFrame({
    'state': ['CA', 'TX', 'NY', 'FL'],
    'value': [10, 15, 8, 12]
})
nps_options = [
  {'label': 'Aminoindanes', 'value': 'Aminoindanes'},
  {'label': 'Benzodiazepines', 'value': 'Benzodiazepines'},
  {'label': 'Fentanyl analogues', 'value': 'Fentanyl analogues'},
  {'label': 'Lysergamides', 'value': 'Lysergamides'},
  {'label': 'Nitazenes', 'value': 'Nitazenes'},
  {'label': 'Phencyclidine-type substances', 'value': 'Phencyclidine-type substances'},
  {'label': 'Phenethylamines', 'value': 'Phenethylamines'},
  {'label': 'Phenidates', 'value': 'Phenidates'},
  {'label': 'Phenmetrazines', 'value': 'Phenmetrazines'},
  {'label': 'Piperazines', 'value': 'Piperazines'},
  {'label': 'Plant-based substances', 'value': 'Plant-based substances'},
  {'label': 'Synthetic cannabinoids', 'value': 'Synthetic cannabinoids'},
  {'label': 'Synthetic cathinones', 'value': 'Synthetic cathinones'},
  {'label': 'Tryptamines', 'value': 'Tryptamines'},
  {'label': 'Other substances', 'value': 'Other substances'}
]
nps_dropdown_options = [
  {'label': 'All', 'value': 'All'},
  {'label': 'Aminoindanes', 'value': 'Aminoindanes'},
  {'label': 'Benzodiazepines', 'value': 'Benzodiazepines'},
  {'label': 'Fentanyl analogues', 'value': 'Fentanyl analogues'},
  {'label': 'Lysergamides', 'value': 'Lysergamides'},
  {'label': 'Nitazenes', 'value': 'Nitazenes'},
  {'label': 'Phencyclidine-type substances', 'value': 'Phencyclidine-type substances'},
  {'label': 'Phenethylamines', 'value': 'Phenethylamines'},
  {'label': 'Phenidates', 'value': 'Phenidates'},
  {'label': 'Phenmetrazines', 'value': 'Phenmetrazines'},
  {'label': 'Piperazines', 'value': 'Piperazines'},
  {'label': 'Plant-based substances', 'value': 'Plant-based substances'},
  {'label': 'Synthetic cannabinoids', 'value': 'Synthetic cannabinoids'},
  {'label': 'Synthetic cathinones', 'value': 'Synthetic cathinones'},
  {'label': 'Tryptamines', 'value': 'Tryptamines'},
  {'label': 'Other substances', 'value': 'Other substances'}
]
checklist_options = [
    {'label': 'Asia', 'value': 'Asia'},
    {'label': 'Africa', 'value': 'Africa'},
    {'label': 'North America', 'value': 'North America'},
    {'label': 'South America', 'value': 'South America'},
    {'label': 'Europe', 'value': 'Europe'},
    {'label': 'Oceania', 'value': 'Oceania'}
]
bt_options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Asia', 'value': 'Asia'},
    {'label': 'Africa', 'value': 'Africa'},
    {'label': 'North America', 'value': 'North America'},
    {'label': 'South America', 'value': 'South America'},
    {'label': 'Europe', 'value': 'Europe'},
    {'label': 'Oceania', 'value': 'Oceania'}
]
df = pd.read_csv('./data/processed_nps_complete_list.csv')
population_df = pd.read_csv('./data/population.csv')

# Create a new DataFrame with rows where 'Year' is 'Total'
df_total = df[df['Year'] == 'Total']
# Exclude rows where 'Year' is 'Total'
df = df[df['Year'] != 'Total']





# Convert 'Year' to float first and then to int to avoid ValueError
df['Year'] = df['Year'].astype(float).astype(int)

#reusable component
def graph_title(title : str, title_id : str) -> dbc.Row:
    return dbc.Row([
        dbc.Col(html.H2(title, id = title_id), width=12)
    ], className="mb-4")

def dropdown(label : str, options : List[Dict[str, str]], id: Optional[str] = None) -> dbc.Container:
    return dbc.Container([
        dbc.Row([
            dbc.Label(label),
            dbc.Col(dbc.Select(
                id=id, 
                options=[{"label": option['label'], "value": option['value']} for option in options],
                value='All'
            ), width=12)
        ], className="mt-4")
    ], fluid=True)

# def navbar(title_id1: str, title_id2: str) -> dbc.Nav:
#     return dbc.Nav(
#         [
#             dbc.NavItem(dbc.NavLink("Choropleth Maps", href="#" + title_id1)),
#             dbc.NavItem(dbc.NavLink("Line chart", href="#" + title_id2))
#         ],
#         pills=False,  
#     )
def nps_checklist_with_select_all(checklist_options, id, title):
    return html.Div([
        dbc.Label(title),
        dbc.Form([
            dbc.Switch(
                id='select-all-switch',
                label="Select All",
                value=True
            ),
            dbc.Checklist(
                options=checklist_options,
                value=[],
                id=id,
                inline=True,
            ),
        ]),
    ], className="mt-4")
def checklist(checklist_options : List[Dict[str, str]], id: Optional[str], title : str) -> dbc.Row:
    return dbc.Row([
            html.Div(
        [
            dbc.Label(title),
            dbc.Checklist(
                options = checklist_options,
                value = [item['value'] for item in checklist_options],
                id = id,
                inline = True,
            ),
        ])
        ], className="mt-4")
def inline_radioitems(bt_options : List[Dict[str, str]], id: Optional[str], title : str) -> dbc.Row :
    return dbc.Row([html.Div(
    [
        dbc.Label(title),
        dbc.RadioItems(
            options=bt_options,
            value= bt_options[0]['value'],
            id=id,
            inline=True,
        ),
    ])
    ],className="mt-4")

def select_all_year_bt(id : str, title: str) -> dbc.Row:
    return dbc.Row([
            html.Div(
        [
            dbc.Label(title),
            dbc.RadioItems(
                id=id,
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "Aggregate Data (Sum of All Years)", "value": "aggregate"},
                    {"label": "Yearly Data (2008-2024)", "value": "yearly"},
                    {"label": "Aggregate Data Normalized by Population", "value": "normalized_aggregate"},
                    {"label": "Yearly Data Normalized by Population", "value": "normalized_yearly"},
                    
                ],
                value="aggregate",
            ),
        ])
    ], className="mt-4")
    # return html.Div([
    #     dbc.Form([
    #         dbc.Switch(
    #             id=id,
    #             label="All Years",
    #             value=False
    #         )
    #     ])
    # ], className="mt-4")


def create_introduction_section(title, descriptipon):
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H2(title), width=12)
        ], className="mt-4"),
         dbc.Row([
            dbc.Col(html.Div([
                dcc.Markdown(
                    descriptipon,
                    dangerously_allow_html=True
                )
            ], style={'fontSize': '16px'}), width=12)
        ], className="mb-4")
    ], fluid=True)

def title_with_description(title: str, description: str) -> dbc.Container:
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(title), width={"size": 6, "offset": 3}),
            dbc.Col(html.P(description), width={"size": 6, "offset": 3})
        ])
    ], fluid=True)



# Initialize the Dash app with Bootstrap
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH, dbc_css], suppress_callback_exceptions=True
)
#lauyout
app.layout = dbc.Container([
    html.Div(children=[
        # Header
        title_with_description("NPS Data Visualization", "Explore data on New Psychoactive Substances across the world."),

        html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Introduction', value='tab-1'),
                dcc.Tab(label='Global Distribution Analysis', value='tab-2'),
                dcc.Tab(label='Country-Level Analysis', value='tab-3'),
            ]),
            html.Div(id='tabs-content')
        ]),
        

        # Footer
        dbc.Container([
            dbc.Row([
                dbc.Col(
                html.P([
                    "Data sourced from UNODC Early Warning Advisory (EWA) on New Psychoactive Substances (NPS) URL:",
                    html.A("https://www.unodc.org/LSS/Home/NPS", href="https://www.unodc.org/LSS/Home/NPS"),
                    html.Br(),  # New line
                    "Developed by National Taiwan University Computational Molecular Design and Metabolomics Lab."
                ]),
                width={"size": 9, "offset": 3},
                style={'fontSize': '12px', "marginBottom": "20px"}  # Adding space below the paragraph
            )
            ])
        ], className="mt-4")
        ])
    ],
    fluid=True,
    className="dbc"
)

#callback to handle the tabs
@app.callback(dash.dependencies.Output('tabs-content', 'children'),
              [dash.dependencies.Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
        #introduction
        create_introduction_section("Welcome to the NPS Data Visualization Tool", """
                        &nbsp;&nbsp;This interactive tool is designed to provide insights into the world of New Psychoactive Substances (NPS). NPS are substances created to mimic the effects of controlled drugs and to evade drug laws. They pose significant challenges to drug policy and public health due to their constantly changing nature and unknown health risks.

                        &nbsp;&nbsp;Here, you can explore various data visualizations that shed light on the prevalence, distribution, and trends of NPS usage across different regions and times. This tool aims to aid researchers, policymakers, and the general public in understanding the complex landscape of NPS and in making informed decisions.
                                    
                        &nbsp;&nbsp;For the best experience, we recommend using this tool on a desktop or PC. 
                                    
                        Data source: UNODC Early Warning Advisory (EWA). Data updated until: January 2024.
                        """),
        ])
    elif tab == 'tab-2':
        return html.Div([
            create_introduction_section("Global Distribution of New Psychoactive Substance Reports", """
                &nbsp;&nbsp;This interactive dashboard features a responsive Choropleth Map and two Bar Charts, both synchronized to user selections of NPS types and continents. 
                The map allows interactive exploration of global NPS trends, while selections instantly reflect on both the map and the charts, offering a comprehensive view of NPS data through annual and cumulative analyses.
                """),
            # Map 
            dbc.Container([
                nps_checklist_with_select_all(nps_options, 'map-nps-checklist', "Select NPS"),
                inline_radioitems(bt_options, 'map-continent-bt', 'Select Continent'),
                select_all_year_bt('select-all-years', 'Select Map View:  '),
                dbc.Row([
                    dbc.Col(dcc.Graph(id='choropleth-map', config={'scrollZoom': False}, responsive='auto', style={'width': "100%"}), width=12)
                ], className="mt-4")
            ], fluid=True),

            #bar chart
            dbc.Container([
                dbc.Row([
                    dbc.Col(dcc.Graph(id='year-barchart', config={'scrollZoom': False}, responsive='auto', style={'width': "100%"}), xs=12, sm=12, md=12, lg=6, xl=6,),
                    dbc.Col(dcc.Graph(id='total-barchart', config={'scrollZoom': False}, responsive='auto', style={'width': "100%"}), xs=12, sm=12, md=12, lg=6, xl=6,)
                ], className="mt-4")
            ], fluid=True),
        ])
    elif tab == 'tab-3':
        return html.Div([
            # Title Row
        create_introduction_section("Country-Level NPS Trend Analysis", """
                        &nbsp;&nbsp;This tool provides an in-depth view of New Psychoactive Substances (NPS) trends on a country-by-country basis. Users select an NPS and a continent, and the tool generates a line chart displaying the reported NPS counts for each country in that continent. It's essential for understanding the regional spread and impact of NPS, offering critical data for informed policy-making and public health strategies.
                        """),


        #Dropdown to select data
        dropdown("Select NPS", nps_dropdown_options, 'line-chart-dropdown'),


        # Line chart 
        dbc.Container([
            checklist(checklist_options, 'line-chart-checklist', "Select Continents"),
            dbc.Row([
                dbc.Col(dcc.Graph(id='line-chart', config={'scrollZoom': False}, responsive='auto', style={'width': "100%"}), width=12)
            ], className="mt-4"),
        ], fluid=True),
        ])

#functuins that create the figure
def create_yearly_choropleth_map(df : pd.DataFrame, nps_list : list) -> Figure:
    # Group by 'Country' and 'Year', summing 'count'
    df = df.groupby(['Country', 'Year']).agg({
    'count': 'sum',
    'iso_alpha': 'first'  
    }).reset_index()

    # Sort the DataFrame by 'Year'
    df = df.sort_values(by='Year')


    min_value = df['count'].min()
    max_value = df['count'].max()
    # df['Year'] = df['Year'].astype(int)
    fig = px.choropleth(df, 
    locations="iso_alpha", 
    color="count",  
    hover_name="Country", 
    animation_frame="Year",  # Animate by year
    projection="robinson" ,
    range_color=[min_value, max_value],
    color_continuous_scale = 'ylorrd')

    fig.update_layout(coloraxis_colorbar=dict(
        title='NPS reports',
        ticks='outside',
        tickvals=[min_value, max_value],
        ticktext=[str(min_value), str(max_value)]
    ))

    fig.update_layout(
    title=f'Global Reports of New Psychoactive Substances (NPS)',
    annotations=[
        dict(
            text=', '.join(nps_list),  # Your dynamic list of NPS types
            showarrow=False,
            xref='paper',  # Relative to the edges of the paper
            yref='paper',
            x=0,  # Align to the left of the graph
            y=1,  # Position right below the main title
            xanchor='left',
            yanchor='bottom',
            font=dict(
                size=14,  # Smaller font size than the main title
                color='grey'  # A different color to distinguish from the main title
            )
        )
    ],
    margin=dict(l=0, r=0, t=50, b=0),
    height=600)

    # fig.update_geos(
    #     lataxis_range=[-67,90],
    #     # projection_rotation_lon=155
    # )
    return fig

def create_all_year_choropleth_map(df : pd.DataFrame, nps_list : list) -> Figure:
    df = df.groupby(['Country']).agg({
    'count': 'sum',
    'iso_alpha': 'first'  
    }).reset_index()

    min_value = df['count'].min()
    max_value = df['count'].max()
    # df['Year'] = df['Year'].astype(int)

    fig = px.choropleth(df, 
        locations="iso_alpha", 
        color="count",  
        hover_name="Country", 
        projection="robinson" ,
        range_color=[min_value, max_value],
        color_continuous_scale = 'darkmint')

    fig.update_layout(coloraxis_colorbar=dict(
        title='NPS reports',
        ticks='outside',
        tickvals=[min_value, max_value],
        ticktext=[str(min_value), str(max_value)]
    ))

    fig.update_layout(
    title=f'Global Reports of New Psychoactive Substances (NPS), all year accumulative',
    annotations=[
        dict(
            text=', '.join(nps_list),  # Your dynamic list of NPS types
            showarrow=False,
            xref='paper',  # Relative to the edges of the paper
            yref='paper',
            x=0,  # Align to the left of the graph
            y=1,  # Position right below the main title
            xanchor='left',
            yanchor='bottom',
            font=dict(
                size=14,  # Smaller font size than the main title
                color='grey'  # A different color to distinguish from the main title
            )
        )
    ],
    margin=dict(l=0, r=0, t=50, b=0),
    height=600)

    # fig.update_geos(
    #     lataxis_range=[-67,90],
    #     # projection_rotation_lon=155
    # )
    return fig

def create_normalized_all_year_choropleth_map(df : pd.DataFrame, pop_df: pd.DataFrame, nps_list : list) -> Figure:
    df_grouped = df.groupby(['Country']).agg({
    'count': 'sum',
    'iso_alpha': 'first'  
    }).reset_index()

    #Use the latest available population (2023)
    pop_latest = pop_df[['iso_alpha', '2023']]

    #Merge population data with NPS data
    merged_df = pd.merge(df_grouped, pop_latest, on='iso_alpha', how='inner')

    #Normalize NPS count by population(per million people)
    merged_df['nps_per_million'] = (merged_df['count'] / merged_df['2023']) * 1e6
    merged_df['nps_per_million_log'] = np.log10(merged_df['nps_per_million'].replace(0, np.nan))

    min_value = merged_df['nps_per_million_log'].min()
    max_value = merged_df['nps_per_million_log'].max()
    # df['Year'] = df['Year'].astype(int)

    fig = px.choropleth(merged_df, 
        locations="iso_alpha", 
        color="nps_per_million_log",  
        hover_name="Country", 
        hover_data={
        "nps_per_million_log": ":.2f",  # Show log value with 2 decimal places  
        "nps_per_million": ":.2f",  
        "iso_alpha": True,  # Hide iso_alpha from hover tooltip
        },
        labels={"nps_per_million_log": "NPS reports per Million (log)", "nps_per_million": "NPS reports per Million"},
        projection="robinson" ,
        range_color=[min_value, max_value],
        color_continuous_scale = 'brwnyl')

    fig.update_layout(coloraxis_colorbar=dict(
        title= 'NPS reports per Million People (log scale)',
        ticks='outside',
        tickvals=[min_value, max_value],
        ticktext=[f'{min_value:.2f}', f'{max_value:.2f}'],
        xanchor='left',
    ))

    fig.update_layout(
    title=f'Global Reports of New Psychoactive Substances (NPS), all year accumulative, normalized by population (log scale)',
    annotations=[
        dict(
            text=', '.join(nps_list),  # Your dynamic list of NPS types
            showarrow=False,
            xref='paper',  # Relative to the edges of the paper
            yref='paper',
            x=0,  # Align to the left of the graph
            y=1,  # Position right below the main title
            xanchor='left',
            yanchor='bottom',
            font=dict(
                size=14,  # Smaller font size than the main title
                color='grey'  # A different color to distinguish from the main title
            )
        )
    ],
    margin=dict(l=0, r=0, t=50, b=0),
    height=600)

    # fig.update_geos(
    #     lataxis_range=[-67,90],
    #     # projection_rotation_lon=155
    # )
    return fig

def create_normalized_yearly_choropleth_map(df : pd.DataFrame, pop_df: pd.DataFrame, nps_list : list) -> Figure:
    df_grouped = df.groupby(['Country', 'Year']).agg({
    'count': 'sum',
    'iso_alpha': 'first'  
    }).reset_index()

    # Sort the DataFrame by 'Year'
    df_sorted = df_grouped.sort_values(by='Year')

   # Population columns from 2008 to 2023
    year_columns = list(map(str, range(2008, 2024)))  # Population data for the years 2008 to 2023
    pop_df = pop_df[['iso_alpha'] + year_columns]  # Keep only the necessary columns

    # Merge population data with NPS data based on iso_alpha
    merged_df = pd.merge(df_sorted, pop_df, on='iso_alpha', how='inner')

    # Normalize NPS count by population, using 2023 population for years after 2023
    merged_df['nps_per_million'] = merged_df.apply(
        lambda row: (row['count'] / row[str(min(row['Year'], 2023))]) * 1e6, axis=1
    )
    merged_df['nps_per_million_log'] = np.log10(merged_df['nps_per_million'].replace(0, np.nan))

    min_value = merged_df['nps_per_million_log'].min()
    max_value = merged_df['nps_per_million_log'].max()
    # df['Year'] = df['Year'].astype(int)

    fig = px.choropleth(merged_df, 
    locations="iso_alpha", 
    color="nps_per_million_log",  
    hover_name="Country", 
    hover_data={
        "nps_per_million_log": ":.2f",  # Show log value with 2 decimal places  
        "nps_per_million": ":.2f",
        "iso_alpha": True,  # Hide iso_alpha from hover tooltip
        "Year": True},
    labels={"nps_per_million_log": "NPS reports per Million (log)", "nps_per_million": "NPS reports per Million"},
    animation_frame="Year",  # Animate by year
    projection="robinson" ,
    range_color=[min_value, max_value],
    color_continuous_scale = 'purpor')

    fig.update_layout(coloraxis_colorbar=dict(
        title='NPS reports per Million People (log scale)', 
        ticks='outside',
        tickvals=[min_value, max_value],
        ticktext=[f'{min_value:.2f}', f'{max_value:.2f}'],  # Format to 2 decimal places
    ))

    fig.update_layout(
    title=f'Global Reports of New Psychoactive Substances (NPS), normalized by population (log scale)',
    annotations=[
        dict(
            text=', '.join(nps_list),  # Your dynamic list of NPS types
            showarrow=False,
            xref='paper',  # Relative to the edges of the paper
            yref='paper',
            x=0,  # Align to the left of the graph
            y=1,  # Position right below the main title
            xanchor='left',
            yanchor='bottom',
            font=dict(
                size=14,  # Smaller font size than the main title
                color='grey'  # A different color to distinguish from the main title
            )
        )
    ],
    margin=dict(l=0, r=0, t=50, b=0),
    height=600)

    return fig

def zoom_in(fig : Figure, selected_continent : str) -> Figure:
    continent_focus = {
        'All': {"lataxis_range": [-67, 90], "lonaxis_range": [-180, 180]},
        'Asia': {"lataxis_range": [-10, 55], "lonaxis_range": [40, 150]},
        'Africa': {"lataxis_range": [-35, 35], "lonaxis_range": [-20, 50]},
        'North America': {"lataxis_range": [10, 70], "lonaxis_range": [-130, -60]},
        'South America': {"lataxis_range": [-55, 15], "lonaxis_range": [-85, -35]},
        'Europe': {"lataxis_range": [35, 70], "lonaxis_range": [-10, 40]},
        'Oceania': {"lataxis_range": [-50, 0], "lonaxis_range": [110, 180]}
    }

    focus = continent_focus.get(selected_continent, continent_focus['All'])
    fig.update_geos(lataxis_range=focus["lataxis_range"], lonaxis_range=focus["lonaxis_range"])
    return fig
    

def create_line_chart(df : pd.DataFrame, selected_continents : list) -> Figure:
    mask = df['Continent'].isin(selected_continents)
    continent_filtered_df = df[mask]
    
    # Exclude rows where 'Year' is 'Total'
    year_filtered_df = continent_filtered_df[continent_filtered_df['Year'] != 'Total']

    # Ensure 'Year' is an integer for proper sorting and line plotting
    year_filtered_df['Year'] = year_filtered_df['Year'].astype(int)

    # First sort by 'Country' then 'Year'
    sorted_df = year_filtered_df.sort_values(by=['Country', 'Year'])

    # Create the line chart
    fig = px.line(sorted_df, x='Year', y='count', color='Country')

    # Force alphabetical ordering of the legend
    fig.update_layout(legend=dict(traceorder='normal'))

    return fig

def create_all_nps_line_chart(df : pd.DataFrame, selected_continents : list) -> Figure:
    mask = df['Continent'].isin(selected_continents)
    continent_filtered_df = df[mask]

    continent_filtered_df = continent_filtered_df.groupby(['Year', 'Country']).agg({
        'count': 'sum'
    }).reset_index()
    
    # Exclude rows where 'Year' is 'Total'
    year_filtered_df = continent_filtered_df[continent_filtered_df['Year'] != 'Total']

    # Ensure 'Year' is an integer for proper sorting and line plotting
    year_filtered_df['Year'] = year_filtered_df['Year'].astype(int)

    # First sort by 'Country' then 'Year'
    sorted_df = year_filtered_df.sort_values(by=['Country', 'Year'])

    # Create the line chart
    fig = px.line(sorted_df, x='Year', y='count', color='Country')

    # # Force alphabetical ordering of the legend
    fig.update_layout(legend=dict(traceorder='normal'))

    return fig

def create_year_barchart(df : pd.DataFrame, nps_list : list) -> Figure:
    # Group by 'Year' and 'Group Name' and sum the 'count'
    grouped_df = df.groupby(['Year', 'Group Name'])['count'].sum().reset_index()

    # Create a bar chart
    fig = px.bar(grouped_df, x='Year', y='count', color='Group Name',
                 labels={'count': 'Total Count'}, 
                 title='Annual Report Count by Group Name')
    fig.update_layout(
        autosize=True,  
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            orientation="h",
        ),
    )
    fig.update_xaxes(title_text='')  # Remove the "Year" label
    return fig

#callback to handle the select all logic
@app.callback(
    Output('map-nps-checklist', 'value'),
    [Input('select-all-switch', 'value')],
    [State('map-nps-checklist', 'options')]
)
def select_all_nps(switch_value, nps_options):
    if switch_value:
        return [option['value'] for option in nps_options]
    return []

# Callback to update the Choropleth map
@app.callback(
    Output('choropleth-map', 'figure'),
    [
    Input('map-nps-checklist', 'value'),
    Input('map-continent-bt', 'value'),
    Input('select-all-years', 'value')
    ]
)
def update_choropleth_map(selected_nps : list[str], selected_continent : str, select_all_years: str) -> Figure:
    if select_all_years == 'aggregate' or select_all_years == 'normalized_aggregate':
        filtered_df = df_total[df_total['Group Name'].isin(selected_nps)]
    elif select_all_years == 'yearly' or select_all_years == 'normalized_yearly':
        filtered_df = df[df['Group Name'].isin(selected_nps)]

    if selected_continent != 'All':
        filtered_df = filtered_df[filtered_df['Continent'] == selected_continent]

    if select_all_years == 'aggregate':
        fig = create_all_year_choropleth_map(filtered_df , selected_nps)
    elif select_all_years == 'normalized_aggregate':
        fig = create_normalized_all_year_choropleth_map(filtered_df, population_df, selected_nps)
    elif select_all_years == 'normalized_yearly':
        fig = create_normalized_yearly_choropleth_map(filtered_df, population_df, selected_nps)
    else:
        fig = create_yearly_choropleth_map(filtered_df , selected_nps)
    fig = zoom_in(fig, selected_continent)
    return fig

# Callback to update the year-barchart
@app.callback(
    Output('year-barchart', 'figure'),
    [
    Input('map-nps-checklist', 'value'),
    Input('map-continent-bt', 'value')
    ]
)
def update_year_barchart(selected_nps : list[str], selected_continent : str) -> Figure:
    # Filter the DataFrame based on the selected NPS and Continent
    filtered_df = df[df['Group Name'].isin(selected_nps)]
    if selected_continent != 'All':
        filtered_df = filtered_df[filtered_df['Continent'] == selected_continent]
    
    fig = create_year_barchart(filtered_df, selected_nps)
    
    return fig

@app.callback(
    Output('total-barchart', 'figure'),
    [
    Input('map-continent-bt', 'value')
    ]
)
def update_total_barchart(selected_continent : str) -> Figure:
    # Filter the DataFrame based on the selected Continent
    if selected_continent != 'All':
        filtered_df = df[df['Continent'] == selected_continent]
    else:
        filtered_df = df.copy()

    # Group by 'Group Name' and sum the 'count'
    grouped_df = filtered_df.groupby('Group Name')['count'].sum().reset_index()

    # Create a bar chart
    fig = px.bar(grouped_df, x='Group Name', y='count',
                 labels={'count': 'Total Count'}, 
                 title='Cumulative Count of New Psychoactive Substance Reports by Group')

    return fig

# Callback to update the Line chart
@app.callback(
    Output('line-chart', 'figure'),
    [
        Input('line-chart-dropdown', 'value'),
        Input('line-chart-checklist', 'value')
    ]
)
def update_linechart(selected_nps : str, selected_continents : list) -> Figure:
    if selected_nps != 'All':
        fig = create_line_chart(df[df['Group Name'] == selected_nps], selected_continents)
    else:
        fig = create_all_nps_line_chart(df, selected_continents)
    return fig

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
