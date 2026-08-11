letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''
print(letter.replace("<|NAME|>", "Abhay").replace("<|DATE|>", "1st Jan 2024"))