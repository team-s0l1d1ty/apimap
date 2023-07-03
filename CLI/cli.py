import argparse

# Define the command structure dictionary
commands = {
    'req': {
        'help': 'Send requests using YAML template',
        'args': {
            'template': {
                'help': 'Path to the YAML template file or directory',
                'type': str
            }
        }
    },
    'auth': {
        'help': 'sends authentication requests',
        'subcommands': {
            'jwt': {
                'help': 'sends auth.yaml and extracts jwt token',
                'args': {
                    'auth_yaml': {
                        'help': 'Username for authentication',
                        'type': str
                    }
                }
            },
            'cookie': {
                'help': 'sends auth.yaml and extracts cookies',
                'args': {
                    'auth_yaml': {
                        'help': 'Username for authentication',
                        'type': str
                    }
                }
            }
        }
    },
    'inv':{
        'help': 'API Inventory Operations',
        'subcommands':{
            'psm':{
                'help':'Get a Quick Inventory of APIs in Postman Collection v2.1.0 Directory or File',
                'args':{
                    'path':{
                        'help':'Path to Postman Collection v2.1.0 Directory or File',
                        'type': str
                    }
                }
            },
            'swg':{
                'help':'Path to Swagger Specification v3.0.1 Directory or File',
                'args':{
                    'path':{
                        'help':'Path to Swagger Specification v3.0.1 Directory or File',
                        'type':str
                    }
                }
            }
        }
    },
    'gen': {
        'help': 'YAML generation operations',
        'subcommands': {
            'auth': {
                'help': 'Generate authentication',
                'subcommands': {
                    'jwt': {
                        'help': 'Generate YAML to request and extract JWT',
                        'args': {
                            'username': {
                                'help': 'Username for authentication',
                                'type': str
                            },
                            'password': {
                                'help': 'Password for authentication',
                                'type': str
                            }
                        }
                    },
                    'cookie': {
                        'help': 'Generate YAML to request and extract cookie',
                        'args': {
                            'username': {
                                'help': 'Username for authentication',
                                'type': str
                            },
                            'password': {
                                'help': 'Password for authentication',
                                'type': str
                            }
                        }
                    }
                }
            },
            'swg': {
                'help': 'Generate Command for Swagger',
                'subcommands': {
                    'bola': {
                        'help': 'Generate BOLA YAML based on Swagger',
                        'args': {
                            'path': {
                                'help': 'Path for Swagger BOLA generation',
                                'type': str
                            }
                        }
                    }
                }
            }
        }
    }
}

def generate_args(args_dict, subparser):
    if 'subcommands' in args_dict:
        subparsers_sub = subparser.add_subparsers(dest='subcommand', title='subcommands')
        for subcommand, subcommand_dict in args_dict['subcommands'].items():
            subparser_sub = subparsers_sub.add_parser(subcommand, help=subcommand_dict['help'])
            generate_args(subcommand_dict, subparser_sub)
    if 'args' in args_dict:
        for arg, arg_dict in args_dict['args'].items():
            subparser.add_argument(arg, **arg_dict)

def parse_arguments():
    parser = argparse.ArgumentParser(description='APIMAP')

    subparsers = parser.add_subparsers(title='subcommands', dest='command')
    subparsers.required = True

    # Generate the command-line arguments based on the dictionary
    for command, command_dict in commands.items():
        command_parser = subparsers.add_parser(command, help=command_dict['help'])
        generate_args(command_dict, command_parser)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    print(args)