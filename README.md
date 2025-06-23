# AI-CT-Covid-Classifier
This is an ML model that predicts if a patient has Pulmonary Fibrosis or not based on their CT Scans of their Lungs using the SE ResNet50 3D model. 

## Description 

## Data 

Data for this project was acquired from the [Open Source Imaging Pulmonary Fibrosis Progression Competition](https://www.kaggle.com/competitions/osic-pulmonary-fibrosis-progression/overview). The aim of this competition is to predict a patient’s severity of decline in lung function based on a CT scan of their lungs. Lung function is assessed based on output from a spirometer, which measures the forced vital capacity (FVC), i.e. the volume of air exhaled.

In the dataset, competitors were  provided with a baseline chest CT scan and associated clinical information for a set of patients. For the purposes of this project, we were interested in identifying if patients did or did not have Pulmonary Fibrosis based on the baseline CT Scan taken. Thus, a new set of labels was created, which marked all the paitents as having pulmonary fibrosis, which was true of the original dataset. 

labels.csv
0 -> No pulmonary fibrosis 
1 -> pulmonary fibrosis 

## Data Usage Disclosure

Anyone may access and use the Competition Data for any purpose, whether commercial or non-commercial, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. 

## References

[Developing approaches to incorporate donor-lung computed tomography images into machine learning models to predict severe primary graft dysfunction after lung transplantation, Ma et al.](https://pubmed.ncbi.nlm.nih.gov/39924113/)

## Training the Model

The dataset can be downloaded from the original competition on Kaggle. This repository contains the train_labels.csv and test_labels.csv for running the project locally, once you have downloaded the dataset from Kaggle. 

## Running the Model

## Results