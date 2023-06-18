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

def get_endpoints(spec):
    paths = spec.get('paths', {})
    endpoints = []

    for path, methods in paths.items():
        if 'parameters' in methods:
            del methods['parameters']  # Remove 'parameters' key
        endpoint = {
            'path': path,
            'methods': methods.keys()
        }
        endpoints.append(endpoint)

    return endpoints

def count_endpoints(endpoints):
    num_endpoints = len(endpoints)
    method_counts = {}

    for endpoint in endpoints:
        methods = endpoint['methods']
        for method in methods:
            method_counts[method] = method_counts.get(method, 0) + 1

    return num_endpoints, method_counts

def swg_inv(spec_file):
    spec = parse_spec(spec_file)
    endpoints = get_endpoints(spec)
    num_endpoints, method_counts = count_endpoints(endpoints)

    print("All Endpoints:")
    for endpoint in endpoints:
        print(f"Path: {endpoint['path']}")
        print(f"Methods: {', '.join(endpoint['methods'])}")
        print()

    print(f"Total Endpoints: {num_endpoints}")
    print("Method Counts:")
    for method, count in method_counts.items():
        print(f"{method}: {count}")


if __name__ == '__main__':
    print('In Progress')

        