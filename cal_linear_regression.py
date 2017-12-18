# coding: utf-8
CNT_MATH_MEAN.sort_values("MATH_MEAN", ascending=False)
country_phase_math_means
pisa2012
pisa2012[[:,"PV1MATH":"PV5MATH"]]
pisa2012[:,"PV1MATH":"PV5MATH"]
pisa2012.loc[:,"PV1MATH":"PV5MATH"]
pisa2012["MATH"]
pisa2012["MATH"] = pisa2012.loc[:, "PV1MATH":"PV5MATH"].mean()
pisa2012["MATH"]
pisa2012["MATH"] = (pisa2012["PV1MATH"] + pisa2012["PV2MATH"] + pisa2012["PV3MATH"] + pisa2012["PV4MATH"] + pisa2012["PV5MATH"]) / 5
pisa2012["MATH"]
countries = CNT_MATH_MEAN["CNT"]
countries
slopes = []
strengths  = []
def cal_linear_regression():
    for country in countries:
        country_escs_math_data = pisa2012[pisa2012["CNT"] = country][["CNT", "ESCS"]]
def cal_linear_regression():
    for country in countries:
        country_escs_math_data = pisa2012[pisa2012["CNT"] == country][["MATH", "ESCS"]] 
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(country_escs_math_data["ESCS"], country_escs_math_data["MATH"])
        slopes.append(slope)
        strengths.append(r_value ** 2)
          
import scipy
