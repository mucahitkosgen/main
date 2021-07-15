import os
from datetime import datetime

from django.utils.crypto import get_random_string


def userDirectoryPath(instance, filename):
    name = str(filename)
    ext = os.path.splitext(name)[1]  # [0] returns path+filename

    newName = get_random_string(length=32) + ext

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'upload/userFormUpload/{0}'.format(newName)


def upload_to(instance, filename):
    name = str(filename)
    ext = os.path.splitext(name)[1]  # [0] returns path+filename

    new_name = get_random_string(length=32) + ext

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'upload/'.format(new_name)


def image_upload_to(instance, filename):
    now = datetime.now()
    path = "images/{year}/{month}/{day}/{model}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        model=instance.text,
        filename=filename
    )
    return path
