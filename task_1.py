import numpy as np
import os


def enumerate_files(directory_name: str) -> list:
    # функция возвращает отсортированный список файлов в директории
    files = sorted(os.listdir(directory_name))
    return files


def load_numpy_array(directory_name: str, file_name: str) -> np.ndarray:
    # функция загружает numpy массивы - матрицы с булевыми значениями (True и False)
    file_path = os.path.join(directory_name, file_name)
    numpy_array = np.load(file_path)
    return numpy_array


def fill_out_layer_with_bricks(layer_matrix: np.ndarray) -> ...:
    pass


def main():
    directory = "data"
    details = ((2, 2), (2, 1), (1, 2), (1, 1))

    for file in enumerate_files(directory):
        model_matrix = load_numpy_array(directory, file)  # воксельная матрица модели
        for layer_matrix in model_matrix:
            fill_out_layer_with_bricks(layer_matrix)


if __name__ == "__main__":
    main()
