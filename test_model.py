import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    """
    Test 2 (na maksymalną ocenę 5): Sprawdza, czy długość listy predykcji jest większa od 0 
    i czy odpowiada przewidywanej liczbie próbek testowych.
    """
    preds, y_test = train_and_predict()
    assert len(preds) > 0, "Predictions list should not be empty."
    assert len(preds) == len(y_test), "Number of predictions must match number of test samples."

def test_predictions_value_range():
    """
    Test 3 (na maksymalną ocenę 5): Sprawdza, czy wartości w predykcjach mieszczą się w 
    spodziewanym zakresie: Dla zbioru Iris mamy 3 klasy (0, 1, 2).
    """
    preds, _ = train_and_predict()
    valid_classes = {0, 1, 2}
    assert set(preds).issubset(valid_classes), f"Predictions must be in {valid_classes}, got {set(preds)}."

def test_model_accuracy():
    """
    Test 4 (na maksymalną ocenę 5): Sprawdza, czy model osiąga co najmniej 70% dokładności.
    """
    acc = get_accuracy()
    assert acc >= 0.7, f"Model accuracy should be >= 0.7, got {acc:.2f}."
