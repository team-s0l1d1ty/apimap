import CLI.cli as cli
import CLI.handler as handler

def printBanner():
	print("""
	
░█████╗░██████╗░██╗███╗░░░███╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║████╗░████║██╔══██╗██╔══██╗
███████║██████╔╝██║██╔████╔██║███████║██████╔╝
██╔══██║██╔═══╝░██║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░░██║██║░░░░░██║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╯
                                  
	""") 

def main():
    printBanner()
    args = cli.parse_arguments()
    cli.validate_arguments(args)
    handler.handle_commands(args)

if __name__ == '__main__':
    main()