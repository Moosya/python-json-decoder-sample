import json

def write_json_structure(json_file,output_file=None):
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    json_str = write_json_structure_helper(json_data, 0)
    if output_file:
        with open(output_file, 'w') as f:
            f.write(json_str)
    else:
        print(json_str)

def write_json_structure_helper(data, indentation):
    json_str = ""
    if isinstance(data, dict):
        json_str += ' ' * indentation + '{\n'
        for key, value in data.items():
            print(f'Processing key: {key}') # print current key
            json_str += ' ' * (indentation + 4) + str(key) + ':\n'
            json_str += write_json_structure_helper(value, indentation + 8)
        json_str += ' ' * indentation + '}\n'
    elif isinstance(data, list):
        json_str += ' ' * indentation + '[\n'
        for item in data:
            json_str += write_json_structure_helper(item, indentation + 4)
        json_str += ' ' * indentation + ']\n'
    else:
        json_str += ' ' * indentation + str(data) + '\n'
    return json_str

json_file = 'path/to/json/file'
output_file = 'path/to/output/file' # None to print to stdout or provide filepath to write to file
write_json_structure(json_file,output_file)
