import pytest
from demo import Utils
from demo import remove_duplicate

ut = Utils()
@pytest.fixture
def testlist():
  return ["a", "b", "a", "c", "c"]
  

@remove_duplicate
def reverse(testlist)
  return testlist

def test1():
  print('Test 1:')
  counter = ut.count_to(3)
  for number in counter:
    print(number)
  #using iter
  #read the file and display if error
  for line in ut.read_file('C:\\Work\\global-python\\apiSetup.txt'):
    if "ERROR" in line:
      print(line)

def test2():
  t2 = testlist()
  print('Test 2:', len(t2))
  assert len(t2) == 3
  myit = iter(t2)
  print(next(myit))
  print(next(myit))
  print(next(myit))
  #expect error
  try:
    print(next(myit))
  except:
    print('expect iteration error')
  
test1()
test2()