
from src import make_data, build_features, train_model, predict_model

def main():
    # Fetch data
    make_data.fetch_all_data()

    # Build features
    build_features.build_all_features()

    # Train or load a model

    # Make predictions
    
    # Measure accuracy
    # print(predictions)

if __name__ == '__main__':
    main()
