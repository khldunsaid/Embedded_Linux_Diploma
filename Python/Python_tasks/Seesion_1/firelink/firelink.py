import webbrowser

# Define the dictionary with URLs
urls = [
    "https://khldunsaid.com",
    "https://github.com/khldunsaid",
    "https://www.linkedin.com/khldunsaid"
]

def firefox(var):
    webbrowser.get('firefox').open(urls[var])

    
def links_menu():
    return urls