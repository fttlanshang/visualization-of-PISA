# coding: utf-8
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import linear_model

pisa2012 = pd.read_csv('pisa2012.csv')
pisa2012 = pisa2012[["CNT","SUBNATIO","STRATUM","OECD","NC","SCHOOLID","STIDSTD",
	"ST04Q01", "ESCS", "PV1MATH","PV2MATH", "PV3MATH", "PV4MATH","PV5MATH",
	"W_FSTUWT"]]
# pisa2012_korea = pisa2012[pisa2012.CNT == "Korea"]
# pisa2012_japan = pisa2012[pisa2012.CNT == 'Japan']
# len(pisa2012_japan)
# pisa2012_macao = pisa2012[pisa2012.CNT == "Macao-China"]
# len(pisa2012_macao)
# pisa2012_hongkong = pisa2012[pisa2012.CNT == "Hong Kong-China"]
# len(pisa2012_hongkong)
# for cnt in pisa2012.CNT: # this is not consistent with the code book
#     if "Shang" in cnt:
#         print cnt
#         break  
# pisa2012_shanghai = pisa2012[pisa2012.CNT == "China-Shanghai"]
# len(pisa2012_shanghai)

# pisa2012_concerned_asian_countries = pd.concat([pisa2012_japan, pisa2012_korea, pisa2012_macao, pisa2012_hongkong, pisa2012_shanghai])
# len(pisa2012_concerned_asian_countries)

#thought boxplot is much more clear
# math_distribution = sns.violinplot(x="CNT", y = "PV1MATH", data = pisa2012_concerned_asian_countries)
# plt.show()
# math_distribution_whole = sns.violinplot(x="CNT", y = "PV1MATH", data = pisa2012)
# plt.show()
# pisa2012["CNT"].nunique() #68 countries

# draw math/read/science score relatively for three asian countries
# sns.boxplot(x="CNT", y = "PV1MATH", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
# plt.show()
# sns.boxplot(x="CNT", y = "PV1READ", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
# plt.show()
# sns.boxplot(x="CNT", y = "PV1SCIE", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
# plt.show()

#########Thinks comparing only 3 contries is not enough###################################################

## delete city information, because they are so hard to show on the map!
pisa2012 = pisa2012[pisa2012["CNT"] != "Perm(Russian Federation)"]
# pisa2012 = pisa2012[pisa2012["CNT"] != "Florida (USA)"]

##before melt, change Shanghai/Hong Kong etc to China, 
## so all the records will aggregate together
# it is suggested not to assign variables with chaining
# http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
pisa2012.loc[pisa2012["CNT"] == "China-Shanghai","CNT"] = "China"
pisa2012.loc[pisa2012["CNT"] == "Hong Kong-China","CNT"] = "China"
pisa2012.loc[pisa2012["CNT"] == "Macao-China","CNT"] = "China"
pisa2012.loc[pisa2012["CNT"] == "Chinese Taipei","CNT"] = "China"


###############Below is for calculating mean for each country################
melted = pd.melt(pisa2012, 
	id_vars = ["CNT", "SUBNATIO","STRATUM","OECD","NC","SCHOOLID",
				"STIDSTD","ST04Q01", "ESCS", "W_FSTUWT"],
	var_name="PHASE", 
	value_name="SCORE")

