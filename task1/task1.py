import re;

def total_salary(path: str) -> set | str:
  numbers = [];

  try:
    with open(path, 'r', encoding='utf-8') as data:
      for line in data.readlines():
        match = re.search(r'\d+$', line);

        if match:
          numbers.append(int(match.group()));
  except FileNotFoundError as e:
    return 'File not found. Please check the path.';


  return (sum(numbers), sum(numbers) // len(numbers)) if len(numbers) else 'Salary info not found or invalid file have been provided. Please check the syntax in your file.';

total, average = total_salary('./homework-2/task1/salaries-data.txt');
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}");
