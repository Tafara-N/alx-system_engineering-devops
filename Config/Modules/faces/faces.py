"""
Convert emoticons to emojis
"""

if __name__ == "__main__":
    emoticon = input("Start typing: ")
    emoticon_to_emoji = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    print(emoticon_to_emoji)
