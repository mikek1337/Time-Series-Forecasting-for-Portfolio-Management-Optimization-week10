# Financial Time Series Analysis Project

This project contains notebooks and scripts for performing Exploratory Data Analysis (EDA) and calculating risk metrics on historical financial time series data.

## 1. Project Overview

This repository provides a practical demonstration of financial time series analysis. It covers data acquisition, preparation, exploratory data analysis to identify trends and patterns, and the calculation of fundamental risk and return metrics.

## 2. Project Structure

The project is organized into the following directories:

- **`data/`**: Contains the raw historical stock data (e.g., `BND.csv`, `SPY.csv`, `TSLA.csv`).
    
- **`notebooks/`**: Houses the Jupyter notebooks for analysis.
    
    - `eda.ipynb`: The primary notebook for Exploratory Data Analysis.
        
    - `model.ipynb`: (Future) Notebook for developing forecasting models.
        
- **`scripts/`**: Contains Python helper scripts.
    
    - `plots.py`: Custom functions for creating visualizations.
        
    - `preprocess.py`: Custom functions for data preprocessing, including outlier detection.
        
- **`requirements.txt`**: Lists all necessary Python dependencies.
    

## 3. Getting Started

Currently, the main entry point for analysis is the `eda.ipynb` notebook. Follow these steps to set up and run the project locally.

### 3.1. Prerequisites

Ensure you have Python 3.x installed on your system.

### 3.2. Setup Process

1. **Clone the Repository**:
    
    ```
    git clone https://github.com/mikek1337/Time-Series-Forecasting-for-Portfolio-Management-Optimization-week10.git
    cd Time-Series-Forecasting-for-Portfolio-Management-Optimization-week10
    ```
    
   
    
2. **Create a Virtual Environment** (Recommended):
    
    ```
    python -m venv .venv
    ```
    
3. **Activate the Virtual Environment**:
    
    - **On Windows**:
        
        ```
        .venv\Scripts\activate
        ```
        
    - **On macOS/Linux**:
        
        ```
        source .venv/bin/activate
        ```
        
4. **Install Dependencies**: Navigate to the project root directory where `requirements.txt` is located and install all necessary packages:
    
    ```
    pip install -r requirements.txt
    ```

5. **Create Data folder**
    ```
    mkdir data
    mkdir data/processed
    ```
    

    
6. **Run the EDA Notebook**: Navigate to the `notebooks/` directory and launch Jupyter Lab or Jupyter Notebook:
    
    ```
    cd notebooks/
    jupyter lab  # or jupyter notebook
    ```
    
    Once Jupyter Lab/Notebook opens in your browser, click on `eda.ipynb` to open and run the notebook cells sequentially.