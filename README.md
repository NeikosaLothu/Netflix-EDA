# 📊 Netflix EDA Project

An Exploratory Data Analysis (EDA) project on the Netflix titles dataset using Python.

## 📁 Project Structure

```
netflix-eda-project/
│
├── data/
│   └── netflix_titles.csv         # The main dataset
│
├── analysis/
│   ├── 1_data_loading.py          # Load and inspect the dataset
│   ├── 2_data_cleaning.py         # Handle missing values, formatting
│   ├── 3_data_visualization.py    # Plotting trends, distributions
│   ├── 4_content_analysis.py      # Genre, country, and rating analysis
│   └── 5_time_trend_analysis.py   # Year-wise trend of content added
│
├── README.md                      # Project description and instructions
└── requirements.txt               # Python dependencies
```

## 📦 Setup Instructions

1. **Clone or download this repository**
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```
3. **Run the analysis scripts** from the `analysis/` folder in order:
```bash
python 1_data_loading.py
python 2_data_cleaning.py
python 3_data_visualization.py
python 4_content_analysis.py
python 5_time_trend_analysis.py
```

## 📊 Analysis Breakdown

- **Data Loading**: Basic inspection of dataset structure and preview.
- **Data Cleaning**: Handles missing values and removes duplicates.
- **Visualization**: Bar plots for type distribution (Movie/TV Show).
- **Content Analysis**: Insights into most common genres, ratings, and countries.
- **Time Trend Analysis**: Trends in content added by year.

## 🛠️ Dependencies

- `pandas`
- `matplotlib`

## 👨‍💻 Author

Project created by **Neikosa Lothu**.

Feel free to use or extend this project with attribution.

---

Netflix data source courtesy of [Kaggle Datasets](https://www.kaggle.com/shivamb/netflix-shows).