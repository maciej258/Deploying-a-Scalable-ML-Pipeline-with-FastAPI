import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics
# TODO: implement the first test. Change the function name and input as needed

def test_train_model():
    """    
    Test to ensure that the train_model function returns a RandomForestClassifier model.
    """
    # sample data for testing
    X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y_train = np.array([0, 1, 0])
    
    # model training
    model = train_model(X_train, y_train)

    # assertion to check if the returned model is of correct type
    assert isinstance(model, RandomForestClassifier), \
        "Model is not a RandomForestClassifier"


# TODO: implement the second test. Change the function name and input as needed
def test_interence():
    """
    test to ensure that the inference function returns predictions of correct length.
    """
    # Your code here
    #sample data for testing
    X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y_train = np.array([0, 1, 0])    
    model = train_model(X_train, y_train)
    
    # sample test data
    X_test = np.array([[2, 3, 4], [5, 6, 7]])

    predictions = inference(model, X_test)
    assert len(predictions) == X_test.shape[0], \
        "Number of predictions does not match number of samples"
    


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test to ensure that the compute_model_metrics function returns precision, recall, and fbeta scores within valid ranges between 0 and 1.
    """
    # Your code here
    # sample true and predicted labels
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    # compute metrics
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    assert 0 <= precision <= 1, "Precision is out of bounds"
    assert 0 <= recall <= 1, "Recall is out of bounds"
    assert 0 <= fbeta <= 1, "F-beta score is out of bounds"         
    
