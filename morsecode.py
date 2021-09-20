from playsound import playsound
from time import sleep


class MorseCode:

    morsecode_dict = {
        "a": ".-", "b": "-...", "c": "-.-.",
        "d": "-..", "e": ".", "f": "..-.",
        "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---",
        "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-",
        "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "--..--", "?": "..--..",
        "'": ".----.", "!": "-.-.--", "/": "-..-.",
        "(": "-.--.", ")": "-.--.-", "&": ".-...",
        ":": "---...", ";": "-.-.-.", "=": "-...-",
        "+": ".-.-.", "-": "-....-", "_": "..--.-",
        '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
        "¿": "..-.-", "¡": "--...-", "start": "-.-.-",
        "end": "...-.-", " ": "/", "\n": ".-.-", }

    my_dict = {}

    @staticmethod
    def _add_dict(a: dict, b: dict):
        foo = a
        for k, v in b.items():
            if k not in a:
                foo[k] = v
        return foo

    @classmethod
    def encode_dict(cls) -> dict:
        return cls._add_dict(cls.morsecode_dict, cls.my_dict)

    @classmethod
    def decode_dict(cls) -> dict:
        foo = {}
        encode_dict = cls.encode_dict()
        for k, v in encode_dict.items():
            foo[v] = k
        return foo

    @classmethod
    def encode(cls, txt: str) -> str:
        encode_dict = cls.encode_dict()
        return " ".join([encode_dict[i] for i in txt.lower()])

    @classmethod
    def decode(cls, txt: str) -> str:
        decode_dict = cls.decode_dict()
        return "".join([decode_dict[i] for i in txt.split(" ")])

    @classmethod
    def play(cls, txt: str, signals=False) -> None:
        meta = {
            ".": ("dot.wav", 0.05),
            "-": ("dash.wav", 0.1),
            "/": ("space.wav", 0.0),
        }
        if "".join("".join("".join("".join(txt.split(" ")).split('/')).split(".")).split("-")) == "":
            def func(*args): return txt
        else:
            func = cls.encode
        if signals:
            cls.play(cls.encode_dict["start"] + "/")
        for i in func(txt) + "/":
            if i == " ":
                sleep(0.3)
            elif i == "\n":
                pass
            else:
                playsound(meta[i][0])
                sleep(meta[i][1])
        if signals:
            cls.play(cls.encode_dict["end"] + "/")


if __name__ == "__main__":
    pass
