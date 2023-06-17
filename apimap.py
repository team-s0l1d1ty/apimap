import CLI.cli as cli
import Controller.Request.request

def main():
    printBanner()
    args = cli.parse_arguments()
    cli.validate_arguments(args)

    if args.command == 'req':
        Controller.Request.request.send_requests(args.template)
    elif args.command == 'gen':
       command_mapping = cli.command_mapping()
       if args.gen_command in command_mapping:
             func = command_mapping[args.gen_command]
             arguments = vars(args)
             del arguments['command']
             del arguments['gen_command']
             func(**arguments)
    elif args.command == 'auth':
         pass


def printBanner():
	print("""
	
░█████╗░██████╗░██╗███╗░░░███╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║████╗░████║██╔══██╗██╔══██╗
███████║██████╔╝██║██╔████╔██║███████║██████╔╝
██╔══██║██╔═══╝░██║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░░██║██║░░░░░██║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╯
                                  
	""") 

if __name__ == '__main__':
    main()