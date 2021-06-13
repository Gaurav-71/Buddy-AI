def analyzeMessage(message):
    if "clear" in message:
        print("from func")

print("before")
analyzeMessage("clear")
print("after")