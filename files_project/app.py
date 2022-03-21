my_file = open('data.txt', 'r') # 'r' stands for reading
file_content = my_file.read() # read the entire contents of the file as a single string


my_file.close() # closes the file so that you do not overload system

print(file_content)


user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w') # w for writing but it erases the contents of the file
                                        # anything you write will overwrite anything that is already there
my_file_writing.write(user_name)

my_file_writing.close()

