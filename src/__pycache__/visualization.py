import matplotlib.pyplot as plt
import seaborn as sns


def price_by_make(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x='make', y='price', palette='Oranges', ax=ax)
    ax.set_title("Car Make vs Price")
    plt.xticks(rotation=45)
    return fig


def price_by_drive(df):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x='drive_wheels', y='price', palette='Oranges', ax=ax)
    ax.set_title("Drive Wheels vs Price")
    return fig


def price_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['price'], bins=30, kde=True, color="orange", ax=ax)
    ax.set_title("Car Price Distribution")
    return fig


def correlation_heatmap(df, features):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df[features + ["price"]].corr(), annot=True, cmap="Oranges", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    return fig


def fueltype_price_box(df):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x='fuel_type', y='price', palette='Oranges', ax=ax)
    ax.set_title("Fuel Type vs Price")
    return fig


def make_average_price(df):
    avg_price = df.groupby("make")["price"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(x=avg_price.values, y=avg_price.index, palette="Oranges", ax=ax)
    ax.set_title("Top 10 Car Makes by Average Price")
    return fig


def horsepower_vs_price(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='horsepower', y='price', hue='fuel_type', palette='Oranges', ax=ax)
    ax.set_title("Horsepower vs Price")
    return fig


def engine_size_vs_price(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='engine_size', y='price', hue='make',
                    palette='Oranges', legend=False, ax=ax)
    ax.set_title("Engine Size vs Price")
    return fig


def body_style_vs_price(df):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x='body_style', y='price', palette='Oranges', ax=ax)
    ax.set_title("Body Style vs Price")
    return fig


def get_visualization(df, features, chart_type: str):
    """Returns the requested visualization figure."""
    if chart_type == "Price Distribution":
        return price_distribution(df)
    elif chart_type == "Correlation Heatmap":
        return correlation_heatmap(df, features)
    elif chart_type == "Fuel Type vs Price":
        return fueltype_price_box(df)
    elif chart_type == "Top 10 Car Makes by Avg Price":
        return make_average_price(df)
    elif chart_type == "Horsepower vs Price":
        return horsepower_vs_price(df)
    elif chart_type == "Engine Size vs Price":
        return engine_size_vs_price(df)
    elif chart_type == "Body Style vs Price":
        return body_style_vs_price(df)
    elif chart_type == "Drive Type vs Price":
        return price_by_drive(df)
    elif chart_type == "Make vs Price":
        return price_by_make(df)

    # default fallback
    return price_distribution(df)