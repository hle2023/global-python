#decorative that remove duplication in a list
def remove_duplicate(func):
  def wrapper():
    original = func()       
    return list(dict.fromkeys(original))
  return wrapper  # Return the wrapper function to be used later

class Utils:
  def count_to(self, max_value):
    count = 1
    while count <= max_value:
      yield count
      count += 1

  def read_file(self, file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
      for line in f:
        yield line.strip()


