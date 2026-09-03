import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the simulated dataset
df = pd.read_csv("logistics_simulated_dataset.csv", parse_dates=["Date"])

# EDA
print(df.describe())
print("\nMissing values:\n", df.isna().sum())

numeric = [
    "Shipment_Volume_kg", "Distance_km", "Delivery_Time_days",
    "Transport_Cost", "Handling_Cost", "Total_Cost", "Fuel_Cost",
    "Weather_Delay_days"
]
print("\nCorrelation matrix:\n", df[numeric].corr())

# Example visualization
plt.figure(figsize=(8, 5))
plt.hist(df["Delivery_Time_days"], bins=30)
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (days)")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.show()

# Grouped KPI analysis
print("\nAverage cost by mode:")
print(df.groupby("Transport_Mode")["Total_Cost"].mean().sort_values(ascending=False))

print("\nAverage delivery time by mode:")
print(df.groupby("Transport_Mode")["Delivery_Time_days"].mean().sort_values())

print("\nVolume by region:")
print(df.groupby("Region")["Shipment_Volume_kg"].sum().sort_values(ascending=False))
