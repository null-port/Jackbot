import json

def convert_jsonl_to_json(input_file, output_file):
    # List to hold the converted data
    converted_data = []

    # Open the JSONL file and read line by line
    with open(input_file, 'r') as jsonl_file:
        for line in jsonl_file:
            # Parse each line as a JSON object
            message_obj = json.loads(line.strip())

            # Extract the necessary fields from the message object
            system_content = message_obj["messages"][0]["content"]
            user_content = message_obj["messages"][1]["content"]
            assistant_content = message_obj["messages"][2]["content"]

            # Create a new object with the desired structure
            converted_obj = {
                "instruction": system_content,
                "input": user_content,
                "output": assistant_content
            }

            # Add the new object to the list
            converted_data.append(converted_obj)

    # Write the converted data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(converted_data, json_file, indent=4)

# Example usage
input_file = 'Quiplash Data/500qs_dataset.jsonl'
output_file = '500qs_dataset_unsloth_format.json'
convert_jsonl_to_json(input_file, output_file)
