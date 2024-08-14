import streamlit as st
import pickle
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from metrics_page import show_metrics_page

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

best_model_regressor = data["best_model"]
linear_model_regressor = data["linear_model"]
decision_tree_regressor = data["decision_tree_model"]
random_forest_regressor = data["random_forest_model"]
le_country = data["le_country"]
le_education = data["le_education"]

# regressor = data["model"]
# le_country = data["le_country"]
# le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.markdown("### Models")
    model_choice = st.selectbox(
        "Select model",
        ('Linear Regression', 'Decision Tree', 'Random Forest')
    )


    st.write("""### Provide information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 3)


    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        models = {
            'Linear Regression': linear_model_regressor,
            'Decision Tree': decision_tree_regressor,
            'Random Forest': random_forest_regressor
        }

        selected_model = models[model_choice]
        salary = selected_model.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")