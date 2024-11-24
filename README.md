# Streamlit Dashboard Enhanced

## Overview
This project focuses on creating a Streamlit dashboard to visualize and explore school learning modalities data from the **National Center for Education Statistics (NCES)** for 2021. The dashboard includes interactive visualizations, metrics, and a data table to provide insights into the educational modalities during the 2020-2021 academic year.

## Features
### Pre-existing Features
- **Data Loading and Cleaning**:
  - Loads a dataset from the [HealthData.gov School Learning Modalities 2020-2021](https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data).
  - Cleans the dataset by converting date fields and standardizing zip code formats.
- **Data Metrics**:
  - Displays the number of rows, columns, and unique districts in the dataset.
- **Pivot Table Visualizations**:
  - Generates bar charts showing the number of students in hybrid, in-person, and remote learning modalities over time.
- **Data Table**:
  - Exposes the cleaned dataset for inspection.

### My Additions
- **Interactive Slider**:
  - A date slider allows users to filter data by specific weeks within the dataset range.
  - Filters data dynamically based on the selected week and displays the relevant rows.
- **Dynamic Bar Chart**:
  - Visualizes the total number of students by learning modality (Hybrid, In-Person, Remote) for the selected week.
- **Empty Data Handling**:
  - Displays a fallback message if no data is available for the selected week.

---

### Deployed App
[Streamlit Dashboard URL](https://bookish-space-train-4jgr76qg677vh7qjw-8504.app.github.dev/)
