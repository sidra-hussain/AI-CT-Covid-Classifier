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

# Step 3: Select and rename columns
output_df = closest_weeks_df[['Patient', 'Weeks', 'FVC', 'Percent']].rename(columns={'Patient': 'patient_id'})

# Step 4: Split into two categories, valid and invalid CTs
between_12 = output_df[(output_df['Weeks'] >= -12) & (output_df['Weeks'] <= 12)].copy()
outside_12 = output_df[(output_df['Weeks'] < -12) | (output_df['Weeks'] > 12)]

# Step 5: Save each to separate CSVs

#binary labeling
between_12['label'] = between_12['Percent'].apply(percent_to_label_binaryclass)
between_12.to_csv('dataset/labels_binary.csv', index=False)

#multiclass labeling
between_12['label'] = between_12['Percent'].apply(percent_to_label_multiclass)
between_12.to_csv('dataset/labels_multi.csv', index=False)

#store the CT scans that are invalid in a seperate CSV
outside_12.to_csv('dataset/labels_invalid.csv', index=False)
