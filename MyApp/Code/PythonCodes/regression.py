import pandas as pd
import numpy as np

from sklearn.metrics import (mean_squared_error, r2_score)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.svm import SVR, SVC
from sklearn.compose import ColumnTransformer

def regression_models(data):
    df = data

    # Separate features and target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Determine task type
    task_type = "regression" if y.dtype == 'float64' or y.dtype == 'int64' else "classification"

    if(task_type == "classification") :
        return None

    # Identify column types
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object', 'bool']).columns

    # Preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
        ])

    X_processed = preprocessor.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

    max_iter_dynamic = X_train.shape[0] * X_train.shape[1]

    # Final result structure
    results = {
        "regression": {},
        "classification": {}
    }

    
    models = {
        "Linear Regression": LinearRegression(),
        "Polynomial Regression (degree=2)": make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
        "Ridge Regression": Ridge(),
        "Lasso Regression": Lasso(max_iter=max_iter_dynamic),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "SVR": SVR(),
        "XGBoost (Gradient Boosting)": GradientBoostingRegressor()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, predictions)

        results["regression"][name] = {
            "MSE": round(mse, 4),
            "RMSE": round(rmse, 4),
            "R2_Score": round(r2, 4)
        }

    print(results)

    return results
