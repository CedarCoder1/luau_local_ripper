with open("code.txt", "r") as file:
    code = file.read()

    # Find the index of "local" in the code
    index = code.find("local")

    # Get the substring starting from the index of "local"
    substring = code[index + len("local"):]

    with open("locals.txt", "w") as file:
        lines = code.split("\n")
        for i, line in enumerate(lines, start=1):
            if "local" in line:
                file.write(f"Line {i}: {line}\n")

print("Done.")
input()
