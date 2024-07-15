def get_cats_info(path: str) -> dict:
  cats_info: list[dict] = [];

  try:
    with open(path, 'r', encoding='utf-8') as data:
      for line in data.read().splitlines():
        id, name, age = line.split(',');

        cats_info.append({
          "id": id,
          "name": name,
          "age": age
        });

  except FileNotFoundError as e:
    return 'File not found. Please check the path.';

  return cats_info;



cats_info = get_cats_info('./homework-2/task2/cats-data.txt');
print(cats_info);
