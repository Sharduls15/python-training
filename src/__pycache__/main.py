from eda import load_dataset, clean_dataset, get_features
from model_training import train_linear_regression
from gradio_ui import build_app


def main():
    df = load_dataset()
    df = clean_dataset(df)

    features = get_features()
    model = train_linear_regression(df, features)

    app = build_app(df, features, model)
    app.launch(share=True)


if __name__ == "__main__":
    main()