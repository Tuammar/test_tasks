import numpy as np
import os


def enumerate_files(directory_name: str) -> list:
    files = sorted(os.listdir(directory_name))
    return files


def load_numpy_array(directory_name: str, file_name: str) -> np.ndarray:
    file_path = os.path.join(directory_name, file_name)
    numpy_array = np.load(file_path)
    return numpy_array

# решение первой задачи
def fill_out_layer_with_bricks(layer_matrix: np.ndarray, details: list) -> list:
    placed_blocks = []

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


    print("Layer matrix before placement:")
    print(layer_matrix)

    for row in range(layer_matrix.shape[0]):
        for col in range(layer_matrix.shape[1]):
            if layer_matrix[row, col]:
                for block_height, block_width in details:
                    if place_test(layer_matrix, row, col, block_height, block_width):
                        place(layer_matrix, row, col, block_height, block_width)
                        placed_blocks.append((row, col, block_height, block_width))
                        break

    return placed_blocks


def main():
    directory = "C:\\Users\\Ivan\\Desktop\\data"
    details = [(2, 2), (2, 1), (1, 2), (1, 1)]


    for file in enumerate_files(directory):
        if file.endswith(".npy"):
            model_matrix = load_numpy_array(directory, file)
            print(f"Processing file: {file}")


            for layer_index, layer_matrix in enumerate(model_matrix):
                print(f"  Processing layer {layer_index}")
                placed_blocks = fill_out_layer_with_bricks(layer_matrix.copy(), details)
                print(f"    Placed blocks: {placed_blocks}")
                if not placed_blocks:
                    print(f"    No blocks placed on layer {layer_index}")
                else:
                    print(f"    Blocks placed: {len(placed_blocks)}")


if __name__ == "__main__":
    main()
