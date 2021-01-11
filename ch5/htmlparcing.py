# 
# Example file for parsing and processing HTML
#

from html.parser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print('encountered comment: ', data)
    pos = self.getpos()
    print('\tAt line: ', pos[0], ' position ', pos[1])

  def handle_starttag(self, tag, attrs):
    global metacount
    
    if tag == 'meta': metacount += 1
    
    print('encountered tag: ', tag)
    pos = self.getpos()
    print('\tAt line: ', pos[0], ' position ', pos[1])
    
    
    if attrs.__len__() > 0:
      print('\tAttributes:')
      for a in attrs:
        print('\t',a[0],'=',a[1])
    
  def handle_endtag(self, tag):
    print('encountered tag: ', tag)
    pos = self.getpos()
    print('\tAt line: ', pos[0], ' position ', pos[1])
    
  def handle_data(self, data):
    if(data.isspace()): return
    
    print('encountered data: ', data)
    pos = self.getpos()
    print('\tAt line: ', pos[0], ' position ', pos[1])
  

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()

  f = open('samplehtml.html')

  if f.mode == 'r':
    content = f.read()
    parser.feed(content)
    

if __name__ == "__main__":
  main()
  