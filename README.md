# nps-vis
An app for visualizing New Psychoactive Substances (NPS) developed by Ting-Jung Ku.  
The live version is freely available at [https://nps-vis.cmdm.tw](https://nps-vis.cmdm.tw).

This repository contains the code for an advanced interactive visualization tool that leverages Geographic Information System (GIS) technologies to enhance the UNODC's Early Warning Advisory for NPS. The tool provides dynamic observation and analysis of the geographical and temporal distribution of NPS, facilitating a comprehensive understanding of their public health impacts.

## Description
### Motivation

The rapid proliferation and evolving nature of New Psychoactive Substances (NPS) present significant challenges for global monitoring and public health policy development. Traditional monitoring systems often lack comprehensive mapping capabilities, limiting the ability to visually assess geographic and temporal trends in NPS usage. This project aims to bridge this gap by developing an interactive web application that utilizes GIS technologies to provide detailed visualizations of NPS trends. By enabling dynamic analysis of NPS data, this tool supports policymakers, researchers, and public health officials in making informed decisions to mitigate the global rise in NPS usage.

### Features

- **Interactive Analysis:** Select specific NPS categories and regions to customize visualizations and analyze trends.
- **Temporal Analysis:** Track changes in NPS reporting over time with a timeline slider.
- **Choropleth Maps:** Visualize the geographic distribution of NPS reports, with options to view data aggregated across all years or broken down annually.
- **Bar Charts:** Display annual and cumulative counts of NPS reports, categorized by substance group.

## Prerequisite

1. Install Docker
2. Install git

## How to start

1. Run `git clone git@github.com:CMDM-Lab/nps-vis.git` to get all source code.
2. Run `docker build -t nps-vis .`
3. Run `docker run -p 8050:8050 nps-vis`
4. Access [http://localhost:8050](http://localhost:8050) through the browser.
