import argparse
import json
import os

def extract_endpoints(collection_file):
    endpoints = {}
    total_methods = 0

    with open(collection_file, 'r') as file:
        collection = json.load(file)

    # Extract server URL
    server_url = collection.get('info', {}).get('schema', '')

    # Extract endpoints and methods
    items = collection.get('item', [])
    for item in items:
        process_item(item, endpoints)

    total_endpoints = len(endpoints)
    for methods in endpoints.values():
        total_methods += len(methods)

    return server_url, total_endpoints, total_methods, endpoints


def process_item(item, endpoints):
    if 'item' in item:
        for sub_item in item['item']:
            process_item(sub_item, endpoints)
    else:
        request = item.get('request')
        if request:
            endpoint_url = request.get('url')
            method = request.get('method')
            if endpoint_url and method:
                endpoint_key = endpoint_url['raw']
                if endpoint_key not in endpoints:
                    endpoints[endpoint_key] = []
                if method not in endpoints[endpoint_key]:
                    endpoints[endpoint_key].append(method)


def process_directory(directory):
    endpoints = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                _, _, _, file_endpoints = extract_endpoints(file_path)
                for endpoint_url, methods in file_endpoints.items():
                    if endpoint_url not in endpoints:
                        endpoints[endpoint_url] = methods

    return endpoints

def handle_inv_psm(input_path):
    if os.path.isfile(input_path):
        # Process a single file
        server_url, total_endpoints, total_methods, endpoints = extract_endpoints(input_path)
    elif os.path.isdir(input_path):
        # Process a directory
        endpoints = process_directory(input_path)
        server_url = ""
        total_endpoints = len(endpoints)
        total_methods = sum(len(methods) for methods in endpoints.values())
    else:
        print(f"Invalid input path: {input_path}")
        exit()    
    # Print summary
    print("Summary")
    print("=======")
    print("Total number of endpoints:", total_endpoints)
    print("Total number of methods:", total_methods)
    print()

    # Print server URL
    print("URLS")
    print("====")
    print("Server URL:", server_url)
    print()

    # Print endpoints
    print("Endpoints")
    print("=========")
    for endpoint_url, methods in endpoints.items():
        method_count = len(methods)
        methods_string = " ".join(methods)
        print(f"{endpoint_url} : [{method_count}] : {methods_string}")

if __name__ == "__main__":
    # Set up argparse
    parser = argparse.ArgumentParser(description='Extract endpoints and methods from Postman Collection v2.1.0')
    parser.add_argument('input_path', help='Path to the Postman Collection file or directory')

    # Parse command-line arguments
    args = parser.parse_args()

    input_path = args.input_path

    # Check if input path is a file or directory
    if os.path.isfile(input_path):
        # Process a single file
        server_url, total_endpoints, total_methods, endpoints = extract_endpoints(input_path)
    elif os.path.isdir(input_path):
        # Process a directory
        endpoints = process_directory(input_path)
        server_url = ""
        total_endpoints = len(endpoints)
        total_methods = sum(len(methods) for methods in endpoints.values())
    else:
        print(f"Invalid input path: {input_path}")
        exit()

    # Print summary
    print("Summary")
    print("=======")
    print("Total number of endpoints:", total_endpoints)
    print("Total number of methods:", total_methods)
    print()

    # Print server URL
    print("URLS")
    print("====")
    print("Server URL:", server_url)
    print()

    # Print endpoints
    print("Endpoints")
    print("=========")
    for endpoint_url, methods in endpoints.items():
        method_count = len(methods)
        methods_string = " ".join(methods)
        print(f"{endpoint_url} : [{method_count}] : {methods_string}")
