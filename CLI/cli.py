import argparse
import os

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
                    },
                    'inv': {
                        'help': 'Generate Swagger inventory for swagger',
                        'args': {
                            'path': {
                                'help': 'Path to swagger documentation',
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

def validate_arguments(args):
    if args.command == 'req':
        if os.path.isfile(args.template) or os.path.isdir(args.template):
            return
        else:
            raise ValueError(f"Invalid path: {args.template}. File or directory not found.")
    elif args.command == 'auth':
        if not os.path.isfile(args.auth_yaml):
            raise ValueError(f"Invalid path: {args.auth_yaml}. file not found.")

if __name__ == '__main__':
    args = parse_arguments()
    print(args)