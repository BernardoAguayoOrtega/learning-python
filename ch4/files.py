#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  f = open('textfile.txt', 'w+')
  
  # Open the file for appending text to the end


  # write some lines of data to the file
  for i in range(10):
    f.write("This is line " + str(i) + "\r\n")
  
  # close the file when done

  
  # Open the file back up and read the contents
  f.close()
    
    
def main2():
  f = open("textfile.txt", 'a')
  
  for line in range(10):
    f.write('This is new line from other method #' + str(line) + '\r\n')

  f.close()

if __name__ == "__main__":
  main2()
