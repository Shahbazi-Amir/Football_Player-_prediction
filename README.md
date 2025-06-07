# Final Report: Predicting Manchester City Wins

Introduction: This project analyzes and predicts Manchester City wins using weather data  
(temperature, humidity, precipitation, wind speed, pressure) and home/away status. The goal  
was to identify key influencing factors and develop predictive models using Random Forest  
and XGBoost. The project was conducted from start to June 07, 2025.

Initial Data: Data was extracted from the `final_corrected_dataset.csv` file, containing  
results and weather variables for 38 Manchester City matches. Columns included `Teams_Result`  
(match outcome), `Match_ID` (match identifier), and weather variables (temperature, humidity,  
precipitation, wind speed, pressure). Initially, `Win` (1 for win, 0 for loss) and `IsHome`  
(1 for home games, 0 for away games) columns were created by processing the text results.

Data Cleaning and Preparation: Data was cleaned based on reasonable ranges. Values outside  
limits (humidity 0-100%, pressure 900-1100 hPa, temperature -10 to 40°C, wind speed 0-40  
m/s, precipitation 0-50 mm) were replaced with mean or default values (e.g., 50% for humidity,  
1013.25 for pressure). Data was aggregated by `Match_ID` to create one row per match. The  
number of rows before and after cleaning was checked to avoid complete data loss.

Features and Variables: Final features included `Temperature`, `Humidity`, `Precipitation`,  
`WindSpeed`, `Pressure`, and `IsHome`. These were normalized using StandardScaler and  
balanced with SMOTE to address class imbalance (29 wins vs. 9 losses).

Modeling:  
- Random Forest: Optimized with GridSearchCV using `n_estimators` (200, 300), `max_depth`  
  (5, 7, 9), `min_samples_split` (2, 5), and `max_samples` (0.8). Best parameters were  
  `max_depth=7`, `max_samples=0.8`, `min_samples_split=2`, `n_estimators=200`.  
- XGBoost: Optimized with GridSearchCV using `n_estimators` (200, 300), `max_depth` (3, 5,  
  7), and `learning_rate` (0.2, 0.3, 0.5). Best parameters were `learning_rate=0.2`,  
  `max_depth=5`, `n_estimators=300`. Validation was performed with Stratified K-Fold (10  
  folds).

Results:  
- Random Forest: Accuracy 84.21%. Confusion matrix `[[ 5  4], [ 2 27]]`. Classification  
  report: Class 0 (Loss) Precision 0.71, Recall 0.56, F1-score 0.62; Class 1 (Win) Precision  
  0.87, Recall 0.93, F1-score 0.90. Cross-Validation F1 0.7564 (±0.2633). Feature  
  importance: Temperature 0.2867, Humidity 0.2406, IsHome 0.2068, Precipitation 0.1804,  
  WindSpeed 0.0856, Pressure 0.0000.  
- XGBoost: Accuracy 78.95%. Confusion matrix `[[ 2  7], [ 1 28]]`. Classification report:  
  Class 0 (Loss) Precision 0.67, Recall 0.22, F1-score 0.33; Class 1 (Win) Precision 0.80,  
  Recall 0.97, F1-score 0.88. Cross-Validation F1 0.6836 (±0.2522). Feature importance:  
  IsHome 0.3368, Precipitation 0.2346, Temperature 0.2110, WindSpeed 0.1331, Humidity 0.0845,  
  Pressure 0.0000.

Visual Analysis: Feature importance plots highlighted `IsHome` and temperature as key factors.  
Win rates were higher for home games at 10-15°C with no precipitation. ROC Curve showed  
Random Forest (AUC ~0.80) outperforming XGBoost (AUC ~0.75).

Conclusion: Random Forest with 84.21% accuracy and a Recall of 0.56 for losses outperformed  
XGBoost (Recall 0.22). Key factors were `IsHome` and temperature. Limitations include limited  
data (38 samples) and potential overfitting with SMOTE.

Recommendations: Collect data from additional seasons, schedule home games in favorable  
conditions (10-15°C, no rain), and test new models (e.g., SVM) with different parameters.

This report was completed on June 07, 2025, at 06:37 PM +04.