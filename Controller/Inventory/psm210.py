import argparse
import json
import os
from datetime import datetime

def extract_endpoints(postman_file):
    endpoints = {}

    with open(postman_file, 'r') as file:
        collection = json.load(file)

    if 'item' in collection:
        extract_endpoints_from_item(collection['item'], endpoints)

    return endpoints


def extract_endpoints_from_item(items, endpoints):
    for item in items:
        if 'item' in item:
            extract_endpoints_from_item(item['item'], endpoints)
        else:
            request = item.get('request', {})
            url = request.get('url', {})
            if isinstance(url, dict):
                url = url.get('raw', '')
            method = request.get('method', '')
            if url:
                if url not in endpoints:
                    endpoints[url] = []
                if method and method not in endpoints[url]:
                    endpoints[url].append(method)


def aggregate_endpoints(endpoints):
    aggregated_endpoints = {}

    for url, methods in endpoints.items():
        if url not in aggregated_endpoints:
            aggregated_endpoints[url] = methods

    return aggregated_endpoints


def extract_file_folder(path):
    extracted_data = []
    total_endpoints = 0
    total_methods = 0

    if os.path.isfile(path):
        endpoints = extract_endpoints(path)
        extracted_data.append({
            "file": path,
            "endpoints": aggregate_endpoints(endpoints),
            "endpoint_count": len(endpoints),
            "method_count": sum(len(methods) for methods in endpoints.values())
        })
        total_endpoints += len(endpoints)
        total_methods += sum(len(methods) for methods in endpoints.values())

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and filename.endswith('.json'):
                endpoints = extract_endpoints(file_path)
                extracted_data.append({
                    "file": file_path,
                    "endpoints": aggregate_endpoints(endpoints),
                    "endpoint_count": len(endpoints),
                    "method_count": sum(len(methods) for methods in endpoints.values())
                })
                file_endpoints = len(endpoints)
                print(f"{file_path}: {file_endpoints} endpoints")
                total_endpoints += file_endpoints
                total_methods += sum(len(methods) for methods in endpoints.values())

    print(f"\nOverall Endpoint Count: {total_endpoints}")
    print(f"Overall Method Count: {total_methods}")

    return extracted_data

def handle_inv_psm(path):
    # Extract data
    extracted_data = extract_file_folder(path)

    # Save data as JSON
    current_time = datetime.now()
    file_path = "Output/psm_inventory_%s.json" % current_time.strftime("%Y%m%d_%H%M%S")
    with open(file_path, 'w') as file:
        json.dump(extracted_data, file, indent=4)

    print("Data saved in %s" % file_path)    

if __name__ == "__main__":
    # Set up argparse
    parser = argparse.ArgumentParser(description='Extract API endpoints from Postman Collection v2.1.0')
    parser.add_argument('path', help='Path to the Postman Collection JSON file or folder')

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
