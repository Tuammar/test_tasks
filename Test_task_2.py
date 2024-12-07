import numpy as np
import os
from collections import defaultdict

def enumerate_files(directory_name: str) -> list:
    files = sorted(os.listdir(directory_name))
    return files

def load_numpy_array(directory_name: str, file_name: str) -> np.ndarray:
    file_path = os.path.join(directory_name, file_name)
    numpy_array = np.load(file_path)
    return numpy_array

def fill_out_layer_with_bricks(layer_matrix: np.ndarray, details: list) -> dict:
    placed_blocks = defaultdict(int)

    def place_test(matrix, start_row, start_col, block_height, block_width):
        if start_row + block_height > matrix.shape[0] or start_col + block_width > matrix.shape[1]:
            return False
        for i in range(start_row, start_row + block_height):
            for j in range(start_col, start_col + block_width):
                if not matrix[i, j]:
                    return False
        return True

    def place(matrix, start_row, start_col, block_height, block_width):
        for i in range(start_row, start_row + block_height):
            for j in range(start_col, start_col + block_width):
                matrix[i, j] = False


    for row in range(layer_matrix.shape[0]):
        for col in range(layer_matrix.shape[1]):
            if layer_matrix[row, col]:
                for block_height, block_width in details:
                    if place_test(layer_matrix, row, col, block_height, block_width):
                        place(layer_matrix, row, col, block_height, block_width)
                        block_size = f"{block_height}x{block_width}"
                        placed_blocks[block_size] += 1
                        break

    return dict(placed_blocks)

def main():
    directory = "C:\\Users\\Ivan\\Desktop\\data"
    details = [(2, 2), (2, 1), (1, 2), (1, 1)]

# решение второй задачи
    for file in enumerate_files(directory):
        if file.endswith(".npy"):
            model_matrix = load_numpy_array(directory, file)
            print(f"Processing file: {file}")
            layer_stats = []


            for layer_index, layer_matrix in enumerate(model_matrix):
                print(f"  Processing layer {layer_index}")
                block_counts = fill_out_layer_with_bricks(layer_matrix.copy(), details)
                layer_stats.append(block_counts)
                print(f"    Block counts: {block_counts}")


            print(f"Summary for file {file}:")
            for i, stats in enumerate(layer_stats):
                print(f"  Layer {i}: {stats}")

if __name__ == "__main__":
    main()
