"""
    In this example, we'll add a timestamp at the start of the image name, and an uuid at the 
    end.

    To do this, we'll make a function that generates the name, and pass it to the upload_to
    param of the image field.
"""

def upload_destination(instance, filename):
    ext = filename.split('.')[-1] 
    name = filename.split('.')[0]
    ts = str(time.time()).replace('.', '') # Timestamp with milliseconds
    finalname = f"postImages/{name}_{uuid4()}_{ts}.{ext}"

    return finalname


class Post(models.Model):

    image = models.ImageField(
        upload_to=upload_destination, 
        null=True, 
        validators=[
            image_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ]
    )


"""
    NOTE: Timestamp only is not ideal, because of there can be 2 requests at the same 
    millisecond with the same filename. The soluton is to also generate an uuid everytime.

    It could have been just the uuid, but with the timestamps in order, we can sort the files 
    by date


    Example of filename generated:

        name        uuid                                 timestamp         extension
        hellknights_fdeb5b1e-cddb-40a6-a9d2-2741e1ab4752_16135823006483839.png
"""
