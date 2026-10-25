import webbrowser
import json
import subprocess
from urllib.parse import quote_plus


def open_web(target):
    return webbrowser.open(target)


def search_web(target):
    query = quote_plus(target)
    url = f"https://www.google.com/search?q={query}"
    return webbrowser.open(url)


def find_application(target):
        
    result = subprocess.run(
    ["powershell", "-Command", "Get-StartApps | ConvertTo-Json"],
    capture_output=True,
    text=True
)

    apps = json.loads(result.stdout)

    for app in apps:
        if target.casefold() == app["Name"].casefold():
            return app["AppID"]
    else:
        return None


    
def open_application(target):
    app_id = find_application(target)
    if app_id:
        subprocess.Popen(
    ["explorer.exe", f"shell:AppsFolder\\{app_id}"]
)
    else:
         print("Application Not Found!")
    
    

TOOL_REGISTRY = {
    'opening': open_web,
    'searching': search_web,
    'application': open_application
}

