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
                                  
(!) Legal Disclaimer : APIMAP is intended solely for security testing and vulnerability assesment of authorized APIs.
Users are responsible for obtaining proper authorization and consent before conducting and scans. 
The tool's creator and contributor assume no liability for any misuse or illegal activities conducted using this software.

(~) License : APIMAP is released under the GNU General Public License v3.0. 
This open-source license grants users the freedom to use, modify, and distibute the software while ensuring that any modifications remain open-source.
	""") 

def main():
    printBanner()
    args = cli.parse_arguments()
    handler.handle_commands(args)
    
if __name__ == '__main__':
    main()