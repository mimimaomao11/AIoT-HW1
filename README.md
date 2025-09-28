# HW1-1: 互動式線性迴歸視覺化工具

**Live Demo:** [https://aiot-hw1-jgvddr7pkczushaemhatrv.streamlit.app/](https://aiot-hw1-jgvddr7pkczushaemhatrv.streamlit.app/)

本專案是一個使用 Streamlit 建構的互動式 Web 應用程式，用於展示簡單線性迴歸的原理。它允許使用者生成模擬數據、擬合迴歸模型並即時視覺化結果。

此應用程式遵循 **CRISP-DM (跨行業數據挖掘標準流程)** 方法論進行建構。

## 線性迴歸專案 To-Do List (CRISP-DM)

- [x] **1. 商業理解 (Business Understanding)**
  - [x] 定義專案目標：建立一個教育工具，以視覺化方式解釋線性迴歸。

- [x] **2. 資料理解 (Data Understanding)**
  - [x] 定義數據生成方式：`y = ax + b + noise`。
  - [x] 允許使用者調整關鍵參數：樣本數、斜率、雜訊。

- [x] **3. 資料準備 (Data Preparation)**
  - [x] 根據使用者輸入生成數據集。
  - [x] 將數據整理成 Pandas DataFrame。

- [x] **4. 模型建立 (Modeling)**
  - [x] 選擇模型：`scikit-learn` 的 `LinearRegression`。
  - [x] 在生成的數據上訓練模型。

- [x] **5. 模型評估 (Evaluation)**
  - [x] 顯示模型係數（斜率和截距）。
  - [x] 計算殘差以評估擬合優度。
  - [x] 識別並列出前 5 個離群值。

- [x] **6. 部署 (Deployment / Visualization)**
  - [x] 建立互動式圖表。
  - [x] 繪製數據散點圖、迴歸線和離群值。
  - [x] 將應用部署到 Streamlit Community Cloud。
