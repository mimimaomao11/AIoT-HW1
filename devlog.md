# 開發日誌

## 2025-09-28

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

## 2025-09-29

### Prompt 1
*   **使用者**: 幫我將整個專案推送至github 網址https://github.com/mimimaomao11/AIoT-HW1

### 執行紀錄
1.  **`git status`**
    *   **結果**: `fatal: not a git repository` (失敗，非 git 儲存庫)
2.  **`git init`**
    *   **結果**: `Initialized empty Git repository` (成功，初始化儲存庫)
3.  **`git remote add origin https://github.com/mimimaomao11/AIoT-HW1`**
    *   **結果**: 成功
4.  **`git add .`**
    *   **結果**: 成功 (將所有檔案加入暫存區)
5.  **`git commit -m "Initial commit"`**
    *   **結果**: `[master (root-commit) 8959b1f] Initial commit` (成功，建立初始版本)
6.  **`git push -u origin master`**
    *   **結果**: `* [new branch]      master -> master` (成功，推送到 GitHub)

---

### Prompt 2
*   **使用者**: streamlit連結為https://aiot-hw1-jgvddr7pkczushaemhatrv.streamlit.app/ 請幫我更新至README以及開發日誌只要留下prompt以及對專案開發有關的詞(修正bug等)，並幫我同步至github

### 執行紀錄
1.  **讀取 `README.md` 和 `devlog.md`**
    *   **結果**: 成功
2.  **寫入 `README.md`** (更新 Streamlit 連結)
    *   **結果**: 成功
3.  **寫入 `devlog.md`** (根據 prompt 精簡內容)
    *   **結果**: 成功
4.  **`git add README.md devlog.md`**
    *   **結果**: 成功
5.  **`git commit -m "Update README with Streamlit link and filter devlog"`**
    *   **結果**: `[master c1c497c] Update README...` (成功)
6.  **`git push`**
    *   **結果**: `8959b1f..c1c497c  master -> master` (成功，同步變更)

---

### Prompt 3
*   **使用者**: devlog請幫我從一開始到現在所有的指令及結果簡單記錄下來

### 執行紀錄
1.  **寫入 `devlog.md`** (更新日誌以包含所有指令歷史)
    *   **結果**: 執行中...