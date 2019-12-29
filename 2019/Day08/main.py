BLACK_PIXEL = 0
WHITE_PIXEL = 1
TRANSPARENT_PIXEL = 2

class Layer:
    def __init__(self, index: int, data, width: int, height: int):
        self.width = width
        self.height = height
        self.index = index
        self.data = data

    def count_pixels(self, pixel_value: int):
        return sum([ 1 if single_pixel == pixel_value else 0 for single_pixel in self.data ])
    
    def get_pixel_value_at_index(self, index: int):
        return self.data[index]

class Image:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.layers = []
        self.raw_data = [int]

    def load(self, filepath: str):
        file_handle = open(filepath, 'r+')
        file_data = file_handle.readline()
        self.raw_data = [int(single_number) for single_number in file_data]
        chunk_size = self.width * self.height
        file_handle.close()
        layers_raw = [self.raw_data[i * chunk_size:(i + 1) * chunk_size] for i in range((len(self.raw_data) + chunk_size - 1) // chunk_size )]
        for index, value in enumerate(layers_raw):
            layer_instance = Layer(index + 1, value, self.width, self.height)
            self.layers.append(layer_instance)

    def get_all_layers(self):
        return self.layers
    
    def get_layer_by_index(self, index: int):
        return self.layers[index]

    def get_final_pixel_value_at_index(self, index: int):
        pixel_values_at_each_layer = [ layer.get_pixel_value_at_index(index) for layer in self.layers ]
        final_pixel_value = None
        for pixel_in_layer in pixel_values_at_each_layer:
            if pixel_in_layer == BLACK_PIXEL or pixel_in_layer == WHITE_PIXEL:
                final_pixel_value = pixel_in_layer
                break
        if final_pixel_value is None:
            final_pixel_value = pixel_values_at_each_layer[len(pixel_values_at_each_layer) - 1]
        return final_pixel_value

    def render_image(self):
        final_image = [ self.get_final_pixel_value_at_index(index) for index in range(0, self.width * self.height) ]
        for row in range(0, self.height):
            for column in range(0, self.width):
                print('1' if final_image[(row * self.width) + column] == WHITE_PIXEL else ' ', end='')
            print()

def main():
    password_image = Image(25, 6)
    password_image.load('input.txt')
    # Part 1:
    layers_count_of_0_pixels = [ layer_data.count_pixels(0) for layer_data in password_image.get_all_layers() ]
    lowest_amount = min(layers_count_of_0_pixels)
    layer_index = layers_count_of_0_pixels.index(lowest_amount)
    layer_data = password_image.get_layer_by_index(layer_index)
    print('Part 1:', layer_data.count_pixels(1) * layer_data.count_pixels(2))
    # Part 2:
    print('Part 2:')
    password_image.render_image()

main()