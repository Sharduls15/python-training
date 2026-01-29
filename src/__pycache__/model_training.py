# src/model_training.py
import numpy as np
import time


def train_test_split_numpy(X, y, test_size=0.25, random_state=5):
    """
    Simple numpy-only train-test split.
    """
    rng = np.random.default_rng(random_state)
    n = len(X)
    indices = np.arange(n)
    rng.shuffle(indices)

    test_n = int(n * test_size)
    test_idx = indices[:test_n]
    train_idx = indices[test_n:]

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


class LinearRegressionNumpy:
    """
    Ordinary Least Squares Linear Regression using NumPy least squares.
    Model: y = b0 + b1*x1 + ... + bk*xk
    """
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).reshape(-1, 1)

        # Add bias column (ones) for intercept
        X_bias = np.c_[np.ones((X.shape[0], 1)), X]

    # Solve least squares: minimize ||Xb - y||
        beta, *_ = np.linalg.lstsq(X_bias, y, rcond=None)

    # ✅ Extract true Python scalars
        self.intercept_ = beta[0, 0].item()          # or float(beta[0,0])
        self.coef_ = beta[1:, 0]                      # shape (k,)
        return self

    def predict(self, X):
        X = np.asarray(X, dtype=float)
        return self.intercept_ + X.dot(self.coef_)


def train_linear_regression(df, features, target_col="price", test_size=0.25, random_state=5):
    """
    Trains a NumPy-only linear regression model and returns it.
    """
    X = df[features].to_numpy(dtype=float)
    y = df[target_col].to_numpy(dtype=float)

    X_train, X_test, y_train, y_test = train_test_split_numpy(
        X, y, test_size=test_size, random_state=random_state
    )

    model = LinearRegressionNumpy().fit(X_train, y_train)
    return model


def predict_car_price(model, normalized_losses, wheel_base, engine_size, bore, stroke,
                      compression_ratio, horsepower, peak_rpm, delay_sec=1.5):
    """
    Predicts car price with simulated delay (same as your original behavior).
    """
    time.sleep(delay_sec)

    input_data = np.array(
        [[normalized_losses, wheel_base, engine_size, bore, stroke,
          compression_ratio, horsepower, peak_rpm]],
        dtype=float
    )

    prediction = model.predict(input_data)
    return round(float(prediction[0]), 2)
