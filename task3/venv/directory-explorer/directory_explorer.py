import sys;
from pathlib import Path
from colorama import Fore;

try:
    current_file_name, param = sys.argv;
except ValueError as e:
   print('Missing path param');
   exit();
except BaseException as e:
   print ('Error happend:', e);
   exit();


current_file_name, param = sys.argv;

if not Path.exists(Path(param)):
   print('The directory does not exists');
   exit();

def get_path_tree(path: str, num_of_spaces: int = 3) -> str:
  spaces = " " * num_of_spaces;

  for item in path.iterdir():
    if item.is_file():
        print(spaces, Fore.GREEN + item.name)
    elif item.is_dir():
        print(spaces, Fore.BLUE + item.name + '/')
        get_path_tree(item, num_of_spaces + 3);
    else:
        print(Fore.RED + f"{item} is neither a file nor a directory.")
  
paramPath = Path(param);

# Show base name
print(Fore.BLUE + paramPath.name);

# Render folders tree
get_path_tree(paramPath);
