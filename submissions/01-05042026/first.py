import os
from narwhals import corr
from narwhals import corr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from py_compile import main
from pandas.plotting import scatter_matrix


features = [
    'Temperature_C',
    'Vibration_Hz',
    'Power_Consumption_kW',
    'Network_Latency_ms',
    'Packet_Loss_%',
    'Quality_Control_Defect_Rate_%',
    'Production_Speed_units_per_hr',
    'Predictive_Maintenance_Score',
    'Error_Rate_%'
]

def read_csv_file(csv_path):
    df = pd.read_csv(csv_path)
    print(f"Read CSV file: {csv_path}")
    print(df.head())
    return df


def plot_data(df):
    scatter_matrix(
        df[features],
        figsize=(14,14)
    )

    corr = df[features].corr()
    print(corr)
    plt.figure(figsize=(10,8))
    plt.imshow(corr)
    plt.colorbar()
    plt.xticks(range(len(features)), features, rotation=90)
    plt.yticks(range(len(features)), features)
    plt.title("Correlation Matrix")
    plt.show()

    # plt.scatter(df['Vibration_Hz'], df['Error_Rate_%'])
    # plt.xlabel('Vibration (Hz)')
    # plt.ylabel('Error Rate (%)')
    # plt.title('Vibration vs Error Rate')
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.plot(df['x'], df['y'], marker='o')
    # plt.title('Sample Plot')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.grid()
    # plt.show()

    
def main():
    df = read_csv_file('./manufacturing_6G_dataset.csv')
    plot_data(df)

if __name__ == "__main__":
    main()