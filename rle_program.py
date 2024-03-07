# Import the ConsoleGfx class to use methods and variables
from console_gfx import ConsoleGfx


# Returns a hex string based on an array with numbers
def to_hex_string(data):
    hex_string = ''
    # Adds hexadecimal string counterpart of every int in the list data to a growing string(hex_string)
    for num in data:
        if int(num) <= 9:
            hex_string += str(num)
        elif int(num) == 10:
            hex_string += 'a'
        elif int(num) == 11:
            hex_string += 'b'
        elif int(num) == 12:
            hex_string += 'c'
        elif int(num) == 13:
            hex_string += 'd'
        elif int(num) == 14:
            hex_string += 'e'
        elif int(num) == 15:
            hex_string += 'f'
    return hex_string


# Counts how many continuous runs of data are in the data.
def count_runs(flat_data):
    num_runs = 0
    temp = flat_data[0]
    num_repeated = 0
    for num in range(1, len(flat_data)):
        if flat_data[num] != temp:
            num_runs += 1
            temp = flat_data[num]
        # Else statement which checks if a num is repeated more than 15x
        else:
            num_repeated += 1
            # If num is repeated more than 15x, then num_runs increases by 1 and int repeated resets to 0
            if num_repeated > 15:
                num_runs += 1
                num_repeated = 0

    num_runs += 1
    return num_runs


# This method encodes flat_data by returning an array which returns count of a value, and it's value
def encode_rle(flat_data):
    arr = []
    count = 1
    temp = flat_data[0]
    for i in range(1, len(flat_data)):
        if flat_data[i] == temp:
            count += 1
            # If data is repeated more than 14x then data value is appended and count 15 is appended
            if count > 14:
                arr.append(count)
                arr.append(temp)
                temp = flat_data[i]
                count = 0
        # Appends the count of data, and it's value to list arr
        else:
            arr.append(count)
            arr.append(temp)
            temp = flat_data[i]
            count = 1
    arr.append(count)
    arr.append(temp)
    return list(arr)


# Gets decoded length by checking the even indexes in rle_data(which contains the length) and adds to growing sum
def get_decoded_length(rle_data):
    length = 0
    for i in range(0, len(rle_data), 2):
        length += rle_data[i]
    return length


# This method decodes list rle_data into it's actual form
def decode_rle(rle_data):
    arr = []
    # Checks even indexes for the data value to append
    # Checks odds indexes to see how many times to append data
    for i in range(0, len(rle_data) - 1, 2):
        for j in range(rle_data[i]):
            arr.append(rle_data[i + 1])
    return arr


# This method decodes a hexadecimal string and returns its int counterparts
def string_to_data(data_string):
    arr = []
    for i in data_string:
        if i == 'a':
            arr.append(10)
        elif i == 'b':
            arr.append(11)
        elif i == 'c':
            arr.append(12)
        elif i == 'd':
            arr.append(13)
        elif i == 'e':
            arr.append(14)
        elif i == 'f':
            arr.append(15)
        else:
            arr.append(int(i))
    # Returns arr with the converted data from the hex_string
    return arr


# Returns a string representing the rle_data(length and value)
def to_rle_string(rle_data):
    rle = ''
    for num in range(0, len(rle_data) - 1, 2):
        rle += str(rle_data[num])
        value = str(rle_data[num + 1])
        if value == '15':
            rle += 'f'
        elif value == '14':
            rle += 'e'
        elif value == '13':
            rle += 'd'
        elif value == '12':
            rle += 'c'
        elif value == '11':
            rle += 'b'
        elif value == '10':
            rle += 'a'
        else:
            rle += value
            # Prevents colon at the end of a string
        if num != len(rle_data) - 2:
            rle += ':'
    return rle


# Turns a hex string into RLE byte-data
def string_to_rle(rle_string):
    data_arr = []
    # Gets rid of colons in the string
    temp = rle_string.split(':')
    for data in temp:
        # Test case for data length and value have length of 3
        if len(data) == 3:
            data_arr.append(data[0: 2])
            if data[2] == 'f':
                data_arr.append('15')
            elif data[2] == 'e':
                data_arr.append('14')
            elif data[2] == 'd':
                data_arr.append('13')
            elif data[2] == 'c':
                data_arr.append('12')
            elif data[2] == 'b':
                data_arr.append('11')
            elif data[2] == 'a':
                data_arr.append('10')
            else:
                data_arr.append(data[2])
        # Test case for data length and value have length of 2
        else:
            data_arr.append(data[0])
            if data[1] == 'f':
                data_arr.append('15')
            elif data[1] == 'e':
                data_arr.append('14')
            elif data[1] == 'd':
                data_arr.append('13')
            elif data[1] == 'c':
                data_arr.append('12')
            elif data[1] == 'b':
                data_arr.append('11')
            elif data[1] == 'a':
                data_arr.append('10')
            else:
                data_arr.append(data[1])
    # Returns the list with RLE byte values
    return data_arr


# Welcome user and display Spectrum image. Declare global variables
if __name__ == '__main__':
    Exit = False
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print()
    image_data = None
    current_data = None
    # While loop which shows menu options iterates until the user inputs 0
    while not Exit:
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")
        user_input = input("Select a Menu Option: ")
        # Conditionals to be executed based on user_input
        # Loads up data from a file
        if user_input == '1':
            file_name = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(file_name)
            current_data = image_data
            # Loads data from test image
        elif user_input == '2':
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")
            current_data = image_data
            # Gets RLE string to be decoded
        elif user_input == '3':
            current_data = input("Enter an RLE string to be decoded: ")
            # Gets hex string holding RLE Data
        elif user_input == '4':
            current_data = input("Enter the hex string holding RLE data: ")
            # Gets hex string holding Flat Data
        elif user_input == '5':
            current_data = input("Enter the hex string holding flat data: ")
            # Displays the image based on current data
        elif user_input == '6':
            print("Displaying image...")
            ConsoleGfx.display_image(current_data)
            # RLE Representation of current_data
        elif user_input == '7':
            current_data = string_to_data(current_data)
            temp = ''
            for i in range(0, len(current_data) - 1, 2):
                temp = temp + str(current_data[i]) + str(current_data[i + 1])
                if i != len(current_data) - 2:
                    temp += ':'
            current_data = temp
            print("RLE representation:", current_data)
            # RLE Hex-decimal representation of current_data
        elif user_input == '8':
            print("RLE hex values: ", to_hex_string(string_to_rle(current_data)))
            current_data = to_hex_string(string_to_rle(current_data))
            # Displays the raw flat data in hexadecimal
        elif user_input == '9':
            string_temp = string_to_rle(current_data)
            int_temp = []
            for i in string_temp:
                int_temp.append(int(i))
            int_temp = decode_rle(int_temp)
            current_data = ''
            for j in int_temp:
                current_data += str(j)
            print("Flat hex values:", current_data)
            # Exits program
        elif user_input == '0':
            Exit = True
