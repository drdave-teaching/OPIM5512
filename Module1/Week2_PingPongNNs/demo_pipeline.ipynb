"""
A02 — Buddy Collab Pipeline
Decision Tree Regression on California Housing Dataset

Students run:
    python src/pipeline.py load
    python src/pipeline.py clean
    python src/pipeline.py model
    python src/pipeline.py evaluate
"""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------
BASE = Path(__file__).resolve().parents[1]   # points to A02-collab/
DATA = BASE / "data"
FIGS = BASE / "figs"


# ---------------------------------------------------------
# Step 1: LOAD
# ---------------------------------------------------------
def cmd_load(args):
    """Load the instructor-provided dataset and create raw.csv."""
    raw_src = DATA / "raw_ca_housing.csv"
    raw_dst = DATA / "raw.csv"

    df = pd.read_csv(raw_src)
    df.to_csv(raw_dst, index=False)

    print(f"[LOAD] Loaded {raw_src.name} → saved {raw_dst.name} (shape={df.shape})")


# ---------------------------------------------------------
# Step 2: CLEAN
# ---------------------------------------------------------
def cmd_clean(args):
    """Basic cleaning: drop rows with missing values."""
    src = DATA / "raw.csv"
    dst = DATA / "clean.csv"

    df = pd.read_csv(src)

    # Simple cleaning: drop NA values
    before = df.shape[0]
    df = df.dropna()
    after = df.shape[0]

    df.to_csv(dst, index=False)
    print(f"[CLEAN] Dropped {before - after} rows with NA. Saved clean.csv (shape={df.shape})")


# ---------------------------------------------------------
# Step 3: MODEL
# ---------------------------------------------------------
def cmd_model(args):
    """Train a Decision Tree Regression model and save metrics + plots."""
    clean_path = DATA / "clean.csv"
    metrics_path = DATA / "metrics.json"
    preds_path = DATA / "preds_test.csv"

    FIGS.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(clean_path)

    # Choose the target column
    target_col = "median_house_value"

    # Features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Save metrics
    with open(metrics_path, "w") as f:
        json.dump({"r2": r2, "rmse": rmse}, f, indent=2)

    # Save predictions
    preds_df = pd.DataFrame({"y_true": y_test, "y_pred": y_pred})
    preds_df.to_csv(preds_path, index=False)

    # Residuals plot
    residuals = y_test - y_pred
    plt.figure(figsize=(6, 4))
    plt.scatter(y_pred, residuals, alpha=0.4)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Predicted")
    plt.ylabel("Residual")
    plt.title("Residuals vs Predicted")
    plt.tight_layout()
    plt.savefig(FIGS / "residuals.png")
    plt.close()

    # Feature importance bar chart
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values()

    plt.figure(figsize=(6, 4))
    importances.plot(kind="barh")
    plt.title("Feature Importance (Decision Tree)")
    plt.tight_layout()
    plt.savefig(FIGS / "feat_importance.png")
    plt.close()

    print(f"[MODEL] Saved metrics.json, preds_test.csv, residuals.png, feat_importance.png")


# ---------------------------------------------------------
# Step 4: EVALUATE
# ---------------------------------------------------------
def cmd_evaluate(args):
    """Create predicted vs. actual plot and print stored metrics."""
    preds_path = DATA / "preds_test.csv"
    metrics_path = DATA / "metrics.json"

    df = pd.read_csv(preds_path)

    # Plot predicted vs actual
    plt.figure(figsize=(6, 4))
    plt.scatter(df["y_true"], df["y_pred"], alpha=0.4)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Predicted vs Actual")
    plt.tight_layout()
    plt.savefig(FIGS / "pred_vs_actual.png")
    plt.close()

    # Print metrics to console
    with open(metrics_path) as f:
        metrics = json.load(f)

    print(
        f"[EVALUATE] R² = {metrics['r2']:.3f}, "
        f"RMSE = {metrics['rmse']:.1f}. "
        f"Saved pred_vs_actual.png."
    )


# ---------------------------------------------------------
# Parser
# ---------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="A02 ML Pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # load
    p = subparsers.add_parser("load", help="Load raw housing data → raw.csv")
    p.set_defaults(func=cmd_load)

    # clean
    p = subparsers.add_parser("clean", help="Clean raw.csv → clean.csv")
    p.set_defaults(func=cmd_clean)

    # model
    p = subparsers.add_parser("model", help="Train model + save metrics, preds, figs")
    p.set_defaults(func=cmd_model)

    # evaluate
    p = subparsers.add_parser("evaluate", help="Plot predicted vs actual + print metrics")
    p.set_defaults(func=cmd_evaluate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
