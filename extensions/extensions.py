file = input("What is your file name? ")
file = file.lower().rstrip()
suffixes = (".gif", ".jpg", ".jpeg",".png",".pdf",".txt",".zip")

def main():
    if file.endswith(suffixes):
        for i in suffixes:
            if file.endswith(i):
                if i in {".pdf",".zip"}:
                    i = i.replace(".","")
                    print(f"application/{i}")
                elif i in {".txt"}:
                    i = i.replace(".","")
                    print(f"text/plain")
                else:
                    i = i.replace(".","")
                    print(f"image/{i}")
                return

            else:
                pass
    else:
        print("application/octet-stream")

main()