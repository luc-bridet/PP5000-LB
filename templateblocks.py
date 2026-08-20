
#%% Setup


## The document uses a small synthetic dataset.

import pandas as pd
import statsmodels.formula.api as smf

df_RBY_9d8 = pd.DataFrame(
    {
        "R9d8": [
            30, 35, 40, 45, 50,
            55, 60, 65, 70, 75
        ],
        "B9d8": [
            60, 55, 62, 58, 61,
            57, 63, 59, 64, 60
        ]
    }
)

df_RBY_9d8["purple_9d8"] = (
    df_RBY_9d8["R9d8"]
    +
    df_RBY_9d8["B9d8"]
)

df_RBY_9d8["orange_9d8"] = (
    df_RBY_9d8["R9d8"]
    +
    40
)

print(df_RBY_9d8)


#%% Predicting orange9d8 from R9d8


## This text belongs to the implicit default block.


results_R = smf.ols(
    "orange_9d8 ~ R9d8",
    data=df_RBY_9d8
).fit()

print(
    results_R.summary()
)


## More default text.




#%% Conditional means


## This section illustrates multiple explicit block types inside a single
## section.


conditional_means = (
    df_RBY_9d8
    .groupby("purple_9d8")
    ["orange_9d8"]
    .mean()
    .reset_index()
)

print(
    conditional_means
)







#%% Centering the predictor typeofframp keywordsinterceptcovariates


## This section demonstrates a non-core enrichment topic.


purple_mean = (
    df_RBY_9d8["purple_9d8"]
    .mean()
)

df_RBY_9d8["purple_9d8_centered"] = (
    df_RBY_9d8["purple_9d8"]
    -
    purple_mean
)

print(
    df_RBY_9d8[
        [
            "purple_9d8",
            "purple_9d8_centered"
        ]
    ]
)




#%% Practice questions typeexercise keywordsregressionstandard






#%% Larger sample size typevariant keywordswithin variation Standard errorclose







#%% Full regression output typeappendix keywordsmodelsummarythe residual




print(
    results_R.summary()
)
