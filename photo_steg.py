#David Shapiro
#May 2024
#Image Steganography using Least Significant Bit
from PIL import Image

class PhotoSteganography:

    #Initialize Steg
    def __init__(self, img):
        self.CHAR_LENGTH = 7
        self.NUM_COLOR_CHANNELS = 3
        self.image = Image.open(img)
        self.image = self.image.convert("RGB")
        self.pixel_map = self.image.load()
        self.width, self.height = self.image.size

    #Displays image
    def show_image(self):
        self.image.show()

    #Ensures there is space for message
    def within_size(self, message_length):
        num_color_channels = self.width * self.height * 3
        if num_color_channels > message_length:
            return True
        else:
            return False
        
    #Convert string to binary
    def get_binary_from_message(self, message):
        binary_message = ""
        for letter in message:
            binary = format(ord(letter), "07b")
            binary_message += binary
        
        #Finish out last pixel
        remainder = len(binary_message) % self.NUM_COLOR_CHANNELS
        if remainder != 0:
            binary_message += (self.NUM_COLOR_CHANNELS - remainder) * "0"

        #Mark end of message
        binary_message += 9 * "0"
        return list(binary_message)

    #Hides a message in image
    def encode(self, message, file_name):

        #Get binary string
        binary_list = self.get_binary_from_message(message)

        if not self.within_size(len(binary_list)):
            return False
        
        #Hide binary in each pixel
        for col in range(self.width):
            for row in range(self.height):
                r, g, b = self.image.getpixel((col, row))
                if len(binary_list) != 0:
                    new_r = self.update_bit(r, binary_list.pop(0))
                    new_g = self.update_bit(g, binary_list.pop(0))
                    new_b = self.update_bit(b, binary_list.pop(0)) 
                    new_pixel = (new_r, new_g, new_b)
                    self.pixel_map[col, row] = new_pixel
                else:
                    break
        self.image.save(file_name)
        return True

    #Adjust least significant bit
    def update_bit(self, color, bit):
        new_color = color
        if color & 1 == 0 and int(bit) & 1 == 1:
            new_color = color + 1
        elif color & 1 == 1 and int(bit) & 1 == 0:
            new_color = color - 1
        return new_color

    #Decode a message from an image
    def decode(self):
        message = ""
        num_c = self.CHAR_LENGTH

        #Load binary from image
        binary_string = self.get_binary_from_image()
        remainder = len(binary_string) % num_c

        #Padding
        if remainder != 0:
            binary_string += (num_c - remainder) * "0"
        
        #Convert to string
        for i in range(0, len(binary_string) // self.CHAR_LENGTH):
            binary = binary_string[i*num_c:i*num_c+num_c]
            #End of message
            if binary == "0000000":
                return message
            letter = chr(int(binary, 2))
            message += letter
        return message
    
    #Gets binary code from image
    def get_binary_from_image(self):
        binary_string = ""
        zero_count = 0
        for col in range(self.width):
            for row in range(self.height):
                pixel = self.image.getpixel((col, row))
                for color in pixel:
                    least_sig = color & 1
                    #Checking for end
                    if least_sig == 0:
                        zero_count += 1
                    else:
                        zero_count = 0
                    binary_string += str(least_sig)
                    if zero_count == 9:
                        return binary_string