# Data Visualization and Model Prediction Platform

A web-based platform for visualizing datasets and predicting outcomes using multiple machine learning models with automatic preprocessing and model evaluation.

---

## Description

This project allows users to upload datasets, perform real-time data visualization, analyze patterns, and generate predictions using various ML algorithms. The system preprocesses the dataset (handles nulls, types, duplicates), reduces features, trains multiple ML models, and shows the best model based on accuracy. It integrates an intuitive web UI with a powerful Django + Python backend.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Applications](#applications)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [License](#license)
- [Author](#author)

---

## Installation

1. **Clone the repository:**

```
git clone https://github.com/YourUsername/Data-Visualization-ML-Prediction.git
cd Data-Visualization-ML-Prediction
```

#### 2. Install Dependencies :
```
pip install -r requirements.txt
```

#### 3. Run the Project :
```
python manage.py runserver
```

## Usage

### 1: Upload Dataset
- Users upload .csv datasets through the UI.

### 2: Preprocessing Steps (Done Automatically)
- Handling null values
- Removing duplicates
- Converting datatypes
- Feature scaling (normalization/standardization)
- Feature selection & dimensionality reduction

### 3: Visualize Data
The platform provides:

- Bar, Line, Scatter, Area, Pie, and Histogram plots
- Drag-and-drop column selectors for X, Y, and Z axes
- Real-time interactive charts using Chart.js

### 4: Model Prediction
The system trains multiple machine learning models:

- Logistic Regression

- Random Forest

- K-Nearest Neighbors

- Support Vector Machine

- Decision Tree

- Naive Bayes

- Gradient Boosting

### 5: Display Best Model
Accuracy of each model is evaluated and the best-performing model is displayed to the user with metrics.


## Applications

### 1. Data Science Learning Tool
Great for beginners to learn how ML models work and how preprocessing impacts prediction.

### 2. Exploratory Data Analysis (EDA)
Used in real-world projects to visualize datasets before building ML models.

### 3. AutoML-like System
Automates ML workflow from raw CSV to insights, including preprocessing and evaluation.

### 4. Business Insights
Upload company data to forecast sales, customer churn, or behavior with ease.

## Features
### End-to-End Machine Learning Workflow
- Preprocess, visualize, train, and evaluate models all in one place.

- Eliminates the need to code ML pipelines manually.

### Drag and Drop Axis Selection for Graphs
- Simple UI to select graph dimensions.
- Auto-generates different graph types like bar, scatter, area, and more.
- Multiple Model Comparison
- Automatically trains multiple algorithms.

### Compares and displays model with highest accuracy.

- Real-Time Visualization
- Interactive, responsive charts with HTML/CSS/JS and Chart.js.
- Supports 1D, 2D, and 3D graphs depending on column selection.


## Tech Stack
### Core Technologies
### Python
Preprocessing and ML model training using pandas, sklearn, numpy, etc.

### Django
Manages backend logic, API routes, and model evaluation pipeline.

### HTML / CSS / JavaScript
Frontend interface for drag-and-drop, visualization, and interactions.

### Chart.js
Renders dynamic charts in the browser.


## License
This project is open-source and available under the [MIT License](LICENSE).  
© 2025 Sruthi Pulipati

## Author
**Sruthi Pulipati**

This project was built to make data science accessible by combining automation, visualization, and real-time model training in a single, easy-to-use web application as a part of MINI-PROJECT.
