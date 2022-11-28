import random
import string
import os
import base64


class File(object):

    @classmethod
    def get_new_file_name_with_extenstion(cls, filename):
        extention = filename.split('.')[-1]
        new_file_name = filename[:(len(filename) - len(extention) - 1)] + \
            File.get_random_string() + '.' + extention
        return new_file_name, extention

    @classmethod
    def get_random_string(cls, length=30):
        letters = string.ascii_letters + string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @classmethod
    def upload_file(cls, file_name, file, base_dir, extention):
        file_path = os.path.join(
            base_dir, file_name)
        with open(file_path + '.' + extention, 'wb+') as destination:
            destination.write(base64.decodebytes(file.encode('ascii')))
        return file_path, file_name
