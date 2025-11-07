# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Type: Random Forest Classifier
framework: scikit-learn
Date: November/2025
Author: Maciej Geisheimer

## Intended Use
This model is intended for educational purposes to demonstrate machine lerning techniques on census income data
intended users: Data scientists and machine learning practitioners

## Training Data
Dataset: Census income dataset
size: Approximately 32,000 samples
target variable: "salary"(binary classification: <=50K, >50K)

## Evaluation Data
test split 20% of dataset held out for testing
evalaution strategy: single train-test split
Performance evaluated across all unique categorical feature values

## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision: the proportion of positive predictions that were actually correct
precission score: 0.7419 

Recall: the proportion of actual positive cases that were correctly identified
recall score: 0.6384

F1 Score: the harmonic mean of precision and recall
F1 score: 0.6863

## Ethical Considerations
The model includes sensitive features such as race and sex, which can introduce bias in predictions.

## Caveats and Recommendations
The training data comes from 1994 U.S. Census data, which does not reflect current socioeconomic realities

the model is intended only for educational purposes


