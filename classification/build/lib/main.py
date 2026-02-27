#!/usr/bin/env python3
"""
Simple conformal prediction for classification from scratch.

Conformal prediction provides prediction sets with guaranteed coverage.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


class ConformalClassifier:
    """Simple conformal predictor for classification."""

    def __init__(self, base_classifier, alpha: float = 0.1):
        """
        Initialize conformal classifier.

        Args:
            base_classifier: Any sklearn-like classifier with predict_proba
            alpha: Target miscoverage rate (1 - coverage level)
        """
        self.base_classifier = base_classifier
        self.alpha = alpha
        self.classes_: np.ndarray | None = None
        self.quantile: float | None = None

    def fit(self, X_train, y_train, X_cal, y_cal):
        """
        Fit the conformal predictor.

        Args:
            X_train: Training features
            y_train: Training labels
            X_cal: Calibration features
            y_cal: Calibration labels
        """
        # Train base classifier
        self.base_classifier.fit(X_train, y_train)
        self.classes_ = self.base_classifier.classes_

        # Get predicted probabilities on calibration set
        probas = self.base_classifier.predict_proba(X_cal)

        # Calculate nonconformity scores: 1 - probability of true class
        n_cal = len(y_cal)
        scores = np.zeros(n_cal)
        for i, (true_label, probs) in enumerate(zip(y_cal, probas, strict=True)):
            true_idx = np.where(self.classes_ == true_label)[0][0]
            scores[i] = 1 - probs[true_idx]

        # Compute quantile threshold (conformal quantile formula)
        n_cal_plus_1 = n_cal + 1
        q_level = np.ceil((n_cal + 1) * (1 - self.alpha)) / n_cal_plus_1
        self.quantile = np.quantile(scores, q_level, method="higher")

    def predict_set(self, X):
        """
        Return prediction sets for new samples.

        Args:
            X: New samples

        Returns:
            List of prediction sets (one per sample)
        """
        assert self.quantile is not None, "Must call fit() before predict_set()"
        assert self.classes_ is not None, "Must call fit() before predict_set()"
        probas = self.base_classifier.predict_proba(X)
        prediction_sets = []

        for probs in probas:
            # Include classes where probability is high enough
            in_set = probs >= (1 - self.quantile)
            prediction_set = self.classes_[in_set]
            prediction_sets.append(prediction_set)

        return prediction_sets

    def predict(self, X):
        """Return single predictions (for compatibility with sklearn)."""
        return self.base_classifier.predict(X)

    def coverage(self, X, y):
        """Calculate empirical coverage on a test set."""
        prediction_sets = self.predict_set(X)
        covered = 0
        for true_label, pred_set in zip(y, prediction_sets, strict=True):
            if true_label in pred_set:
                covered += 1
        return covered / len(y)


def main():
    """Demo conformal prediction on synthetic data."""
    np.random.seed(42)

    # Generate synthetic classification data
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_classes=3,
        n_informative=15,
        random_state=42,
    )

    # Split into proper training, calibration, and test sets
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.6, random_state=42
    )
    X_cal, X_test, y_cal, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )

    print(f"Train size: {len(X_train)}")
    print(f"Calibration size: {len(X_cal)}")
    print(f"Test size: {len(X_test)}")

    # Create conformal predictor with 90% coverage (alpha=0.1)
    conformal = ConformalClassifier(
        base_classifier=RandomForestClassifier(n_estimators=100, random_state=42),
        alpha=0.1,
    )

    # Fit conformal predictor
    conformal.fit(X_train, y_train, X_cal, y_cal)
    print(f"\nQuantile threshold: {conformal.quantile:.4f}")

    # Evaluate on test set
    coverage = conformal.coverage(X_test, y_test)
    print(f"Target coverage: {1 - conformal.alpha:.2%}")
    print(f"Actual coverage: {coverage:.2%}")

    # Show some example prediction sets
    print("\nExample prediction sets for 5 test samples:")
    for i in range(5):
        pred_set = conformal.predict_set(X_test[i : i + 1])[0]
        print(f"  True label: {y_test[i]}, Prediction set: {pred_set}")


if __name__ == "__main__":
    main()
