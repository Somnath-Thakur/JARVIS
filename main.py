websites = {
    # Search engines
    "google": "https://www.google.com",
    "bing": "https://www.bing.com",
    "duckduckgo": "https://duckduckgo.com",

    # Video and entertainment
    "youtube": "https://www.youtube.com",
    "netflix": "https://www.netflix.com",
    "prime video": "https://www.primevideo.com",
    "spotify": "https://open.spotify.com",
    "twitch": "https://www.twitch.tv",

    # Social media
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "x": "https://x.com",
    "twitter": "https://x.com",
    "reddit": "https://www.reddit.com",
    "discord": "https://discord.com/app",
    "linkedin": "https://www.linkedin.com",
    "whatsapp": "https://web.whatsapp.com",
    "telegram": "https://web.telegram.org",

    # Development and programming
    "github": "https://github.com",
    "gitlab": "https://gitlab.com",
    "stackoverflow": "https://stackoverflow.com",
    "stack overflow": "https://stackoverflow.com",
    "leetcode": "https://leetcode.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "geeks for geeks": "https://www.geeksforgeeks.org",
    "w3schools": "https://www.w3schools.com",
    "mdn": "https://developer.mozilla.org",
    "mdn docs": "https://developer.mozilla.org",
    "python docs": "https://docs.python.org/3/",
    "pypi": "https://pypi.org",
    "hugging face": "https://huggingface.co",
    "kaggle": "https://www.kaggle.com",
    "google colab": "https://colab.research.google.com",

    # AI tools
    "chatgpt": "https://chatgpt.com",
    "openai": "https://openai.com",
    "claude": "https://claude.ai",
    "gemini": "https://gemini.google.com",
    "perplexity": "https://www.perplexity.ai",

    # Google services
    "gmail": "https://mail.google.com",
    "google drive": "https://drive.google.com",
    "google maps": "https://maps.google.com",
    "google docs": "https://docs.google.com",
    "google meet": "https://meet.google.com",
    "google translate": "https://translate.google.com",
    "google classroom": "https://classroom.google.com",

    # Learning
    "coursera": "https://www.coursera.org",
    "edx": "https://www.edx.org",
    "freecodecamp": "https://www.freecodecamp.org",
    "free code camp": "https://www.freecodecamp.org",
    "w3resource": "https://www.w3resource.com",

    # Shopping
    "amazon": "https://www.amazon.com",
    "daraz": "https://www.daraz.com.np",

    # News and reference
    "wikipedia": "https://www.wikipedia.org",
    "bbc": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",

    # Gaming
    "steam": "https://store.steampowered.com",
    "epic games": "https://store.epicgames.com"
}


import webbrowser
from urllib.parse import quote_plus
from core import tool_registry


print("JARVIS is online.")

while True:

    command = input("Enter the command:")
    command = command.lower()
    
    if command == "exit":
        print("JARVIS: Shutting down...")
        break

    l1 = command.split()

    if len(l1) == 0:
        print("Please enter the command...")
        continue
        

    action = l1[0]

    target = l1[1:]
    target = " ".join(target)

    if action == "open":
        url = websites.get(target)
        if url:
            print(f"Opening {target} ...")
            tool_registry.TOOL_REGISTRY["opening"](url)
        else:
            print("The website is not recognized...")

    elif action == "search":
        print(f"Searching for {target} ...")
        tool_registry.TOOL_REGISTRY["searching"](target)
        

    else:
        print("I don't understand that command.")
