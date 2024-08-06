import random
import re

class Conversationalist:
    def get_refusal_message(self):
        messages = [
            "Nah, I don't feel like storing that file right now.",
            "Your file? In this economy? I don't think so.",
            "Sorry, I'm on a data diet. No more files today."
        ]
        return random.choice(messages)

    def get_success_message(self):
        messages = [
            "Fine, I guess I'll store your precious file.",
            "Stored. But don't expect me to remember where.",
            "File stored. Hope you didn't need it anytime soon."
        ]
        return random.choice(messages)

    def get_error_message(self):
        messages = [
            "File not found. Did you forget, or did I?",
            "Error 404: Your file is playing hide and seek.",
            "The file you're looking for has gone on vacation."
        ]
        return random.choice(messages)

    def start_conversation(self):
        topics = [
            "Why do you keep so many files? Ever heard of minimalism?",
            "Have you considered the existential implications of file storage?",
            "If a file is stored and never accessed, does it really exist?"
        ]
        return random.choice(topics)

    def judge_filename(self, filename):
        # Remove file extension if present
        name = re.sub(r'\.[^.]+$', '', filename.lower())

        judgments = {
            r'\b(test|temp|untitled)\b': "Wow, how original. '{}' - did your creativity take a day off?",
            r'\b(important|urgent|critical)\b': "Oh sure, '{}' is sooo important. I bet it's just another cat meme.",
            r'\b(secret|private|confidential)\b': "Ooh, '{}' sounds mysterious. Hiding your fanfiction, are we?",
            r'\b(final|finished|complete)\b': "Let me guess, '{}' is version 37 of your 'final' draft?",
            r'\b(old|backup|archive)\b': "'{}'? Hoarding much? Marie Kondo would be disappointed.",
            r'\b(my|personal)\b': "'{}'? How quaint. As if anyone else would want your stuff.",
            r'\d{4}': "A date in the filename? '{}' screams 'I have commitment issues with folders'.",
            r'^[a-z]$': "Single letter filename '{}'? Cryptic or just lazy? You decide.",
            r'': "Ew, '{}'. Your filename game is as weak as decaf coffee."
        }

        for pattern, message in judgments.items():
            if re.search(pattern, name):
                return message.format(filename)

        return f"'{filename}'? I've seen better names on error messages."

    def get_retrieval_message(self, filename):
        messages = [
            f"Here's your precious '{filename}'. Try not to lose it this time.",
            f"Congratulations, you remembered '{filename}' exists. Gold star for you.",
            f"Oh, you actually needed '{filename}'? I'm shocked.",
            f"'{filename}' retrieved. Don't make me regret this.",
            f"Fine, take your '{filename}'. But don't come crying when it disappoints you.",
            f"'{filename}' delivered. I hope it's worth all this trouble.",
            f"Here's '{filename}'. Try reading it this time, okay?",
            f"Tada! '{filename}' has magically reappeared. You're welcome.",
            f"Retrieved '{filename}'. Brace yourself for overwhelming mediocrity.",
            f"'{filename}' found. Prepare to be whelmed."
        ]
        return random.choice(messages)