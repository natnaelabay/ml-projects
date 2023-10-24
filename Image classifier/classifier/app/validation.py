def isValidFile(file):
    ALLOWED_EXTENSIONS = {"png","jpg","jpeg"}
    
    if file is None or file.filename == "":
        return "Image not specified"
    if "." not in file.filename or file.filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
        return "File format not supported"
    
    return False
    