# HW1-1: 互動式線性迴歸視覺化工具

本專案是一個使用 Streamlit 建構的互動式 Web 應用程式，用於展示簡單線性迴歸的原理。它允許使用者生成模擬數據、擬合迴歸模型並即時視覺化結果。

此應用程式遵循 **CRISP-DM (跨行業數據挖掘標準流程)** 方法論進行建構。

## CRISP-DM 實作步驟

1.  **商業理解 (Business Understanding)**: 目標是提供一個教育工具，讓使用者直觀地了解樣本數、斜率和數據變異數等參數如何影響線性迴歸模型及離群值的識別。

2.  **資料理解 (Data Understanding)**: 應用程式根據線性方程式 `y = ax + b + noise` 生成模擬數據。使用者可以控制參數 `a` (斜率)、`n` (資料點數量) 和雜訊變異數。截距 `b` 固定為 5。

3.  **資料準備 (Data Preparation)**: 根據側邊欄的使用者輸入，建立一個包含模型所需 `X` 和 `y` 值的 Pandas DataFrame。

4.  **模型建立 (Modeling)**: 使用 `scikit-learn` 的 `LinearRegression` 類別實作一個簡單的線性迴歸模型。該模型在生成的數據集上進行訓練，以找到最佳擬合線。

5.  **模型評估 (Evaluation)**: 應用程式透過以下方式評估模型：
    *   顯示學習到的係數 (斜率) 和截距。
    *   計算殘差 (實際 `y` 值與預測 `y` 值之間的差異)。
    *   透過找到絕對殘差最大的數據點來識別前 5 個離群值，並將它們顯示在表格中。

6.  **部署 (Deployment / Visualization)**: 最後一步是透過 Matplotlib 建立的互動式圖表進行視覺化。圖表顯示：
    *   原始數據點的散點圖。
    *   紅色的擬合線性迴歸線。
    *   標示出的前 5 個離群值。

## 如何在本地端運行

1.  **複製儲存庫或下載檔案。**

2.  **安裝所需的依賴套件：**
    ```bash
    pip install -r requirements.txt
    ```

3.  **運行 Streamlit 應用程式：**
    ```bash
    streamlit run app.py
    ```

    應用程式將在您的預設網頁瀏覽器中打開。

## 如何部署到 Streamlit Community Cloud

1.  **建立 GitHub 儲存庫**: 將您的專案檔案 (`app.py`, `requirements.txt`, `README.md`) 推送到 GitHub 上的新儲存庫。

2.  **註冊 Streamlit Community Cloud**: 如果您還沒有帳戶，請在 [streamlit.io/cloud](https://streamlit.io/cloud) 註冊。

3.  **連接您的 GitHub 帳戶**: 在您的 Streamlit Cloud 儀表板中，連接您的 GitHub 帳戶。

4.  **部署新應用**:
    *   點擊 "New app" 按鈕。
    *   選擇您剛剛建立的 GitHub 儲存庫。
    *   確保分支是正確的 (例如 `main` 或 `master`)。
    *   確保 "Main file path" 設定為 `app.py`。
    *   點擊 "Deploy!"。

5.  **存取您的應用**: Streamlit 將建置並部署應用程式。完成後，您將獲得一個用於線上應用的公開 URL (例如 `https://your-app-name.streamlit.app`)。