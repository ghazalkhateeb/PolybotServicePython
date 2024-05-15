from pathlib import Path
import random
from matplotlib.image import imread, imsave


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def blur(self, blur_level=16):
        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2
        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)
        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))
            self.data[i] = res

    def rotate(self):
        width = len(self.data[0])
        for i in range(width // 2):
            for j in range(i, width - i - 1):
                tmp = self.data[i][j]
                self.data[i][j] = self.data[width - 1 - j][i]
                self.data[width - 1 - j][i] = self.data[width - 1 - i][width - 1 - j]
                self.data[width - 1 - i][width - 1 - j] = self.data[j][width - 1 - i]
                self.data[j][width - 1 - i] = tmp

    def salt_n_pepper(self):
        height = len(self.data)
        width = len(self.data[0])
        #Iterate over each row and pixel of the image.
        for i in range(height):
            for j in range(width):
                #Randomly generate a number between 0 and 1.
                random_value = random.random()
                #Check if the random number is less than 0.2 for salt.
                if random_value < 0.2:
                    self.data[i][j] = 255
                #Check if the random number is greater than 0.8 for pepper.
                elif random_value > 0.8:
                    self.data[i][j] = 0
                #Otherwise, keep the original pixel value.


    def concat(self, other_img, direction='horizontal'):
        #Check the dimensions of both images to ensure they are compatible for concatenation.
        if len(self.data) != len(other_img.data):
            raise RuntimeError("Images have different heights and cannot be concatenated horizontally.")
        #Create a new list to store concatenated image data.
        concatenated_image_data = []
        if direction == 'horizontal':
            for row, other_row in zip(self.data, other_img.data):
                #Combine the rows pixel.
                concatenated_row_data = row + other_row
                #Append the concatenated row.
                concatenated_image_data.append(concatenated_row_data)
            #Update the self.data attribute with the concatenated image data.
            self.data = concatenated_image_data



    def segment(self):
        height = len(self.data)
        width = len(self.data[0])
        #Iterate over each row and pixel of the image.
        for i in range(height):
            for j in range(width):
                #Check if the intensity of the pixel is greater than 100.
                if self.data[i][j] > 100:
                    #Replace pixels with intensity greater than 100 with white (255).
                    self.data[i][j] = 255
                else:
                    #Replace pixels with intensity less than or equal to 100 with black (0).
                    self.data[i][j] = 0



