# FileHandlingDjango
This repository is about how to handle all types of file in django

## Notes about File Handling in Django

- Uploaded files are placed in `request.FILES`, which is a dictionary.
- `request.FILES` dictionay key is the name from the `<input type="file" name="key_name" />` and value is the UploadedFile instance.
- HTML form must have the attribute `enctype="multipart/form-data"` and sbmitted `method=POST`
- Django provide model fields to handle uploaded files: `FileField` and `ImageField`.
- The files uploaded to `FileField` or `ImageField` are not stored in the database but in the filesystem and field contains the path where files saved.
- By deleting model we can not delete saved file, they reamin physically.
