import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:

            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        valid_dir = os.path.isdir(target_dir)
        if not valid_dir:
            return f'Error: "{directory}" is not a directory'
        

        for file in target_dir:
            name = file
            size = os.path.getsize(file)
            is_dir = os.path.isdir(target_dir)
        
    except Exception as e:
        return f"Error: {e}"
    


    return f'Success: "{directory}" is within the working directory'


        




    

