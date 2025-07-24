import pandas as pd

# Load the dataset
df = pd.read_csv('dataset/train.csv')

# Step 1: For each patient, find the row where `Weeks` is closest to 0
df['Weeks_abs'] = df['Weeks'].abs()
closest_weeks_df = df.loc[df.groupby('Patient')['Weeks_abs'].idxmin()]

# Step 2: Assign a label based on `Percent` value
#labeling function for multiclass labels
def percent_to_label_multiclass(p):
    if p >= 80: #normal
        return 0
    elif 60 <= p < 80: #mild
        return 1
    elif 50 <= p < 60: #moderate
        return 2
    else:
        return 3 #severe

#labeling function for binary class labels
def percent_to_label_binaryclass(p):
    if p >= 80: #normal
        return 0
    elif p < 80: #not normal
        return 1

#multi class labeling
# closest_weeks_df['label'] = closest_weeks_df['Percent'].apply(percent_to_label_multiclass)

#binary labeling
closest_weeks_df['label'] = closest_weeks_df['Percent'].apply(percent_to_label_binaryclass)

# Step 3: Select and rename columns
output_df = closest_weeks_df[['Patient', 'label', 'Weeks', 'FVC', 'Percent']].rename(columns={'Patient': 'patient_id'})

# Step 4: Split into three categories
between_8 = output_df[(output_df['Weeks'] >= -8) & (output_df['Weeks'] <= 8)]
between_12 = output_df[(output_df['Weeks'] >= -12) & (output_df['Weeks'] <= 12)]
outside_12 = output_df[(output_df['Weeks'] < -12) | (output_df['Weeks'] > 12)]

# Step 5: Save each to separate CSVs
between_8.to_csv('dataset/labels_8_weeks.csv', index=False)
between_12.to_csv('dataset/labels_12_weeks.csv', index=False)
outside_12.to_csv('dataset/labels_invalid_fvc.csv', index=False)
