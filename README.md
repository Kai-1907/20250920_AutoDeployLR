# 線性回歸示範 (CRISP-DM 流程)

本專案示範如何依據 CRISP-DM 流程，建立簡單線性回歸模型，並透過 Streamlit 部署成互動式網頁應用。

---

##  CRISP-DM 步驟說明

1. **Business Understanding**  
   了解問題：用簡單線性模型 y = ax + b 模擬資料並擬合。

2. **Data Understanding**  
   使用者可自行輸入斜率 a、截距 b、雜訊強度與資料點數量。

3. **Data Preparation**  
   自動生成隨機資料，建立 X 與 y。

4. **Modeling**  
   使用 `LinearRegression()` 進行建模。

5. **Evaluation**  
   輸出模型 R²、MSE、估計參數與圖形化結果。

6. **Deployment**  
   透過 Streamlit Cloud 發佈。

---

##  安裝與執行

### 1️ 安裝套件
```bash
pip install -r requirements.txt
```

### 2️ 本地執行
```bash
streamlit run app.py
```

---

##  部署至 Streamlit Cloud

1. 建立 GitHub Repo，例如  
   **20250920_AutoDeployLR**

2. 上傳以下檔案：
   ```
   app.py
   requirements.txt
   README.md
   ```

3. 前往 [Streamlit Cloud](https://share.streamlit.io)

4. 登入後 → 點選 **"New App"**  
   → 選擇你的 Repo  
   → 指定主檔案為 `app.py`

5. 完成部署後，即可取得一個公開網址  
   例如：  
   https://aiotda.streamlit.app/

---

## 🧠 作者
- 專案名稱：`20250920_AutoDeployLR`
- 製作人：朱仕凱
- 課程作業：HW1 - CRISP-DM 線性回歸
