# coding: utf-8
get_ipython().magic(u'run get_concerned_countries.py')
country = "Japan"
data = pisa2012[pisa2012["CNT"] == country][["ESCS", "MATH"]]
modified = data.dropna()
modified
x = np.array(modified["ESCS"])
y = np.array(modified["MATH"])
x
y
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
slope
get_ipython().magic(u'pinfo import')
import
get_ipython().magic(u'pinfo import')
get_ipython().magic(u'paste')
cal_linear_regression()
slopes
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
cal_linear_regression()
slopes
len(slopes)
len(countries)
len(strengths)
country = "Albania"
country_escs_math_data = pisa2012[pisa2012["CNT"] == country][["MATH", "ESCS"]]
country_escs_math_data
a = [1, 3,4]
a.pop(3)
a.pop(3,0)
a.remove(3)
a
countries.remove("Albania")
countries = np.array(countries)
countries.remove("Albania")
countries = CNT_MATH_MEAN["CNT"]
countries = countries.values
type(countries)
get_ipython().magic(u'paste')
len(valid_countries)
len(strengths)
get_ipython().magic(u'paste')
CNT_RELATIONSHIP
type(CNT_RELATIONSHIP)
CNT_RELATIONSHIP = pd.DataFrame({ "CNT": valid_countries, "slope": slopes, "strength": strengths })
CNT_RELATIONSHIP
CNT_RELATIONSHIP.sort_values("slope", ascending=False)
CNT_RELATIONSHIP.sort_values("strength")
a = [1,5]
a
a.concat(7)
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
CNT_GENDER_MATH_MEAN
type(CNT_GENDER_MATH_MEAN)
pd.melt(CNT_GENDER_MATH_MEAN)
CNT_GENDER_MATH_MEAN = pd.DataFrame({ "CNT": CNT_GENDER_MATH_MEAN.index, "MATH_MEAN": CNT_GENDER_MATH_MEAN.values })
CNT_GENDER_MATH_MEAN
pd.melt(CNT_GENDER_MATH_MEAN)
CNT_GENDER_MATH_MEAN = cal_math_avg(["CNT", "ST04Q01"]) # get a series
CNT_GENDER_MATH_MEAN
CNT_GENDER_MATH_MEAN("Vietnam", "female")
CNT_GENDER_MATH_MEAN["Vietnam", "female"]
CNT_GENDER_MATH_MEAN[("Vietnam", "female")]
CNT_GENDER_MATH_MEAN["Vietnam", "female"]
CNT_GENDER_MATH_MEAN["Vietnam"]["female"]
CNT_GENDER_MATH_MEAN
CNT_GENDER_MATH_MEAN["Vietnam"]
CNT_GENDER_MATH_MEAN["Vietnam"]["Female"]
CNT_GENDER_MATH_MEAN["Female"]
get_ipython().magic(u'paste')
CNT_GENDER_MATH_MEAN
