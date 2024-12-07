import numpy as np
import os
import matplotlib.pyplot as plt
import json
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
# функция визуализации (3 задание)
def visualize_layer(layer_matrix: np.ndarray, output_path: str, layer_index: int):
    plt.figure(figsize=(6, 6))
    plt.imshow(layer_matrix, cmap="gray", interpolation="nearest")
    plt.title(f"Layer {layer_index}")
    plt.axis("off")
    plt.savefig(output_path)
    plt.close()

def save_json(data: dict, output_path: str):
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

def main():
    directory = "C:\\Users\\Ivan\\Desktop\\data"
    output_directory = "C:\\Users\\Ivan\\Desktop\\data\\output"  #путь до изображений-визуализации слоев
    details = [(2, 2), (2, 1), (1, 2), (1, 1)]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file in enumerate_files(directory):
        if file.endswith(".npy"):
            model_matrix = load_numpy_array(directory, file)
            file_output_dir = os.path.join(output_directory, file.split(".")[0])

            if not os.path.exists(file_output_dir):
                os.makedirs(file_output_dir)

            print(f"Processing file: {file}")
            layer_stats = {}

            for layer_index, layer_matrix in enumerate(model_matrix):

                layer_output_path = os.path.join(file_output_dir, f"layer_{layer_index}.png")
                visualize_layer(layer_matrix, layer_output_path, layer_index)


                block_counts = fill_out_layer_with_bricks(layer_matrix.copy(), details)
                layer_stats[f"Layer {layer_index}"] = block_counts


            json_output_path = os.path.join(file_output_dir, "block_counts.json")
            save_json(layer_stats, json_output_path)

            print(f"Finished processing {file}. Results saved in {file_output_dir}")

if __name__ == "__main__":
    main()
