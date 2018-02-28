from authenticator import Authenticator
from .utils import Storage

platform = 'WHERE-APP'
storage = Storage()


authenticator = Authenticator(platform, storage)
