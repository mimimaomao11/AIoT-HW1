# 開發日誌

## 2025-09-28: 專案初始化

### Prompt
*   **使用者**: 
I want to create a Python project for homework called 
**HW1-1: Interactive Linear Regression Visualizer**.

Please generate the following files:

1. **app.py**
   - Use Streamlit for an interactive web app.
   - Follow CRISP-DM methodology with clear markdown comments:
     Business Understanding, Data Understanding, Data Preparation,
     Modeling, Evaluation, Deployment.
   - Functionality:
     * Generate synthetic data y = ax + b + noise
     * Allow user to configure:
       - number of points n (100–1000)
       - slope a (-10 to 10)
       - noise variance (0–1000)
       - (optional) intercept b = fixed at 5
     * Fit linear regression (scikit-learn).
     * Plot scatter data + regression line (red).
     * Detect and label top 5 outliers (largest residuals).
     * Show regression coefficients and intercept.
     * Display top 5 outliers in a table.

2. **requirements.txt**
   - List all dependencies needed for deployment on Streamlit Cloud.

3. **README.md**
   - Explain project purpose, CRISP-DM steps, usage instructions.
   - Show how to run locally (`streamlit run app.py`).
   - Show how to deploy to Streamlit Cloud:
     - Push repo to GitHub
     - Connect GitHub repo to Streamlit Community Cloud
     - Select `app.py` as entry point
     - Deploy and get URL like https://xxx.streamlit.app

Make sure the code is ready to run and deploy without modification.

### 產出
*   `app.py`
*   `README.md`
*   `requirements.txt`

---

## 2025-09-29: 版本控制與部署

### 1. Git 初始化與首次推送
*   **Prompt**: 將整個專案推送至 GitHub。
*   **操作**:
    *   `git init` - 初始化本地儲存庫。
    *   `git remote add origin ...` - 新增遠端 GitHub 儲存庫。
    *   `git add .` -> `git commit` -> `git push` - 完成首次程式碼推送。

### 2. 部署至 Streamlit Cloud
*   **Prompt**: 更新 README，加入 Streamlit 部署連結。
*   **操作**:
    *   手動將專案部署到 Streamlit Community Cloud。
    *   取得部署連結: `https://aiot-hw1-jgvddr7pkczushaemhatrv.streamlit.app/`
    *   更新 `README.md`，加入 Live Demo 連結。
    *   將變更推送到 GitHub。

### 3. 文件整理與迭代
*   **Prompt**: 根據互動過程，多次更新與整理 `devlog.md` 和 `README.md`。
*   **操作**:
    *   **重新生成開發日誌**: 根據 `app.py` 的結構，建立一份詳細的開發過程日誌。
    *   **還原並補充日誌**: 應使用者要求，還原日誌到特定版本，並在開頭補充初始 prompt。
    *   **完成日誌**: 根據完整的互動歷史，最終整理並完成所有開發日誌條目。
    *   **修改 README**: 將 `README.md` 的內容修改為 To-Do List 格式。
    *   所有文件變更均已同步至 GitHub。

