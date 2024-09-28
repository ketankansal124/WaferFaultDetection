# 📄✏ Sensor Fault Detection Project

### **Overview**
The **Sensor Fault Detection Project** focuses on detecting anomalies or faults in sensors used in various industrial applications. Sensors play a critical role in monitoring and controlling processes in industries such as manufacturing, energy, and electronics. Early detection of sensor faults is vital to ensure system reliability and reduce downtime.

In this project, we utilize a dataset sourced from Kaggle, which contains sensor data from semiconductor wafers used in integrated circuit manufacturing. These wafers undergo multiple microfabrication processes such as doping, etching, and deposition. Ensuring accurate sensor data during these processes is essential to avoid costly production errors.

The goal of this project is to develop a machine learning-based fault detection system that identifies faulty sensors in real-time, helping prevent defective products and reducing operational inefficiencies.

### **Dataset**
- The dataset used for this project is sourced from **Kaggle** and contains sensor readings from semiconductor manufacturing processes.
- The data is stored in **MongoDB** for scalable and efficient querying.


💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.8 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
5. Run Application
```
python app.py
```

## 🔧 Technologies Used

- **Flask**: A lightweight web framework for building the application and serving machine learning models via API endpoints.
- **Python 3.8**: The core programming language used for implementing the project’s logic and machine learning algorithms.
- **Scikit-learn**: A comprehensive library for machine learning in Python, used for model training, evaluation, and selection.
  
- **XGBoost**: An efficient and scalable implementation of gradient boosting, employed in the project for its performance in classification tasks.
  - **Key Hyperparameters Tuned**:
    - `learning_rate`: Controls the step size at each iteration while moving toward a minimum of the loss function.
    - `max_depth`: Maximum depth of a tree, used to control overfitting.
    - `n_estimators`: The number of trees in the ensemble.
    - `gamma`: Minimum loss reduction required to make a further partition on a leaf node.

- **GradientBoostingClassifier**: A traditional gradient boosting model from Scikit-learn, used for baseline comparisons.
  - **Key Hyperparameters Tuned**:
    - `n_estimators`: Number of boosting stages to be run.
    - `criterion`: Function to measure the quality of a split, specifically using 'friedman_mse' for improved performance.

- **Support Vector Classifier (SVC)**: A powerful classification method that finds the hyperplane that best separates the classes.
  - **Key Hyperparameters Tuned**:
    - `C`: Regularization parameter to control the trade-off between achieving a low training error and a low testing error.
    - `kernel`: Specifies the kernel type to be used in the algorithm, such as 'linear' or 'rbf'.
    - `gamma`: Kernel coefficient for 'rbf', controlling the influence of individual training examples.

- **RandomForestClassifier**: An ensemble learning method for classification that operates by constructing multiple decision trees.
  - **Key Hyperparameters Tuned**:
    - `n_estimators`: Number of trees in the forest.
    - `max_depth`: Maximum depth of the trees to prevent overfitting.
    - `min_samples_split`: Minimum number of samples required to split an internal node.
    - `min_samples_leaf`: Minimum number of samples required to be at a leaf node.

- **Pandas & NumPy**: Essential libraries for data manipulation, analysis, and numerical operations, providing robust data structures and functions.

- **MongoDB**: A NoSQL database used for storing and retrieving large volumes of sensor data efficiently, enabling easy data management and access.


---

## 💡 Features

- **Fault Detection Model**: A machine learning model trained to detect sensor faults using historical data.
- **Real-time Monitoring**: Capable of integrating with real-time systems to continuously monitor sensor health.
- **Database Integration**: Utilizes MongoDB to store and retrieve sensor data for large-scale processing.
- **User Interface**: A simple Flask web application to visualize sensor status and fault detection results.

---

## 🏦 Industrial Use Cases

This sensor fault detection system can be applied to multiple industries, including:

- **Semiconductor Manufacturing**: To detect sensor faults during wafer fabrication processes.
- **Predictive Maintenance**: Monitor sensor health and predict failures before they lead to downtime.
- **Automotive & Aerospace**: Ensure reliability in critical sensor-dependent systems for vehicle control and safety.

---

## 🚀 How It Works

1. **Data Preprocessing**: The sensor data is cleaned, normalized, and preprocessed to ensure accurate model training.
2. **Model Training**: A supervised machine learning model is trained using historical sensor data, classifying readings as normal or faulty.
3. **Prediction**: The model predicts whether the incoming sensor readings are faulty based on learned patterns.
4. **Alerts**: If a fault is detected, the system generates alerts for immediate action, reducing potential downtimes.

## 📈 Results & Performance

The model has been evaluated using common metrics such as:

- **Accuracy**: The overall correctness of the model.
- **Precision**: The ratio of true positive predictions to the total positive predictions.
- **Recall**: The ratio of true positive predictions to the actual positives in the dataset.
- **F1-score**: The harmonic mean of precision and recall, providing a balance between the two.

Achieved over **96% accuracy** in identifying faulty sensors from the test dataset.

---

## 📚 References

- Kaggle: [Semiconductor Sensor Data](https://www.kaggle.com/your-dataset)


