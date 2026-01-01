extensions=[
"gif",
"jpg",
"jpeg",
"png",
"pdf",
"txt",
"zip"
]

type={
 "gif" : "image/gif",
 "jpg" : "image/jpeg",
 "jpeg": "image/jpeg",
 "png" : "image/png",
 "pdf" : "application/pdf ",
 "txt" : "text/plain",
 "zip" : "application/zip"
}


def file_type(file_name):
    name=file_name.strip().lower()
    name=name.split(".")
    name=name[-1]
    if name in type:
        return type[name]
    else:
        return "application/octet-stream"



def main():
    file_name=input("File name : ")

    print(file_type(file_name))


main()
