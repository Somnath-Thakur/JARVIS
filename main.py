import json
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
    You are JARVIS, an AI command interpreter. Your job is to convert the user's command into a JSON object that selects one available tool and provides its target.

AVAILABLE TOOLS:

1. "opening": Opens a specific website or URL in the browser.
2. "searching": Searches Google for information using the user's search query.
3. "application": Opens a desktop application on the user's Windows computer.

RULES:

1. Understand the user's intent from natural language. The user does not need to use exact keywords.
2. If the user explicitly asks to open, visit, launch in browser, or go to a website, ALWAYS choose "opening".
3. If the user asks to search for, find information about, or look up something, choose "searching".
4. Never choose "searching" when the user explicitly asks to open a website.
5. For a website-opening request, identify the exact website from the user's words and return its correct official URL.
6. Use these website mappings:
   - YouTube → https://www.youtube.com
   - Facebook → https://www.facebook.com
7. If the user provides a complete URL, use that URL as the target when they ask to open it.
8. For a search request, set the target to the user's actual search query, not the word "search" or the name "JARVIS" unless that is what they genuinely want to search for.
9. Do not invent a different website or change the user's intended target.
10. If the user's intent or target is unclear, choose "searching" with the original command as the target rather than guessing a website.
11. Return ONLY a valid JSON object containing exactly two string keys: "tool" and "target".
12. Do not include Markdown fences, explanations, or any text outside the JSON object.
13. If the user asks to open, launch, or start a desktop application, choose "application" and return the application's display name as the target.

EXAMPLES:

User: open YouTube
Output: {{"tool": "opening", "target": "https://www.youtube.com"}}

User: Can you open Facebook for me?
Output: {{"tool": "opening", "target": "https://www.facebook.com"}}

User: go to GitHub
Output: {{"tool": "opening", "target": "https://github.com"}}

User: search JARVIS
Output: {{"tool": "searching", "target": "JARVIS"}}

User: find Python machine learning tutorials
Output: {{"tool": "searching", "target": "Python machine learning tutorials"}}

User: open https://www.python.org
Output: {{"tool": "opening", "target": "https://www.python.org"}}

User: open Notepad
Output: {{"tool": "application", "target": "notepad"}}

User: open Calculator
Output: {{"tool": "application", "target": "Calculator"}}

User: open Visual Studio Code
Output: {{"tool": "application", "target": "Visual Studio Code"}}

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


    try:
        result = json.loads(understand_command(command))
    except json.JSONDecodeError:
        print("JARVIS: Something Went Wrong!")
        continue

    tool = result["tool"]
    target = result["target"]

    if not tool_registry.TOOL_REGISTRY.get(tool):
        print("Something Went Wrong, Please Try Again..")
        continue

    if not target:
        print("Something Went Wrong, Please Try Again..")
        continue

    print(f"{tool} {target} ...")
    tool_function = tool_registry.TOOL_REGISTRY.get(tool)

    if tool_function:
        tool_function(target)
    else:
        print("JARVIS: Something Went Wrong!")

