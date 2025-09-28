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

### Prompt 1: 推送至 GitHub
*   **使用者**: 幫我將整個專案推送至github 網址https://github.com/mimimaomao11/AIoT-HW1

### 執行紀錄
1.  **`git status`** -> `fatal: not a git repository`
2.  **`git init`** -> `Initialized empty Git repository`
3.  **`git remote add origin ...`** -> 成功
4.  **`git add .`** -> 成功
5.  **`git commit -m "Initial commit"`** -> `[master (root-commit) 8959b1f] Initial commit`
6.  **`git push -u origin master`** -> `* [new branch] master -> master`

---

### Prompt 2: 更新 README 與開發日誌
*   **使用者**: streamlit連結為https://aiot-hw1-jgvddr7pkczushaemhatrv.streamlit.app/ 請幫我更新至README以及開發日誌只要留下prompt以及對專案開發有關的詞(修正bug等)，並幫我同步至github

### 執行紀錄
1.  **讀取/寫入檔案** -> 成功更新 `README.md` 和 `devlog.md`
2.  **`git add README.md devlog.md`** -> 成功
3.  **`git commit -m "Update README..."`** -> `[master c1c497c] Update README...`
4.  **`git push`** -> `8959b1f..c1c497c master -> master`

---

### Prompt 3: 記錄所有指令
*   **使用者**: devlog請幫我從一開始到現在所有的指令及結果簡單記錄下來

### 執行紀錄
1.  **寫入 `devlog.md`** -> 成功 (更新日誌以包含所有指令歷史)
2.  **`git add devlog.md`** -> 成功
3.  **`git commit -m "Update devlog..."`** -> `[master 93ea167] Update devlog...`
4.  **`git push`** -> `c1c497c..93ea167 master -> master`

---

### Prompt 4: 根據 app.py 生成開發日誌
*   **使用者**: 幫我從一開始的app.py生成建立一個開發日誌

### 執行紀錄
1.  **讀取 `app.py`** -> 成功
2.  **寫入 `devlog.md`** -> 成功 (基於 `app.py` 重新生成開發日誌)
3.  **`git add devlog.md`** -> 成功
4.  **`git commit -m "Recreate devlog..."`** -> `[master 8e3e57a] Recreate devlog...`
5.  **`git push`** -> `93ea167..8e3e57a master -> master`

---

### Prompt 5: 返回上一個版本並補充日誌
*   **使用者**: 幫我返回上一個版本 並在前面加入2025-09-28的版本...

### 執行紀錄
1.  **`git checkout 93ea167 -- devlog.md`** -> 成功 (還原 `devlog.md`)
2.  **讀取/寫入 `devlog.md`** -> 成功 (在頂部加入 2025-09-28 的初始 prompt)
3.  **`git add devlog.md`** -> 成功
4.  **`git commit -m "Revert devlog..."`** -> `[master 3e195fe] Revert devlog...`
5.  **`git push`** -> `8e3e57a..3e195fe master -> master`

---

### Prompt 6: 完成日誌
*   **使用者**: 保留現在並繼續把剩下的寫完

### 執行紀錄
1.  **讀取/寫入 `devlog.md`** -> 成功 (完成所有歷史紀錄的填寫)
2.  **`git add devlog.md`** -> 執行中...
