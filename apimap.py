import CLI.cli as cli
import Controller.Request.request

def main():
    printBanner()
    args = cli.parse_arguments()
    cli.validate_arguments(args)

    if args.command == 'req':
        Controller.Request.request.send_requests(args.template)
    elif args.command == 'gen':
        print("Generating YAML from Swagger and Postman files...")
        print("Swagger file:", args.swagger)
        print("Postman file:", args.postman)

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