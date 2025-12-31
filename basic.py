r"""
Tokens:Token are the smallest part/meaning of anything in our case or programming anything can be tokens or basically every things are made of tokens:

ex: Shakeeb Shaikh is my name and let's take the name 'Shakeeb Shaikh' this name comprises of 13 tokens each and evry letter is a token 'S','h','a','k','e','e','b','S','h','a','i','k','h' => this name is made of 13 token in the similar way programming languages breaks every thing in tokens to have a complete understanding what does the user/person working on the computer wants


Note:for docs refer to this repo and docs
https://github.com/ShakeebSk/build-your-own-x?tab=readme-ov-file#build-your-own-programming-language

https://ruslanspivak.com/lsbasi-part1/




"""


class Token:
    r"""
    The init function have 2 parameters
    1.type -> which means what is the type of the current token like INTEGER, PLUS, or EOF
    2.value -> 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
    """

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    r""" 
    The representation function is used for representing something on the the CLI like [INT:356] like this as it will look better in the CLI and if there is value to the type other wise it will just return the type of the token like this [INT] 
    """

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

    def interpreter(self):
        pass

    def __str__(self):
        pass


class Interpreter:

    pass
    r"""
    
    """


# if __name__ == "main":
# main()
