


def main():
    pixel1 = pixel(5, 6)
    pixel1._red = 250
    pixel1.print_pixel_info()
    pixel1.grey_scale()
    pixel1.print_pixel_info()


class pixel():

    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        self._red = 0
        self._blue = 0
        self._green = 0
    
    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def grey_scale(self):
        grey = int((self._red + self._blue + self._green) / 3)
        self._red = grey
        self._blue = grey
        self._green = grey

    def print_pixel_info(self):
        if (self._red == 0 and self._green == 0 and self._blue > 50):
            print("X: {0}, Y: {1}, Color: ({2}, {3}, {4}) Blue".format( self._x, self._y, self._red, self._green, self._blue))
        elif (self._green == 0 and self._blue == 0 and self._red > 50):
            print("X: {0}, Y: {1}, Color: ({2}, {3}, {4}) Red".format( self._x, self._y, self._red, self._green, self._blue))
        elif(self._red == 0 and self._blue == 0 and self._green > 50):
            print("X: {0}, Y: {1}, Color: ({2}, {3}, {4}) Green".format( self._x, self._y, self._red, self._green, self._blue))
        else:
            print("X: {0}, Y: {1}, Color: ({2}, {3}, {4})".format( self._x, self._y, self._red, self._green, self._blue))
    


    

    




if __name__ == "__main__":
    main()