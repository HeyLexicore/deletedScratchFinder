import requests
import lister

X_token = "Your x-token here"
projectSearchStart = 637857076 #2. Feb 2022
projectSearchEnd = 785587324 #9. Jan 2023    
endpoint = "https://api.scratch.mit.edu/projects/"
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://scratch.mit.edu',
    'priority': 'u=1, i',
    'referer': 'https://scratch.mit.edu/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0 (Edition std-1)',
    'x-token': X_token,
}


def getSingularProject(projectId):
    url=endpoint+str(projectId)
    
    re = requests.get(url,headers=headers)
    
    if not re.status_code == 200:
        #print("{} is a 404 project".format(projectId))
        return
    else:
        re = re.json()

    print("{} {} {}".format(re["visibility"], str(projectId), re["history"]["created"]))

    if re["visibility"] == "notvisible":
        open(str(projectId)+".txt","w").write("The project {} is a deleted project".format(str(projectId)))
    #print("Project {} is a public project but not a deleted project. It was created {}".format(projectId,re["history"]["created"]))
        


lister.process(range(projectSearchStart,projectSearchEnd),getSingularProject,1000)

