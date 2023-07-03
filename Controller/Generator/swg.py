import json
import yaml

def parse_spec(spec_file):
    with open(spec_file, 'r') as file:
        try:
            # Try parsing as JSON
            spec = json.load(file)
        except json.JSONDecodeError:
            file.seek(0)
            try:
                # If parsing as JSON fails, try parsing as YAML
                spec = yaml.safe_load(file)
            except yaml.YAMLError:
                raise ValueError("Invalid file format. Please provide a YAML or JSON file.")

    return spec

if __name__ == '__main__':
    print('In Progress')

        