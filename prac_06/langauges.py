"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""
# Note that the import has a folder (module) in it.



from prac_06.programming_language import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are")
    for language in languages:
        if language.typing == "Dynamic":
            print(language.name)


main()