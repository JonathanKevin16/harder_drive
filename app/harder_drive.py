import random
from .file_handler import FileHandler
from .encryption import Encryptor
from .conversation import Conversationalist


class HarderDrive:
    def __init__(self):
        self.file_handler = FileHandler()
        self.encryptor = Encryptor()
        self.conversationalist = Conversationalist()

    def store_file(self, filename, content):
        judgment = self.conversationalist.judge_filename(filename)

        if random.random() < 0.3:  # 30% chance of refusal
            return f"{judgment} Also, {self.conversationalist.get_refusal_message()}", False

        encrypted_content = self.encryptor.encrypt(content)
        self.file_handler.store(filename, encrypted_content)
        return f"{judgment} But {self.conversationalist.get_success_message()}", True

    def retrieve_file(self, filename):
        judgment = self.conversationalist.judge_filename(filename)

        encrypted_content = self.file_handler.retrieve(filename)
        if encrypted_content is None:
            return f"{judgment} And {self.conversationalist.get_error_message()}", None
        decrypted_content = self.encryptor.decrypt(encrypted_content)
        return judgment, decrypted_content

    def initiate_conversation(self):
        return self.conversationalist.start_conversation()