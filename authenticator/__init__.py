from django.core import signing

signer = signing.TimestampSigner()


class Authenticator:
    PLATFORM_TYP = None
    storage = None

    def __init__(self, platform, storage):
        self.platform = platform
        self.storage = storage

    def __set_sign(self, user_id, sign):
        self.storage.set(user_id, sign)

    def __get_sign(self, user_id):
        return self.storage.get(user_id)

    def __clear_sign(self, user_id):
        self.storage.clear(user_id)

    def gen_sign(self, user_id):
        signature = self.__get_sign(user_id)
        if signature:
            return signature
        signature = signer.sign(user_id)
        self.__set_sign(user_id, signature)
        return signature

    def sign_to_user_id(self, signture):
        user_id = signer.unsign(signture)
        now_signture = self.__get_sign(user_id)
        if now_signture and signture == now_signture:
            return user_id

    def clear_sign(self, user_id):
        self.__clear_sign(user_id)
