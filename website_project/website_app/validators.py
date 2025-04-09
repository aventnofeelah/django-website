from django.core.exceptions import ValidationError

#validor for profile picture (size)
def profilepictureValidator(file):
    max_file_size = 1024 * 1024 * 2
    if file.size > max_file_size: 
        raise ValidationError(f"Image size should not be larger than 2MB, Your file is {file.size / 1024 / 1024} ")

#validator for file (size, extension)
#NOT_ALLOWED_EXTENSIONS = ['mp4', 'mp3', 'mkv', 'mov', 'avi', 'mpg']
def fileValidator(file):
    max_file_size = 1024 * 1024 * 15
    if file.size > max_file_size:
        raise ValidationError(f"File size should not be larger than 15MB, Your file is {file.size / 1024 / 1024} ")
    
