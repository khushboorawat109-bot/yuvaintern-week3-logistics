# YuvaIntern Week 3 - Advanced Data Analysis and Visualization in Logistics

This project simulates a logistics dataset and performs exploratory data analysis (EDA) and visualization.

## Dataset
`logistics_simulated_dataset.csv` contains 1,200 simulated shipments with:
- Region
- Transport mode
- Priority
- Shipment volume
- Distance
- Delivery time
- Transport/handling/total cost
- Fuel cost
- Weather delay
- On-time indicator

## Run
```bash
pip install pandas numpy matplotlib
python src/logistics_visualization.py
```

The `visualizations/` folder contains six generated charts used in the Word report.

## Important
The dataset is synthetic and generated with a fixed random seed (42), so the analysis is reproducible. Results are illustrative and should not be presented as real-world operational measurements.
