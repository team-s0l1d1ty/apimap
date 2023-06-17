import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='APIMAP')

    subparsers = parser.add_subparsers(title='subcommands', dest='command')
    subparsers.required = True

    '''
    req subcommand parser
    '''
    req_parser = subparsers.add_parser('req', help='Send requests using YAML template')
    req_parser.add_argument('template', help='Path to the YAML template file or directory')

    '''
    auth subcommand parser
    '''
    auth_parser = subparsers.add_parser('auth', help='sends authentication requests')
    auth_parser.add_argument('auth_yaml', help='Path to the Auth YAML template file')

    '''
    gen subcommand parser
    '''  
    gen_parser = subparsers.add_parser('gen', help='YAML generation operations')
    gen_subparsers = gen_parser.add_subparsers(dest='gen_command', title='Generate commands')

    # gen auth subcommand parser
    auth_parser = gen_subparsers.add_parser('auth', help='Generate authentication')
    auth_subparsers = auth_parser.add_subparsers(dest='auth_command', title='Authentication commands')

    jwt_parser = auth_subparsers.add_parser('jwt', help='Generate YAML to request and extract JWT')
    jwt_parser.add_argument('username', type=str, help='Username for authentication')
    jwt_parser.add_argument('password', type=str, help='Password for authentication')

    cookie_parser = auth_subparsers.add_parser('cookie', help='Generate YAML to request and extract cookie')
    cookie_parser.add_argument('username', type=str, help='Username for authentication')
    cookie_parser.add_argument('password', type=str, help='Password for authentication')

    # gen swg subcommand parser
    swg_parser = gen_subparsers.add_parser('swg', help='Generate Command for Swagger')
    swg_subparsers = swg_parser.add_subparsers(dest='swg_command', title='Swagger commands')

    bola_parser = swg_subparsers.add_parser('bola', help='Generate BOLA YAML based on Swagger')
    bola_parser.add_argument('path', type=str, help='Path for Swagger BOLA generation')

    inv_parser = swg_subparsers.add_parser('inv', help='Generate Swagger inventory for swagger')
    inv_parser.add_argument('path', type=str, help='path to swagger documentation')

    return parser.parse_args()

def command_mapping():
   command_mapping = {
      'jwt': 'generate_auth_jwt',
      'cookie': 'generate_auth_cookie',
      'bola': 'generate_swagger_bola',
      'inv': 'generate_swagger_inv',
    }
   return command_mapping 

def validate_arguments(args):
    if args.command == 'req':
        if os.path.isfile(args.template) or os.path.isdir(args.template):
            return
        else:
            raise ValueError(f"Invalid path: {args.template}. File or directory not found.")
    elif args.command == 'auth':
        if not os.path.isfile(args.auth_yaml):
            raise ValueError(f"Invalid path: {args.auth_yaml}. file not found.")
