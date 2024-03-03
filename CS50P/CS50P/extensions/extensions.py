x = input("File name: ").lower().strip()
filetype = x[-4:]
match filetype:
    case ".gif" | ".png":
        print(f"image/{filetype[-3:]}")
    case ".pdf" | ".zip":
        print(f"application/{filetype[-3:]}")
    case ".pdf":
        print("text/pdf")
    case ".jpg" | "jpeg":
        print("image/jpeg")
    case ".txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
