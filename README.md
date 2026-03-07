# 🌬️ Real-Time Air Pollution Monitor Dashboard (India)

A live ETL pipeline and visualization project that monitors air quality across India. This project extracts data from government APIs, processes it via Python/Pandas, and visualizes real-time insights through a Tableau dashboard.

---

## 🏗️ Data Architecture & Flow

The system follows a classic **ETL (Extract, Transform, Load)** pattern to ensure data remains live and accurate.

1.  **Extraction:** A `.py` script connects to the **Government Air Quality API** to fetch raw JSON/XML data.
2.  **Transformation (Pandas):** * Retrieves raw payloads into DataFrames.
    * Performs **Data Cleansing** (handling missing values, formatting timestamps).
    * Calculates statistical metrics (Min, Max, Avg) for each pollutant.
3.  **Loading:** The cleaned data is stored as a structured `.csv` / `.xlsx` file.
4.  **Automation:** The Python script runs on a refresh cycle, fetching new data to keep the dataset "Live."
5.  **Visualization:** **Tableau** connects to the processed file via a live connection to render the final dashboard.

---

## 📊 Key Insights & Visualizations

### 1. Geospatial Pollution Distribution
An interactive **Choropleth Map of India** visualizing pollution levels across all states.
* **Finding:** **Delhi** is rendered in the highest intensity color, indicating it as the national hotspot for air toxicity.

### 2. Pollutant Composition (The "Dust" Factor)
A pie chart analysis reveals the primary drivers of poor air quality:
* **Particulate Matter dominance:** $PM_{2.5}$ (**33%**) and $PM_{10}$ (**28%**) combined contribute over **61%** of total pollution, proving that dust particles are the primary concern.
* **Surprising Ozone Levels:** $O_3$ accounts for **12%**, ranking third, followed by Carbon Monoxide ($CO$) at **11%**.

### 3. State-wise Rankings
A horizontal (Y-axis) bar chart ranks the top 10 most polluted states.
1. **Delhi** (Highest)
2. **Maharashtra**
3. **Haryana**
* **Regional Observation:** Southern Indian states consistently show significantly lower contribution to overall air pollution compared to the Northern belt.

### 4. Pollutant Statistical Ranges
A grouped bar chart for each pollutant type displaying:
* **Average ($Avg$):** The baseline exposure.
* **Maximum ($Max$):** Peak pollution events.
* **Minimum ($Min$):** Best-case scenarios at specific timestamps.

### 5. Sensor Integrity Validation
To ensure the high particulate matter readings weren't skewed by a higher density of sensors, a validation bar chart was created to count sensors per pollutant.
* **The Logic:** If $PM_{2.5}$ had 500 sensors and $SO_2$ had 10, the data would be biased.
* **The Result:** Sensor counts are remarkably consistent, ranging only between **123 and 147** (a delta of only 7–5% across types). 
* **Conclusion:** Even though $PM_{2.5}$ and $PM_{10}$ have slightly *fewer* sensors than some other pollutants, they still record the highest levels, confirming the pollution is real and not a result of sampling bias.

### 6. K-Means Clustering (Station Behavior)
We applied **K-Means Clustering** to group monitoring stations with similar pollution profiles.
* **Scope:** 4D clustering based on $NO_2$, $O_3$, $PM_{10}$, and $PM_{2.5}$.
* **Outlier Analysis:** The scatter plot clearly identifies Delhi stations as a distinct outlier cluster, showing extreme values across all four pollutant dimensions simultaneously.

### 7. Pollution Intensity Heatmap
A high-density heatmap used to visualize the "Pollution Count"—tracking where and when the air quality index crosses hazardous thresholds most frequently.

---
## 🛠️ Tech Stack
* **Data Source:** Government Open Data API
* **Data Engineering:** Python, Pandas, NumPy
* **Machine Learning:** Tableu K-Means clustering (unsupervised Machine learning)
* **Visualization:** Tableau
* **Automation:** Python Scripting (`.py`)