def weighted_avg(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()
    
country_phase_math_means = melted.groupby(["CNT","PHASE"]).apply(weighted_avg, "SCORE","W_FSTUWT")
CNT_MATH_MEAN = country_phase_math_means.groupby("CNT").mean() # this is series data, not dataframe

##############THIS WILL BE USED LATER################
CNT_MATH_MEAN = pd.DataFrame({
	"CNT": CNT_MATH_MEAN.index, 
	"MATH_MEAN": CNT_MATH_MEAN.values
})

CNT_MATH_MEAN.sort_values("MATH_MEAN", ascending=False)

pisa2012["MATH"] = (pisa2012["PV1MATH"] + pisa2012["PV2MATH"] + pisa2012["PV3MATH"] + pisa2012["PV4MATH"] + pisa2012["PV5MATH"]) / 5
countries = CNT_MATH_MEAN["CNT"]
slopes = []
strengths  = []
valid_countries = []

def cal_linear_regression():
	for country in countries:
		try:
			country_escs_math_data = pisa2012[pisa2012["CNT"] == country][["MATH", "ESCS"]] 
			modified_country_escs_math_data = country_escs_math_data.dropna() # need to draw nan values!!
			x = np.array(modified_country_escs_math_data["ESCS"])
			y = np.array(modified_country_escs_math_data["MATH"])
			slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
			slopes.append(slope)
			strengths.append((r_value**2) * 100)
			valid_countries.append(country)
		except ValueError:
			print country

cal_linear_regression()

##############THIS WILL BE USED LATER################
CNT_RELATIONSHIP = pd.DataFrame({
	"CNT": valid_countries,
	"slope": slopes,
	"strength": strengths
})

def cal_math_avg(agg_var):
	initial_agg_var = []
	for var in agg_var:
		initial_agg_var.append(var)
	initial_agg_var.append("PHASE")
	country_phase_math_means = melted.groupby(by=initial_agg_var).apply(weighted_avg, "SCORE","W_FSTUWT")
	return country_phase_math_means.groupby(by=agg_var).mean() 
	
CNT_GENDER_MATH_MEAN = cal_math_avg(["CNT", "ST04Q01"]) # get a series
gaps = []
## I think there must be an easy method
for country in valid_countries:
	gap = CNT_GENDER_MATH_MEAN[country]["Male"] - CNT_GENDER_MATH_MEAN[country]["Female"] 
	gaps.append(gap)

##############THIS WILL BE USED LATER################
CNT_GENDER_MATH_MEAN = pd.DataFrame({
	"CNT": valid_countries, 
	"MATH_GENDER_GAP": gaps
})

INFO = pd.merge(CNT_MATH_MEAN, CNT_RELATIONSHIP,
	how="right", on="CNT")
INFO = pd.merge(INFO, CNT_GENDER_MATH_MEAN,
	how="left", on="CNT")



def draw_scatter_plot(var):
	plt.scatter(x = var, y = "MATH_MEAN", data = INFO)
	y_mean = INFO["MATH_MEAN"].mean()
	x_mean = INFO[var].mean()
	plt.axvline(x = x_mean, color='k', linestyle='--')
	plt.axhline(y = y_mean, color='k', linestyle='--')
	plt.savefig(var + "_math.png")
	plt.show()

# draw_scatter_plot('MATH_GENDER_GAP')

#calculate average for math score and strength



## divide these countries into 9 groups according to relative rank
## position by math_mean and relation_strength
INFO["MATH_INDEX"] = 0
INFO["RELATION_INDEX"] = 0
first_slice = len(INFO["CNT"]) / 3
second_slice = first_slice * 2
third_slice = len(INFO["CNT"])
# notes when using df.loc[,],contrary to usual python slices,
# both the start and the stop are included!
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html

INFO = INFO.sort_values("strength", ascending=False)

INFO.iloc[0:first_slice, 6] = 1
INFO.iloc[first_slice:second_slice, 6] = 2
INFO.iloc[second_slice:third_slice, 6] = 3

# len(INFO[INFO["RELATION_INDEX"] == 2])
# len(INFO[INFO["RELATION_INDEX"] == 1])
# len(INFO[INFO["RELATION_INDEX"] == 3])

INFO = INFO.sort_values("MATH_MEAN", ascending = False)    
# INFO.iloc[0:first_slice]["MATH_MEAN"] = 1
# don't use above line of code to assign values
# INFO.loc[second_slice + 1:third_slice, "MATH_INDEX"] = 3 
#loc is used for labels of index, not position
#maybe I can use the score to divide into three groups!!!!!!!!!!!!!!!!!!!!!!!
INFO.iloc[0:first_slice,5] = 3
INFO.iloc[first_slice:second_slice, 5] = 2
INFO.iloc[second_slice:third_slice, 5] = 1

#calculate average for math score and strength
mean_math_score = INFO["MATH_MEAN"].mean()
mean_strength = INFO["strength"].mean()
INFO = INFO.append({
	"MATH_MEAN": mean_math_score, 
	"strength": mean_strength,
 	"CNT": "AVERAGE"
}, ignore_index=True)

INFO.to_csv("INFO_PISA2012.csv")


america_pisa = pisa2012[pisa2012["CNT"] == "United States of America"][["ESCS", "MATH"]]
america_pisa = america_pisa.dropna()
america_pisa_sample = america_pisa.sample(n = 500)
x = np.array(america_pisa_sample["ESCS"])
y = np.array(america_pisa_sample["MATH"])
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
america_pisa_sample["predict"] = america_pisa_sample["ESCS"] * slope + intercept
america_pisa_sample.to_csv('america_pisa_sample.csv')
