output = list()

def sentence(ans):

    ans = ans.capitalize()

    if ans.startswith(("How","What","Why")):
        ans  = ans + "?"
    else:
        ans = ans + "."
        
    output.append(ans)

while True:

    inp = input("Say something: ")

    if inp != "\end":
        sentence(inp)
        continue
    else:
        print (" ".join(output))
        break

