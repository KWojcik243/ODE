import errno
import mimetypes
import os
from urllib import request
from django.http.response import HttpResponse
from owlready2 import *


class UserFile:
    def __init__(self, file_name, ontology):
        self.name = file_name
        self.ontology = ontology

    def create_file(self, user_name, file_name):
        self.name = file_name
        i=0
        while True:
            try:
                file_path = os.path.join("http://test.org/onto" + user_name + file_name + str(i))
                self.ontology = get_ontology(file_path)
                break
            except:
                i+=1

    def save_on_server(self, user_name):
        file_path = os.path.join(os.path.abspath(os.getcwd()), "data", user_name, "")

        if not os.path.exists(os.path.dirname(file_path)):
            try:
                os.makedirs(os.path.dirname(file_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        self.ontology.save(os.path.join(file_path, self.name), format="rdfxml")

    def load_from_server(self, user_name, file_name):
        self.name = file_name
        file_path = os.path.join(os.path.abspath(os.getcwd()), "data", user_name, file_name)
        self.ontology = get_ontology(file_path).load()

    def file_rename(self, user_name, new_file_name):
        file_path_old = os.path.join(os.path.abspath(os.getcwd()), "data", user_name, self.name)
        file_path_new = os.path.join(os.path.abspath(os.getcwd()), "data", user_name, new_file_name)
        if not os.path.exists(os.path.dirname(file_path_old)):
            self.name = new_file_name
        else:
            self.name = new_file_name
            os.rename(file_path_old, file_path_new)

    def delete_from_server(self, user_name, file_name):
        try:
            file_path = os.path.join(os.path.abspath(os.getcwd()), "data", user_name, file_name)
            os.remove(file_path)
        except:
            pass

    def download(self, user_name, file_name):
        file_path = os.path.join(os.path.abspath(os.getcwd()), "data", user_name, file_name)
        path = open(file_path, 'r')
        mime_type, _ = mimetypes.guess_type(file_path)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % self.name
        return response

    def load_from_computer(self, file):
        self.name = file.name
        self.ontology = ""
        self.save_on_server(file.name)
        with open(file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
