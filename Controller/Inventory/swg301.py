import argparse
import os
import json


def extract_endpoints(openapi_file):
    # Load the OpenAPI specification from file
    try:
        with open(openapi_file, 'r') as file:
            openapi_spec = json.load(file)
    except FileNotFoundError:
        print(f"Failed to open OpenAPI specification file: {openapi_file}")
        return [], {}

    server_urls = []
    endpoints = {}
    total_methods = 0

    # Extract server URLs
    servers = openapi_spec.get('servers', [])
    for server in servers:
        server_url = server.get('url')
        if server_url:
            server_urls.append(server_url)

    # Extract endpoints and methods
    paths = openapi_spec.get('paths', {})
    for path, path_item in paths.items():
        for method, operation in path_item.items():
            endpoint_url = path
            if endpoint_url not in endpoints:
                endpoints[endpoint_url] = []
            endpoints[endpoint_url].append(method.upper())
            total_methods += 1

    return server_urls, endpoints, total_methods


def process_directory(directory):
    server_urls = []
    endpoints = {}
    total_methods = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json") or file.endswith(".txt"):
                file_path = os.path.join(root, file)
                file_server_urls, file_endpoints, file_total_methods = extract_endpoints(file_path)
                server_urls.extend(file_server_urls)
                endpoints.update(file_endpoints)
                total_methods += file_total_methods

    return server_urls, endpoints, total_methods

def handle_inv_swg(input_path):
    # Check if input path is a file or directory
    if os.path.isfile(input_path):
        # Process a single file
        server_urls, endpoints, total_methods = extract_endpoints(input_path)
    elif os.path.isdir(input_path):
        # Process a directory
        server_urls, endpoints, total_methods = process_directory(input_path)
    else:
        print(f"Invalid input path: {input_path}")
        exit()

    # Print counts
    print("\nSummary")
    print("=======")
    print("Total number of endpoints: ", len(endpoints))
    print("Total number of methods: ", total_methods)
    print()

    # Print server URLs
    print("URLS")
    print("====")
    for server_url in server_urls:
        print("Server URL: ", server_url)
    print()

    # Print endpoints
    print("Endpoints")
    print("=========")
    for endpoint_url, methods in endpoints.items():
        method_count = len(methods)
        print(f"{endpoint_url} : [{method_count}] : {', '.join(methods)}")


if __name__ == "__main__":
    # Set up argparse
    parser = argparse.ArgumentParser(description='Extract server URLs, endpoints, and methods from OpenAPI 3.0.1')
    parser.add_argument('input_path', help='Path to the OpenAPI specification file or directory')

    # Parse command-line arguments
    args = parser.parse_args()

    input_path = args.input_path

    # Check if input path is a file or directory
    if os.path.isfile(input_path):
        # Process a single file
        server_urls, endpoints, total_methods = extract_endpoints(input_path)
    elif os.path.isdir(input_path):
        # Process a directory
        server_urls, endpoints, total_methods = process_directory(input_path)
    else:
        print(f"Invalid input path: {input_path}")
        exit()

    # Print counts
    print("\nSummary")
    print("=======")
    print("Total number of endpoints: ", len(endpoints))
    print("Total number of methods: ", total_methods)
    print()

    # Print server URLs
    print("URLS")
    print("====")
    for server_url in server_urls:
        print("Server URL: ", server_url)
    print()

    # Print endpoints
    print("Endpoints")
    print("=========")
    for endpoint_url, methods in endpoints.items():
        method_count = len(methods)
        print(f"{endpoint_url} : [{method_count}] : {', '.join(methods)}")
