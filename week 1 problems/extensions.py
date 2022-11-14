"""
Implement a program that prompts the user for the name of a file
Outputs: File's media type if it ends with any of these suffixes
    .gif -> image/gif
    .jpg -> image/jpeg
    .jpeg -> image/jpeg
    .png -> image/png
    .pdf -> application/pdf
    .txt -> text/plain
    .zip -> application/zip
"""

def main():
    #Ask user for file name with extension
    file = input("File name: ")
    #Verify the file type using the file_type function and print it
    print(file_type(file))

def file_type(file_name):
    #Break down the string until we only have the file extension
    file_name = file_name.split(".")[1].lower().strip()
    #Check what kind of file it is using match
    match file_name:
        case "gif":
            return "image/gif"
        case "jpeg" | "jpg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"


main()