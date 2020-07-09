import os
from faker import Faker

def mk_dir(path):
    """ Creates folder if it does not exist. Return is_dir (True/False). """
    is_dir = os.path.isdir(path)
    if not is_dir:
        print('Creating dir: ' + path)
        os.mkdir(path)
    return is_dir

def generate_model_name():
    """ Generate a random name for model """
    fake = Faker()
    model_name = fake.name().replace(" ", "_")
    return model_name
