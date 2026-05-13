def convert(text):
    text = text.replace(":)" ,"🙂")
    text = text.replace(":(" ,"🙁")
    return text
def main():
    user = input(" ")
    result = convert(user)
    print(result)
main()
