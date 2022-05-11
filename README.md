# Post-COVID Pre-owned Vehicle Price Analysis

## Team Members
* Muqing Li (A92108137) Presenter
* Xin Xie(A59010731)
* Ajit Deshpande (A59003350)
* Junzhe Luo(A16564475)
* John Malgeri (A15656397) 
* LinXiao Zhang(A59013665)

## Objective
The objective of the project is to figure out the impact of different factors on the fluctuation of the car prices. It is aimed at building a car price 
monitoring system for car prices, especially during the COVID-19 pandemic since the price of cars has fluctuated greatly during this time period. 

## File Structure

```
|-- ROOT
  |-- README.md
  |-- data_analysis.py
  |-- data_cleaning.py
  |-- notebook_for_visualization.ipynb
  |-- ECE143presentation-Group11.pdf
  |-- Modules
  |   |-- averageprice_bodytype_2.py
  |   |-- Car_brands_and_COVID_cities_analysis.py
  |   |-- pie_bodytype.py
  |   |-- price_plot.py
  |   |-- pricevsdays_bodytype.py
  |   |-- season_plot.py
  |   |-- sns_plots.py
  |   |-- utils.py
  |-- cleaned_data
  |   |-- Cleaned10GB.csv
  |-- plots
  |   |-- Car_price_range_vs_price.png
  |   |-- Cities_affected_bycovid_vs_price.png
  |   |-- all level_vs_price_line_sns.png
  |   |-- average-price vs region.png
  |   |-- averages.png
  |   |-- avg_firstwave.png
  |   |-- avg_secondwave.png
  |   |-- bodytypes.png
  |   |-- car_season_plot.png
  |   |-- daysonmarket_vs_price.png
  |   |-- first wave_vs_price_line_sns.png
  |   |-- high level_vs_price_line_sns.png
  |   |-- low level_vs_price_line_sns.png
  |   |-- mid level_vs_price_line_sns.png
  |   |-- second wave_vs_price_line_sns.png
  |   |-- sum-price vs region.png
  |   |-- price vs days, grouped by body type
  |       |-- Figure_1.png
  |       |-- Figure_2.png
  |       |-- Figure_3.png
  |       |-- Figure_4.png
  |-- raw_data
      |-- vehicles.csv
```


## Run the code
1. Run the ```data_cleaning.py``` to clean the data in ```raw_data```  
2. Run the ```data_analysis.py``` to get all graphs.
3. Run the ```Car_brands_and_COVID_cities_analysis.py``` to get analysis on Car Brands of different price ranges and prices in cities affected by COVID-19

## third-party modules
* pandas_profiling
* numpy
* pandas
* matplotlib
* seaborn
* sklearn
* plotly
* csv

