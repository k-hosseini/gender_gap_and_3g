# 3G Internet and Gender Gap in Iran
(This repository made as a part of term project for ECON622)

This package aims to prepare maps and dataframes which can be used to estimate the effects of rol-put of 3G Internet on gender gap in Iran.



Installing the package:

```python
pip install --index-url https://test.pypi.org/simple/ --no-deps gender-gap-in-iran
```

Iran political division maps

```python
Iran_map = load_Iran_shape_files()
```

plot Iran maps

```python
import geopandas as gpd

country = Iran_map["Country"].plot()
provinces = Iran_map["Provinces"].plot()
counties = Iran_map["Counties"].plot()
cities = Iran_map["Cities"].plot()
```

total area of each city
```python
city_area(cities)
```

load .1 percent sample of Mylinkov Geo project

```python
mylinkov_df = read_mylinkov()
```
or to use the original dataset, download  [Mylikov Geo project dataset](https://www.mylnikov.org/download) and set the path of the file as input of this function:

```python
mylinkov_df = read_mylinkov(cells_path =[path])
```



3G coverage map with different radius around each 3G cell. (the default value is 500)

```python
import gender_gaps 
gender_gaps.maps.coverage_map(UMTS_df = mylinkov , Cities = cities , radius=500)
```

covered area in each city 

```python
gender_gaps.maps.covered_area(UMTS_df = mylinkov , Cities = cities , radius=500)
```
3G coverage rate in each city:
```python
gender_gaps.maps.cov_map_rate_period(UMTS_df= mylinkov , Cities = cities , radius=500 , frequency = 'Q)
```

coverage rate and coverage map for each period in the dataset. (the default period is quarter)
```python
coverage_maps_period_dic , coverage_rate_df = gender_gaps.maps.cov_map_rate_period(UMTS_df= mylinkov , Cities = cities ,radius=500,frequency = 'Q')
```

export coverage map shapefiles, png and gif files and dataframe for coverage rate in each period and coverage.
```python
gender_gaps.maps.export_maps(coverage_maps_period_dict= coverage_maps_period_dic , Country = country)
```
the coverage map gif file from 2012 to 2018:
![](https://github.com/k-hosseini/gender_gap_and_3g/blob/master/src/gender_gaps/data/UMTS_animation_500.gif)


## Background and Research Question
Increasing global access to the Internet could affect the labor market outcomes from different channels. These affects could be more influential in developing countries, where in general, there are more severe institutional inefficiencies in the labor market. Studying the effect of the Internet in the case of Iran can have other attractions as well since apart from the general inefficiencies in the labor market institutions of a developing country, Iran is historically suffering from one of the lowest levels of female labor force participation rates in the world. In regard, a typical hypothesis to explain this phenomenon is cultural gender discrimination. As a result, some observers believe that more exposure to the Internet could change this culture, providing more support for women to work.

In this line, this project seeks to answer the following question: what are the short-term impacts of expanding mobile broadband coverage on females’ labor market outcomes in urban regions of Iran? To answer this question, I matched Semi-Panel of Iranian Household Income and Expenditure Survey (HEIS) from 2012 to 2018 with Mylinkov Geo project that can be used to determine geographical roll-out of 3G Internet from 2014 to 2018, and taking advantage of a difference-in-difference analysis, I estimate the effects of 3G Internet on the individual level labor outcomes.

