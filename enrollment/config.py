import os

class Config(object):
    #In a small app I could have it in main or init
    SECRET_KΕY = os.environ.get('SECRET_KEY') or "secret_string"
    # Signature key to make sure anything I send across server is not changed by hackers etc
    # for example cookies 
    # Secret string that will be hashed
    