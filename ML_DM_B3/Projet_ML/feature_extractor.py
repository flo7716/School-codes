import numpy as np
from scipy.linalg import lstsq
from PIL import Image, ImageOps
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import os

def preprocess_image(image_path, output_size=(64, 64)):
    """
    Load, normalize, and resize an image.

    :param image_path: Path to the image file
    :param output_size: Target size (width, height)
    :return: Preprocessed image as a numpy array
    """
    image = Image.open(image_path).convert("L")
    image = ImageOps.invert(image)  # Invert colors for black text on white background
    bbox = image.getbbox()
    image = image.crop(bbox) if bbox else image
    image = image.resize(output_size, Image.Resampling.LANCZOS)
    return np.array(image)

def extract_features(image_array, grid_size=(5, 5)):
    """
    Extract features from an image using Local Line Fitting (LLF).

    :param image_array: Grayscale image as a numpy array
    :param grid_size: Grid dimensions for feature extraction
    :return: Feature vector
    """
    h, w = image_array.shape
    cell_h, cell_w = h // grid_size[0], w // grid_size[1]
    features = []

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            cell = image_array[i * cell_h:(i + 1) * cell_h, j * cell_w:(j + 1) * cell_w]
            black_pixels = np.sum(cell < 128)  # Count black pixels
            density = black_pixels / (cell_h * cell_w)

            y, x = np.where(cell < 128)
            if len(x) > 1:
                A = np.vstack([x, np.ones_like(x)]).T
                slope, _ = lstsq(A, y)[0]
                f2 = (2 * slope) / (1 + slope**2)
                f3 = (1 - slope**2) / (1 + slope**2)
            else:
                f2, f3 = 0, 0

            features.extend([density, f2, f3])

    return np.array(features)

def prepare_dataset(image_dir, grid_size=(5, 5)):
    """
    Prepare dataset from images in a directory.

    :param image_dir: Path to the directory with images
    :param grid_size: Grid dimensions for feature extraction
    :return: Features (X) and labels (y)
    """
    X, y = [], []
    labels = {"b": 0, "h": 1, "k": 2, "g": 3, "j": 4, "f": 5}

    for label, class_id in labels.items():
        class_dir = os.path.join(image_dir, label)
        for file in os.listdir(class_dir):
            image_path = os.path.join(class_dir, file)
            image_array = preprocess_image(image_path)
            features = extract_features(image_array, grid_size=grid_size)
            X.append(features)
            y.append(class_id)

    return np.array(X), np.array(y)

def build_model(input_dim, output_dim):
    """
    Build a neural network for classification.

    :param input_dim: Input feature vector size
    :param output_dim: Number of classes (outputs)
    :return: Compiled Keras model
    """
    model = Sequential([
        Dense(128, activation="relu", input_dim=input_dim),
        Dense(64, activation="relu"),
        Dense(output_dim, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

def main():
    """
    Main function to preprocess data, train a model, and evaluate its performance.
    """
    # Dataset path
    image_dir = "/home/florian-andr/Downloads/projet_ML_Hector_Mathis_Florian/"

    # Prepare dataset
    X, y = prepare_dataset(image_dir)

    # Split dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and train the model
    input_dim = X.shape[1]
    output_dim = len(set(y))
    model = build_model(input_dim, output_dim)

    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

    # Evaluate model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

    # Save the trained model
    model.save("handwriting_recognition_model.h5")

if __name__ == "__main__":
    main()
