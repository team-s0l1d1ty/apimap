# APIMAP {Work In Progress}

░█████╗░██████╗░██╗███╗░░░███╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║████╗░████║██╔══██╗██╔══██╗
███████║██████╔╝██║██╔████╔██║███████║██████╔╝
██╔══██║██╔═══╝░██║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░░██║██║░░░░░██║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░

APIMAP is a python based tool designed to automate API security testing. It utilizes YAML as the scanning template for defining security checks and tests against target APIs. This scanner is targeted but not limited to API security testing and aims to be the python HTTP scanner. It allows user to easily generate YAML templates using OpenAPI Specifications and Postman Collections.

## Key Features
1. **YAML Scanning Template** : APIMAP leverages YAML-based scanning templates allowing users to customise their own security checks and tests.
2. **OpenAPI and Postman Collection Support** : APIMAP has a template generation module that can generate basic YAML scanning template using OpenAPI specification or Postman Collections JSON. 
3. **API Specific** : APIMAP is developed with API Security Testing in mind and the basic scanning templates is created based on [OWASP Top 10 API Security Risks – 2019](https://owasp.org/API-Security/editions/2019/en/0x11-t10/).

## Installation and Usage
See [Installation and Usage](https://github.com/team-s0l1d1ty/apimap/wiki/Installation-and-Usage)

## Contributions and Feedback
Contributions and feedback are highly encouraged to enhance the functionality and effectiveness of APIMAP. Users are encouraged to actively participate by forking the repository, making modifications and submitting pull requests. Feedback, bug reports and feature requests can be shared through the repository's issue tracker. See [Contributor's Guide](https://github.com/team-s0l1d1ty/apimap/wiki/Contributor's-Guide)

## License
APIMAP is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). This open-source license grants users the freedom to use, modify, and distibute the software while ensuring that any modifications remain open-source. It is essential to review and adhere to the license terms and conditions when utilizing and modifying the tool.

## Disclaimer
APIMAP is intended solely for security testing and vulnerability assesment of authorized APIs. Users are responsible for obtaining proper authorization and consent before conducting and scans. The tool's creator and contributor assume no liability for any misuse or illegal activities conducted using this software.
