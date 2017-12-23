# Visualization of PISA Dataset in 2012

### Summary
This visualization used PISA dataset, which assessed the extent to which 15-year-old students have acquired key knowledge and skills that are essential for full participation in modern societies. And I mainly explored the strength of relationship between math score and social-economic status. The countries are divided into 9 groups due to their math score and strength of relationship.

### Design

- story I want to tell: 
	- Different countries varied in math performance. And the influence of social-economic status to math performance was different in each country. Like, Peru and some Latin American countries had bad math performance and less equity compared with other countries. 
	- I tried to express the same idea as Figure II.1.2 on [PISA 2012 Results: Excellence Through Equity: Giving Every Student the Chance to Succeed (Volume II)](http://www.oecd.org/pisa/keyfindings/pisa-2012-results-volume-ii.htm), which was in the form of a scatterplot.
- chart type: I choose to use a choropleth map for the main part and I was inspired by the graphs in [this article](http://uk.businessinsider.com/income-and-racial-inequality-maps-2015-5?r=US&IR=T). Also, I added two barcharts to show exactly how students behaved and how strong the relationship was in each country. Further, a scatterplot to explain how the "equity" was calculated.
- visual encodings: 
	- choropleth map:
		- map: showing geological information
		- color: showing both math performance and variance explained by social-economic status
	- barchart:
		- bar width(x axis): showing the mean math score or the strength of the relationship in each country
		- y axis: different countries
	- scatterplot:
		- x axis: the index of social-economic status
		- y axis: the mean math score
		- line: the regresssion line
- interaction: When hovering on one country, then relative information would pop up, including mean math score, strength of relationship between math score and social-economic status. People can also switch between the two barcharts.
- changes after collecting feedback：
	- Add another barchart showing strength of the relationship. I also added buttons to allow users switch between these two barcharts easily.
	- Add average line to barcharts.

### Feedback
1. Add the barchart of strength of the relationship, since there were two dimensions on the map. 
2. Add average line to the barchart.

### Resources
- [inspiration](http://uk.businessinsider.com/income-and-racial-inequality-maps-2015-5?r=US&IR=T), already linked
- [some visualizations others made using this dataset](http://mi2.mini.pw.edu.pl:8080/SmarterPoland/PISAcontest/#Dataset)
- [pisa 2012 report about equity](http://www.oecd.org/pisa/keyfindings/pisa-2012-results-volume-ii.htm), I tried to express the same idea as Figure II.1.2 which was in the form of a scatterplot.
- [how to calculate weighted average](http://pbpython.com/weighted-average.html)
- [how to reshape data in python](https://deparkes.co.uk/2016/10/28/reshape-pandas-data-with-melt/)
- [a simple way to zoom the map](https://coderwall.com/p/psogia/simplest-way-to-add-zoom-pan-on-d3-js)
- [how to draw a grid in d3](https://bl.ocks.org/cagrimmett/07f8c8daea00946b9e704e3efcbd5739)
- [arrow head in d3](http://vanseodesign.com/web-design/svg-markers/)
- for adding tooltips in d3, [reference 1](http://zeroviscosity.com/d3-js-step-by-step/step-5-adding-tooltips) and [reference 2](http://www.d3noob.org/2013/01/adding-tooltips-to-d3js-graph.html)
- for drawing a scatterplot with a regression line, [reference 1](https://bl.ocks.org/ctufts/298bfe4b11989960eeeecc9394e9f118) and [reference 2](https://bl.ocks.org/HarryStevens/be559bed98d662f69e68fc8a7e0ad097)