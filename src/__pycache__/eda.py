# src/eda.py
import pandas as pd

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

HEADERS = [
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration",
    "num_doors", "body_style", "drive_wheels", "engine_location",
    "wheel_base", "length", "width", "height", "curb_weight",
    "engine_type", "num_cylinders", "engine_size", "fuel_system",
    "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
    "city_mpg", "highway_mpg", "price"
]

NUMERIC_COLS = ["normalized_losses", "bore", "stroke", "horsepower", "peak_rpm", "price"]

FEATURES = [
    "normalized_losses", "wheel_base", "engine_size", "bore", "stroke",
    "compression_ratio", "horsepower", "peak_rpm"
]


def load_dataset(url: str = DATA_URL) -> pd.DataFrame:
    df = pd.read_csv(url, header=None)
    df.columns = HEADERS
    return df

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col].fillna(df[col].mean(), inplace=True)
    return df


def get_features() -> list:
    return FEATURES