import os
import Controller.Request.request
import Controller.Generator.swg
import Controller.Inventory.psm210, Controller.Inventory.swg301


def handle_req(args):
    Controller.Request.request.handle_req(args.template)

def handle_auth_jwt(args):
    Controller.Request.request.send_request(args.auth_yaml)

def handle_auth_cookie(args):
    auth = args.auth_yaml
    print(auth)

def handle_gen_auth_jwt(args):
    username = args.username
    password = args.password
    print(username + password)

def handle_gen_auth_cookie(args):
    username = args.username
    password = args.password
    print(username + password)

def handle_gen_swg_bola(args):
    path = args.path
    print(path)

def handle_inv_swg(args):
    path = args.path
    Controller.Inventory.swg301.handle_inv_swg(path)

def handle_inv_psm(args):
    path = args.path
    Controller.Inventory.psm210.handle_inv_psm(path)    

def handle_commands(args):
    command_handlers = {
        'req': handle_req,
        'auth': {
            'jwt': handle_auth_jwt,
            'cookie': handle_auth_cookie
        },
        'inv':{
            'psm': handle_inv_psm,
            'swg': handle_inv_swg
        },
        'gen': {
            'jwt': handle_gen_auth_jwt,
            'cookie': handle_gen_auth_cookie,
            'bola': handle_gen_swg_bola,
        }
    }
    command = args.command
    handler = command_handlers.get(command)

    if handler is None:
        print(f"Invalid command: {command}")
        return

    if callable(handler):
        handler(args)
    elif isinstance(handler, dict):
        subcommand = args.subcommand
        subcommand_handler = handler.get(subcommand)

        if subcommand_handler is None:
            print(f"Invalid subcommand: {subcommand}")
            return

        if callable(subcommand_handler):
            subcommand_handler(args)
        else:
            handle_commands(args, subcommand_handler)
    else:
        print(f"Invalid command handler: {handler}")