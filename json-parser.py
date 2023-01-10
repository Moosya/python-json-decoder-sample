import json

# Function to parse a JSON file
def parse_json(file_path):
    # Open the file
    with open(file_path, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)
        
        # Iterate through the data and print each item
        for item in data:
            print(item)

# Main function
def main():
    # File path of the JSON file
    file_path = 'large_json_file.json'
    
    # Parse the JSON file
    parse_json(file_path)

# Run the main function
if __name__ == '__main__':
    main()
