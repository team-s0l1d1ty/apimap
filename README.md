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
3. **Python Implementation** 
4. **API Specific** : APIMAP is developed with API Security Testing in mind and the basic scanning templates is created based on [OWASP Top 10 API Security Risks – 2019](https://owasp.org/API-Security/editions/2019/en/0x11-t10/).

### Roadmap
#### Stage 1 [Envisioned Usage]
- [ ] CLI 
   - [ ] cli.py
- [ ] Generator
   - [ ] swg.py (generates yaml based on swagger documentation)
   - [ ] auth.py (generates yaml to be used for authentication)
- [ ] Authentication
   - [ ] auth.py (sends authentication requests)
- [ ] Request 
   - [ ] request.py
   - [ ] response.py
   - [ ] handler.py

#### Stage 2 [Expanded Capabilities]
- [ ] Generator
   - [ ] psm.py
- [ ] Authentication
   - [ ] more authentication methods (TBA)

#### Stage 3 [QoL Improvements]
- [ ] TBA

## Installation and Basic Usage
### Dependencies
```
pip install pyyaml requests argparse
```

### Envisioned Usage
#### To Execute Test
Step 1 : generate YAML template 

``` 
python apimap.py gen swg bola {openapi specs}
```

Step 2 : generate authentication token

```
python apimap.py gen auth jwt 
```

Step 3 : Executing the test 

```
python apimap.py req {path to req testing template} {path to auth file} {output folder}
```

#### To get an Inventory based on openAPI specs or postman collection
```
# for swagger doc
python apimap.py gen swg inv {path to specs}
``` 

### Writing Template
Template conforms to all the parameters used in `Requests` library. Shown below are simple `GET` requests.
#### Sending GET requests
```
requests:
  - url: https://github.com
    method: GET

  - url: https://google.com
    method: GET
```

#### Sending GET requests with Proxy
```
In Progress
```

## Contributions and Feedback
Contributions and feedback are highly encouraged to enhance the functionality and effectiveness of APIMAP. Users are encouraged to actively participate by forking the repository, making modifications and submitting pull requests. Feedback, bug reports and feature requests can be shared through the repository's issue tracker. 

### Folder Structure
The follwing is the folder structure for more clarity:

```
.
├── apimap.py
├── CLI
│    └── cli.py
├── Controller            
│    ├── Generator
|    |    ├── swg.py (stage 1)
|    |    ├── psm.py (stage 2)
|    |    ├── inv.py (stage 2)
|    |    └── auth.py (stage 1)     
|    └── Request        
|         ├── request.py  (stage 1)
|         ├── response.py (stage 1)    
|         ├── Authentication
|         |    └── auth.py (stage 1)   
|         └── Test
|              └── handler.py (stage 1) 
├── Templates
|    └── skeleton_template.yaml
├── LICENSE
└── README.md
```

## License
APIMAP is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). This open-source license grants users the freedom to use, modify, and distibute the software while ensuring that any modifications remain open-source. It is essential to review and adhere to the license terms and conditions when utilizing and modifying the tool.

## Disclaimer
APIMAP is intended solely for security testing and vulnerability assesment of authorized APIs. Users are responsible for obtaining proper authorization and consent before conducting and scans. The tool's creator and contributor assume no liability for any misuse or illegal activities conducted using this software.
