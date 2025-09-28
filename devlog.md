# 開發日誌

## 2025-09-28

### 專案初始化
*   **`app.py`**: 使用 Streamlit 建立了主要的應用程式檔案。它包含了生成、建模和視覺化線性迴歸數據的完整 CRISP-DM 工作流程。
*   **`requirements.txt`**: 為專案生成了所有必要的 Python 套件列表 (`streamlit`, `scikit-learn`, `pandas`, `numpy`, `matplotlib`)。
*   **`README.md`**: 建立了一個詳細的 README 檔案，說明專案目的、本地設定說明以及 Streamlit Community Cloud 的部署指南。

### 執行與偵錯
1.  **依賴套件安裝**: 使用 `pip install -r requirements.txt` 成功安裝了所有必要的套件。
2.  **初次運行嘗試**: `streamlit run app.py` 命令執行失敗。
    *   **原因**: 在使用者級別安裝後，`streamlit` 執行檔未被找到於系統的 PATH 環境變數中。
3.  **第二次運行嘗試**: 改用 `python -m streamlit run app.py` 以確保可以找到模組。
    *   **問題**: 這觸發了 Streamlit 的一個互動式設定提示，要求輸入電子郵件，導致執行暫停。
4.  **第三次運行嘗試**: 嘗試以無頭模式 (`--server.headless true`) 運行應用程式以繞過互動式提示。此命令被使用者取消。