from yapf.yapflib.yapf_api import FormatFile  # reformat a file

print(open("printer.py").read())  # contents of file

reformatted_code, encoding, changed = FormatFile("printer.py", in_place=True)
print(reformatted_code)
print(f"changed = {changed}")

# yapf -ir . #reformat all in a dir
