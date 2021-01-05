#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print('myCLass method1')
    
  def method2(self, someString):
    print('myCLass method2' + someString)

class anotherClass(myClass):
  
  def method1(self):
    myClass.method1(self)
    print('anotherClass method1')
    myClass.method2(self, 'someString')
    
  def method2(self):
    print('anotherClass method2')

def main():
  c = myClass()
  
  c2 = anotherClass()
  
  c2.method1()
  c2.method2()  


if __name__ == "__main__":
    main()