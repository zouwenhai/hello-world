from authenticator import Authenticator
from app.utils import Storage

platform = 'WHERE-APP'
storage = Storage()


authenticator = Authenticator(platform, storage)
