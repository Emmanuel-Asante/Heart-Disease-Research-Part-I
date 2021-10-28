# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# Use the dataset yes_hd to save cholesterol levels for patients with heart disease as a variable named chol_hd
chol_hd = yes_hd['chol']

# Calculate the mean cholesterol level for patients who were diagnosed with heart disease and print it out
print(np.mean(chol_hd))

# Implementing a One-Sample T-Test for chol_hd (compare sample average to a hypothetical population average)
ttest, pval = ttest_1samp(chol_hd, 240)

# Output the p-value
print(pval/2)

# Interpreting the p-value based on a significance threshold of 0.05
print('Since the p-value of 0.0035 is less than the significant threshold of 0.05, we reject the null hypothesis and suggest that heart disease patients have an average cholesterol level significantly higher than 240 mg/dl\n')

# Use the dataset no_hd to save cholesterol levels for patients without heart disease as a variable named chol_no_hd
chol_no_hd = no_hd['chol']

# Calculate the mean cholesterol level for patients who were not diagnosed with heart disease and print it out
print(np.mean(chol_no_hd))

# Implementing a One-Sample T-Test for chol_no_hd (compare sample average to a hypothetical population average)
ttest, pval = ttest_1samp(chol_no_hd, 240)

# Output the p-value
print(pval/2)

# Interpreting the p-value based on a significance threshold of 0.05
print('Since the p-value of about 0.2640 is greater than the significant threshold of 0.05, we do not reject the null hypothesis and conclude that people without heart disease have an average cholesterol level equal to 240 mg/dl\n')

# Save the number of patients of the heart dataset and save the result in variable named num_patients
num_patients = len(heart)

# Output num_patient
print(num_patients)

# Calculate the number of patients with fasting blood sugar greater than 120. Save this number as num_highfbs_patients
num_highfbs_patients = np.sum(heart.fbs)

# Output num_highfbs_patients
print(num_highfbs_patients)

# Calculate 8% of the sample population
print(0.08*num_patients)

# Run a binomial test to check if the sample came from a population in which the rate of fbs > 120 mg/dl equals 8%
p_value = binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')

# Output p_value
print(p_value)

# Interpreting the p_value
print('The p-value of 0.0000469 which is less than 0.05 indicates that, this sample likely comes from a population where more than 8% of people have fbs > 120 mg/dl.')