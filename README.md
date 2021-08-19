# GamingExcuseGenerator

Have you ever whiffed a game with your friends super hard but didn't want to admit the blame? Look no further! The Gaming Excuse Generator has your back. You can count on it to find you a good default excuse to get out of any gaming failure you come across 😎

## Installation

Grab the latest release here, or look through all the releases here. Simply download the release ZIP, extract it to the location of your choosing, and fire it up!

## Custom Excuses

By default, I've included a few basic excuses categorized by piece of equipment. However, you can easily add your own excuses!
- If you want to add to an existing category, simply add a line to the corresponding .txt file.
- If you want to create a new category, create a new .txt file in the root directory or any subdirectory and it will appear as a separate checkbox when you launch the application next!

## Building the Binary
I used [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html) for this. If you'd like to build the binary yourself, you can run the following in the root directory:
```bash
pyinstaller --onefile --noconsole -n "GamingExcuseGenerator" .\main.py
```

## Found a bug or want to request a feature?

Drop an issue/PR on this repository! I'll be here waiting 🌚
