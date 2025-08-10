import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def plot_boxplot(df:pd.DataFrame, cols:list[str]):
    """
    Generates and displays box plots for specified numeric columns in a DataFrame.
    Box plots are useful for visualizing the distribution of numerical data and
    identifying potential outliers.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        cols (list[str]): A list of column names for which to generate box plots.
                          If the list is empty, box plots will be generated for all
                          numeric columns in the DataFrame.
    """
    if len(cols) == 0:
        cols = df.columns
    for col in cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            plt.boxplot(df[col])
            plt.xlabel(col, fontsize=8)
            plt.figure(figsize=(10,7))
            plt.show()

def plot_histogram(df:pd.DataFrame,cols:list[str]):
    """
    Generates and displays histograms for numeric columns and count plots for
    non-numeric (categorical) columns in a DataFrame. Histograms show the
    distribution of numeric data, while count plots show the frequency of
    categories.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        cols (list[str]): A list of column names for which to generate plots.
                          If the list is empty, plots will be generated for all
                          columns in the DataFrame.
    """
    i = 0
    if len(cols) == 0:
        cols = df.columns
    for col in cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col], kde=True) # dropna() to handle missing values
            plt.title(f'Distribution of {col}', fontsize=10)
            plt.xlabel(col, fontsize=8)
            plt.ylabel('Frequency', fontsize=8)
            plt.tick_params(axis='both', which='major', labelsize=7)
        else:
            # Use value_counts() to get counts for each category
            sns.countplot(data=df, x=col, order=df[col].value_counts().index, palette='viridis', hue=col)
            plt.title(f'Counts of {col}', fontsize=10)
            plt.xlabel(col, fontsize=8)
            plt.ylabel('Count', fontsize=8)
            plt.xticks(rotation=45, ha='right', fontsize=7)
            plt.tick_params(axis='y', which='major', labelsize=7)
        plt.show()
        i=+1
def correlation_matrix(df:pd.DataFrame, cols:list, name:str):
    """
    Generates and displays a correlation matrix heatmap for the specified columns of a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        cols (list): List of column names to include in the correlation matrix.
        name (str): A name or label to use in the plot title.

    Displays:
        A heatmap plot of the correlation matrix for the specified columns.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title(f'Correlation Matrix for {name}')
    plt.show()
   


