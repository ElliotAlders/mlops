# Import your individual scripts
import data_creation
import data_preprocessing
import model_preparation
import model_testing

# Orchestrate the execution of your scripts
if __name__ == "__main__":
    data_creation.create_data()
    data_preprocessing.preprocess_data()
    model_preparation.prepare_model()
    model_testing.test_model()
