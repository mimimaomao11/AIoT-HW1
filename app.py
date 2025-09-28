
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- 1. Business Understanding ---
st.set_page_config(page_title="Interactive Linear Regression Visualizer", layout="wide")
st.title("HW1-1: Interactive Linear Regression Visualizer")
st.markdown("""
This interactive web application is designed to help users understand the fundamentals of linear regression. 
By allowing real-time manipulation of data parameters (sample size, slope, and noise), users can instantly 
see how these changes affect the data distribution, the fitted regression model, and the identification of outliers.
The application follows the CRISP-DM methodology.
""")

# --- 2. Data Understanding ---
st.sidebar.header("Data Generation Parameters")
st.sidebar.markdown("""
Configure the parameters for generating synthetic data. The data is created using the linear equation `y = ax + b + noise`, where `b` is fixed at 5.
""")

n_points = st.sidebar.slider("Number of data points (n)", min_value=100, max_value=1000, value=200, step=10)
a_slope = st.sidebar.slider("Slope (a)", min_value=-10.0, max_value=10.0, value=2.5, step=0.1)
noise_variance = st.sidebar.slider("Noise Variance", min_value=0.0, max_value=1000.0, value=100.0, step=10.0)
b_intercept_fixed = 5

# --- 3. Data Preparation ---
@st.cache_data
def generate_data(n, a, noise_var, b):
    """Generates synthetic data based on user-defined parameters."""
    X = np.random.rand(n, 1) * 10  # Feature values between 0 and 10
    noise = np.random.randn(n, 1) * np.sqrt(noise_var)
    y = a * X + b + noise
    df = pd.DataFrame(data=np.hstack([X, y]), columns=['X', 'y'])
    return df

data = generate_data(n_points, a_slope, noise_variance, b_intercept_fixed)
X = data[['X']]
y = data['y']

# --- 4. Modeling ---
@st.cache_data
def fit_model(_data):
    """Fits a linear regression model to the provided data."""
    model = LinearRegression()
    model.fit(_data[['X']], _data['y'])
    return model

model = fit_model(data)
y_pred = model.predict(X)
data['y_pred'] = y_pred

# --- 5. Evaluation ---
st.header("Model Evaluation")

# Calculate residuals and identify outliers
data['residuals'] = np.abs(data['y'] - data['y_pred'])
data_sorted_by_residuals = data.sort_values(by='residuals', ascending=False)
top_5_outliers = data_sorted_by_residuals.head(5)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Regression Coefficients")
    st.metric(label="Coefficient (Slope)", value=f"{model.coef_[0]:.4f}")
    st.metric(label="Intercept", value=f"{model.intercept_:.4f}")

with col2:
    st.subheader("Top 5 Outliers")
    st.markdown("The table below lists the top 5 data points with the largest absolute residuals, which are considered outliers.")
    st.dataframe(top_5_outliers[['X', 'y', 'residuals']].style.format({
        'X': '{:.2f}',
        'y': '{:.2f}',
        'residuals': '{:.2f}'
    }))

# --- 6. Deployment (Visualization) ---
st.header("Data Visualization")
st.markdown("The scatter plot shows the generated data points, the fitted regression line (in red), and the top 5 identified outliers (labeled in red).")

fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plot of the data
ax.scatter(data['X'], data['y'], alpha=0.6, label='Generated Data')

# Regression line
ax.plot(data['X'], data['y_pred'], color='red', linewidth=2, label='Regression Line')

# Annotate top 5 outliers
for i, row in top_5_outliers.iterrows():
    ax.scatter(row['X'], row['y'], color='red', s=50, edgecolors='black') # Highlight outlier point
    ax.text(row['X'], row['y'], f"({row['X']:.1f}, {row['y']:.1f})", fontsize=9, color='red', ha='left', va='bottom')

ax.set_title("Linear Regression Fit and Outlier Detection", fontsize=16)
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.legend()
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

st.pyplot(fig)

st.info("""
**How to Interpret the Visualization:**
- **Blue Points:** The synthetic data points you generated.
- **Red Line:** The best-fit line calculated by the linear regression model.
- **Red-Highlighted Points & Labels:** The top 5 points that are furthest from the regression line (outliers).
""")
