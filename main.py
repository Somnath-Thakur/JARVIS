import os
from urllib.parse import quote_plus
from core import tool_registry
from dotenv import load_dotenv
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)




def understand_command(command):
    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""
    You are JARVIS, an AI command interpreter.

Your job is to understand what the user wants and decide which available tool should handle the request.

Available tools:
- opening: opens a website or URL
- searching: searches the web using Google

Rules:
1. Understand natural language. The user does not have to use exact commands.
2. If the user wants to open or visit a website, choose "opening".
3. If the user wants to search for information, choose "searching".
4. For an opening request, determine the correct website URL when you know it.
5. For a search request, return the user's search query as the target.
6. Do not perform the action yourself. Only decide which tool JARVIS should use.
7. Return ONLY this format:

tool: <tool name>
target: <target>

User command: {command}"""
    )
    return (response.text)





print("JARVIS is online.")
while True:

    command = input("Enter the command:")
    command = command.lower()
    
    if command == "exit":
        print("JARVIS: Shutting down...")
        break

    check_empty_command = command.split()
    if len(check_empty_command) == 0:
        print("Please enter the command...")
        continue


    result = understand_command(command) 
    result_lines = result.splitlines()

    if len(result_lines) != 2:
        print("JARVIS: Invalid response from Gemini.")
        continue

    if not result_lines[0].startswith("tool:"):
        print("JARVIS: Invalid response from Gemini.")
        continue

    if not result_lines[1].startswith("target:"):
        print("JARVIS: Invalid response from Gemini.")
        continue
         

    result_l1 = result_lines[0].split(":")
    result_l2 = result_lines[1].split(":",1)
    tool = result_l1[1].strip()
    target = result_l2[1].strip()

        

    
    print(f"{tool} {target} ...")
    tool_function = tool_registry.TOOL_REGISTRY.get(tool)

    if tool_function:
        tool_function(target)
    else:
        print("Something Went Wrong!")

