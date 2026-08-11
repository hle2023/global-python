def read_file(file_path):
  f = open(file_path, 'r', encoding="utf-8")
  for line in f:
    yield line

def count_to(max_value):
  count = 1
  while count <= max_value:
    yield count
    count += 1

#decorative that remove duplication in a list
def remove_duplicate(func):
  def wrapper():
    original = func()       
    return list(dict.fromkeys(original))
  return wrapper  # Return the wrapper function to be used later

@remove_duplicate
def test2():
  return ["a", "b", "a", "c", "c"]

def test1():
  print('Test 1:')
  counter = count_to(3)
  for number in counter:
    print(number)
  #read the file and display if error
  for line in read_file('C:\\Work\\global-python\\apiSetup.txt'):
    if "ERROR" in line:
      print(line)

print('Test 2:', len(test2()))
test1()
