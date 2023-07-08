import argparse
import os
from datetime import datetime
import yaml,json
import requests, urllib3

def send_requests(path):
    if os.path.isfile(path):
        return send_request(path)
    elif os.path.isdir(path):
        responses = []
        for filename in os.listdir(path):
            # if filename.endswith('.json'):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                template_path = os.path.join(path, filename)
                response = send_request(template_path)
                responses.extend(response)
        return responses


def send_request(template_path):
    with open(template_path) as template_file:
        template = yaml.safe_load(template_file)
        # template = json.load(template_file)

        requests_template = template.get('requests',[])
        name_template = template.get('name', 'Template with No Name')
        print('[-] Executing %s' % name_template)
        
        responses = []
        for request_template in requests_template:
            validate_request_parameters(request_template)
            # Extract response_checks and proxies from the request_template
            response_checks = request_template.pop('response_checks', None)
            proxies = request_template.pop('proxies', None)
            verify = request_template.pop('verify',None)
            allow_redirects = request_template.pop('allow_redirects',True)

            # Disable InsecureRequestWarning
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Send request and add response received into a dictionary
            response = requests.request(proxies=proxies,verify=verify,allow_redirects=allow_redirects, **request_template)
            response_dict = {
                'name':name_template,
                'request':request_template,
                'response': response, 
                'response_checks': response_checks
                }
            responses.append(response_dict)
        print('[+] Completed %s' % name_template)
        return responses


def perform_response_checks(response, response_checks):
    check_results = []
    for check in response_checks:
        if 'status_code' in check:
            expected_status_code = check['status_code']
            actual_status_code = response.status_code
            is_matched = expected_status_code == actual_status_code
            check_results.append({
                    'Expected Status Code': expected_status_code,
                    'Actual Status Code': actual_status_code,
                    'Match': is_matched
                })

        if 'headers' in check:
            headers = check['headers']
            for header_check in headers:
                header_name = header_check['name']
                expected_value = header_check['value']
                actual_value = response.headers.get(header_name)
                is_matched = expected_value in actual_value
                check_results.append({
                    'Header':header_name,
                    'Expected Value':expected_value,
                    'Actual value': actual_value,
                    'Match':is_matched
                })

        if 'text' in check:
            patterns = check['text']
            response_text = response.text
            for pattern in patterns:
                expected_pattern = pattern['pattern']
                is_matched = expected_pattern in response_text
                check_results.append({
                    'Pattern': expected_pattern,
                    'Match': is_matched
                })

    return check_results


def validate_request_parameters(request_template):
    valid_parameters = set(requests.Request('').__dict__.keys())
    valid_parameters.add('proxies')
    valid_parameters.add('response_checks')
    valid_parameters.add('verify')
    valid_parameters.add('allow_redirects')
    for param in request_template.keys():
        if param not in valid_parameters:
            raise ValueError(f"Invalid parameter in request template: {param}")

def handle_req(template_path):
    responses = send_requests(template_path)
    all_results = []
    for response in responses:
        response_checks = response.get('response_checks')
        if response_checks:
            one_result = []
            one_result.append(response['name'])
            one_result.append(response['request'])
            one_result.append({
                "status_code":response['response'].status_code,
                "headers": str(response['response'].headers),
                "content": response['response'].text
            })
            for check_result in perform_response_checks(response['response'], response_checks):
                one_result.append(check_result)
            all_results.append(one_result)
        else:
            one_result = []
            one_result.append(response['name'])
            one_result.append(response['request'])
            one_result.append({
                "status_code":response['response'].status_code,
                "headers": str(response['response'].headers),
                "content":  response['response'].text
            })
            one_result.append({"result":"No response checks defined for this request."})
            all_results.append(one_result)
    
    current_time = datetime.now()
    file_path = "Output/results_%s.json" % current_time.strftime("%Y%m%d_%H%M%S")
    with open(file_path,"w") as json_file:
        json.dump(all_results,json_file)
    print('[+] Results are saved in %s' % (file_path))
    print('[+] results.json can be viewed with /Output/Pages/index.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send requests and perform response checks.')
    parser.add_argument('template', help='Path to the template file')
    args = parser.parse_args()

    template_path = args.template
    response_objects = send_requests(template_path)

    # Process the response_objects as needed
    print(response_objects)

    # Perform response checks for each response
    for response in response_objects:
        response_checks = response.get('response_checks')
        if response_checks:
            for check_result in perform_response_checks(response['response'], response_checks):
                print(check_result)
        else:
            print("No response checks defined for this request.")
