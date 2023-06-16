import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='APIMAP')

    subparsers = parser.add_subparsers(title='subcommands', dest='command')
    subparsers.required = True

    # Request subcommand parser
    req_parser = subparsers.add_parser('req', help='Send requests using YAML template')
    req_parser.add_argument('template', help='Path to the YAML template file or directory')

    # Generate subcommand parser
    gen_parser = subparsers.add_parser('gen', help='Generate YAML')
    gen_parser.add_argument('swagger', type=str, help='Path to Swagger Documentation file')
    gen_parser.add_argument('postman', type=str, help='Path to Postman Collection file')

    return parser.parse_args()

def validate_arguments(args):
    if args.command == 'req':
        if os.path.isfile(args.template) or os.path.isdir(args.template):
            return
        else:
            raise ValueError(f"Invalid path: {args.template}. File or directory not found.")
    elif args.command == 'gen':
        if not os.path.isfile(args.swagger):
            raise ValueError(f"Invalid path: {args.swagger}. Swagger Documentation file not found.")
        if not os.path.isfile(args.postman):
            raise ValueError(f"Invalid path: {args.postman}. Postman Collection file not found.")
