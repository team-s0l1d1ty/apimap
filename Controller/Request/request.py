import os
import yaml
import requests
import CLI.cli

def send_requests(path):
    if os.path.isfile(path):
        send_request(path)
    elif os.path.isdir(path):
        send_requests_from_directory(path)

def send_requests_from_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            template_path = os.path.join(directory, filename)
            send_request(template_path)

def send_request(template_path):
    with open(template_path) as template_file:
        template = yaml.safe_load(template_file)

        requests_template = template['requests']
        for request_template in requests_template:
            validate_request_parameters(request_template)

            response = requests.request(**request_template)

            print('URL:', request_template['url'])
            print('Response status code:', response.status_code)
            print('---')

def validate_request_parameters(request_template):
    valid_parameters = requests.Request('').__dict__.keys()
    for param in request_template.keys():
        if param not in valid_parameters:
            raise ValueError(f"Invalid parameter in request template: {param}")

if __name__ == '__main__':
    args = CLI.cli.parse_arguments()

    if args.command == 'req':
        send_requests(args.template)
