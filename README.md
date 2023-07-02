# Directories.py

## Features
* Create directories: Users can create directories by specifying the desired path. Parent directories must exist for a new directory to be created.
* Move directories: Directories can be moved from one location to another.
* Delete directories: Directories can be deleted if they do not have any child directories. Deleting a directory also removes its contents.
* List directories: Users can list all directories and their nested structure in alphabetical order.

## Run App
```
python3 directories.py
```

### Usage

1. Create and List directories

Input:
```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
```

Output:
```
fruits
  apples
    fuji
grains
vegetables
```

2. Move directories

Input:
```
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
```

Output:
```
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
```

3. Delete directories

Input:
```
DELETE fruits/apples
DELETE foods/fruits/apples
LIST
```

Output:
```
Cannot delete fruits/apples - fruits does not exist
foods
  fruits
  grains
  vegetables
    squash
```

### Run Unit Tests

```
python3 tests.py
```
