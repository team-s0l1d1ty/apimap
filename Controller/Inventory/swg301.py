import argparse
import json, yaml
import os
from datetime import datetime

def extract_endpoints(openapi_file):
    endpoints = {}

    with open(openapi_file, 'r') as file:
        if openapi_file.endswith('.json'):
            openapi_spec = json.load(file)
        elif openapi_file.endswith('.yaml') or openapi_file.endswith('.yml'):
            openapi_spec = yaml.safe_load(file)
        else:
            print(f"Invalid file format: {openapi_file}")
            return endpoints

    paths = openapi_spec.get('paths', {})
    for path, path_item in paths.items():
        methods = list(path_item.keys())
        endpoints[path] = methods

    return endpoints


def extract_file_folder(path):
    extracted_data = []
    total_endpoints = 0
    total_methods = 0

    if os.path.isfile(path):
        endpoints = extract_endpoints(path)
        extracted_data.append({"file": path, "endpoints": endpoints, "endpoint_count": len(endpoints), "method_count": sum(len(methods) for methods in endpoints.values())})
        total_endpoints += len(endpoints)
        total_methods += sum(len(methods) for methods in endpoints.values())

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and (filename.endswith('.json') or filename.endswith('.yaml') or filename.endswith('.yml')):
                endpoints = extract_endpoints(file_path)
                extracted_data.append({"file": file_path, "endpoints": endpoints, "endpoint_count": len(endpoints), "method_count": sum(len(methods) for methods in endpoints.values())})
                file_endpoints = len(endpoints)
                file_methods = sum(len(methods) for methods in endpoints.values())
                print(f"{file_path}: {file_endpoints} endpoints, {file_methods} methods")
                total_endpoints += file_endpoints
                total_methods += file_methods

    print(f"\nOverall Endpoint Count: {total_endpoints}")
    print(f"Overall Method Count: {total_methods}")

    return extracted_data

def handle_inv_swg(path):
    # Extract data
    extracted_data = extract_file_folder(path)

    # Save data as JSON
    current_time = datetime.now()
    file_path = "Output/swg_inventory_%s.json" % current_time.strftime("%Y%m%d_%H%M%S")
    with open(file_path, 'w') as file:
        json.dump(extracted_data, file, indent=4)

    print("Data saved in %s" % file_path)    

if __name__ == "__main__":
    # Set up argparse
    parser = argparse.ArgumentParser(description='Extract API endpoints from OpenAPI Specification')
    parser.add_argument('path', help='Path to the OpenAPI Specification file or folder')

    # Parse command-line arguments
    args = parser.parse_args()

    path = args.path

    # Extract data
    extracted_data = extract_file_folder(path)

    # Save data as JSON
    output_file = "output.json"
    with open(output_file, 'w') as file:
        json.dump(extracted_data, file, indent=4)

    print(f"\nData saved in {output_file} file.")
