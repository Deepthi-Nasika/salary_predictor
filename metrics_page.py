import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st
import pickle
import pandas as pd

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

best_model_regressor    = data["best_model"]
linear_model_regressor  = data["linear_model"]
decision_tree_regressor = data["decision_tree_model"]
random_forest_regressor = data["random_forest_model"]
le_country              = data["le_country"]
le_education            = data["le_education"]

def show_metrics_page():
    st.title("Performance Metrics of Models")

    st.markdown("### Models")
    model_choice = st.selectbox(
        "Select model",
        ('Linear Regression', 'Decision Tree', 'Random Forest')
    )

    models = {
            'Linear Regression': linear_model_regressor,
            'Decision Tree': decision_tree_regressor,
            'Random Forest': random_forest_regressor
        }

    # selected_model = models[model_choice]
    
    # if model_choice == "Linear Regression":
    #     st.write("")
    #     st.write(f"Mean Absolute Error(MAE):{30479.812}")
    #     st.write(f"Mean Square Error(MSE):{1542506276.874}")
    #     st.write(f"Root Mean Square Error(RMSE):{39274.753}")
    #     st.write(f"R-squared(R2):{0.323}")

    # elif model_choice == "Decision Tree":
    #     st.write("")
    #     st.write(f"Mean Absolute Error(MAE):{19972.535}")
    #     st.write(f"Mean Square Error(MSE):{865238589.711}")
    #     st.write(f"Root Mean Square Error(RMSE):{29414.938}")
    #     st.write(f"R-squared(R2):{0.620}")

    # elif model_choice == "Random Forest":
    #     st.write("")
    #     st.write(f"Mean Absolute Error(MAE):{20166.160}")
    #     st.write(f"Mean Square Error(MSE):{869501373.564}")
    #     st.write(f"Root Mean Square Error(MSE):{29487.308}")
    #     st.write(f"R-squared(R2):{0.618}")

    # Define metrics for each model (These should be computed dynamically in a real scenario)
    metrics = {
        'Linear Regression': {'MAE': 30479.812, 'MSE': 1542506276.874, 'RMSE': 39274.753, 'R2': 0.323},
        'Decision Tree': {'MAE': 19972.535, 'MSE': 865238589.711, 'RMSE': 29414.938, 'R2': 0.620},
        'Random Forest': {'MAE': 20166.160, 'MSE': 869501373.564, 'RMSE': 29487.308, 'R2': 0.618}
    }

    selected_metrics = metrics[model_choice]
    
    # Create a DataFrame for the selected model's metrics
    df_metrics = pd.DataFrame(list(selected_metrics.items()), columns=['Metric', 'Value'])
    
    st.markdown("Performance metrics:")
    # Display the DataFrame as a table
    st.table(df_metrics)
