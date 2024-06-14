def list_files(dir_path, pathtype='none'):
    """
    This function returns a list of filenames in a given directory (dir_path)
    The second input argument of this function defines the type of the path
    - if pathtype='none' the function returns only the filename 
    'filename.extenson'
    - if pathtype='rel' the function returns the relative pathname 
    'relpath \ filename.extenson'
    - if pathtype='abs' the function returns the absolute pathname 
    'abspath \ filename.extenson'
    """
    import os
    
    files = []
    try:
        if len(os.listdir(dir_path)) == 0:
            # empty directory
            print("Empty directory")
            return files
        else:
            # not empty directory
            for file_path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, file_path)):
                    if pathtype == 'none':
                        files.append(file_path)
                    elif pathtype == 'rel':
                        files.append(os.path.join(dir_path,file_path))
                    elif pathtype == 'abs':
                        files.append(os.path.abspath(os.path.join(dir_path,file_path)))
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {dir_path}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
    return files