class alphabet():
    def __init__(self, lang, letters):
     self.lang = lang
     self.letters = letters

    def printing_letters(self):
        print(self.letters)

    def letters_num (self):
        return(len(self.letters))
class ENGalphabet(alphabet):
    def __init__ (self, lang, letters):
        super().__init__(lang, letters)
    def letters_num (self):
        return(len(self.letters))
    def is_en_letters (self, letters):
        return letters in self.letters
    @staticmethod
    def example():
        return "Chicago is a vibrant and diverse city located in the Midwest region of the United States."

language2= ENGalphabet('англйиский', 'abcdefghijklmnopqrstuvwxyz')
#Тесты
print(language2.letters)
print(language2.is_en_letters('f'))
print(language2.is_en_letters('ш'))
print(language2.example())
print(language2.letters_num())
