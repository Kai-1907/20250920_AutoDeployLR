import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.title("線性回歸示範 (CRISP-DM 流程)")
# ---- CRISP-DM Step 1: Business Understanding ----
st.header("Step 1: Business Understanding")
st.write("本程式依據 CRISP-DM 流程，示範如何產生模擬資料並建立簡單線性回歸模型。")

# ---- Step 2: Data Understanding ----
st.header("Step 2: Data Understanding")
st.write("請輸入資料生成參數：")

a = st.slider("斜率 a", min_value=-10.0, max_value=10.0, value=4.5, step=0.1)
b = st.slider("截距 b", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
noise = st.slider("雜訊強度 (noise)", 0.0, 200.0, 100.0, 1.0)
n_points = st.slider("資料點數量", 10, 1000, 500, 10)

# ---- Step 3: Data Preparation ----
st.header("Step 3: Data Preparation")
X = np.linspace(0, 10, n_points).reshape(-1, 1)
y = a * X + b + np.random.randn(n_points, 1) * noise
data = pd.DataFrame(np.hstack([X, y]), columns=["X", "y"])
st.dataframe(data.head())

# ---- Step 4: Modeling ----
st.header("Step 4: Modeling")
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# ---- Step 5: Evaluation ----
st.header("Step 5: Evaluation")
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
st.write(f"**R²:** {r2:.3f}")
st.write(f"**MSE:** {mse:.3f}")
st.write(f"**模型估計參數:** 斜率 a = {model.coef_[0][0]:.3f}, 截距 b = {model.intercept_[0]:.3f}")

fig, ax = plt.subplots()
ax.scatter(X, y, label="Data with noise", alpha=0.6)
ax.plot(X, y_pred, color="red", label="Fitted line")
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("y")
st.pyplot(fig)

# ---- Step 6: Deployment ----
st.header("Step 6: Deployment")
st.write("此應用可部署於 Streamlit Cloud。")
st.markdown("[範例部署網址](https://aiotda.streamlit.app/)")
st.markdown("[GitHub 專案範例](https://github.com/huanchen1107/20250920_AutoDeployLR)")
