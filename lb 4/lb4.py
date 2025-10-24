def list_benefits():
    return [
        "Більш організований код",
        "Більш читабельний код",
        "Легше повторне використання коду",
        "Можливість програмістам ділитися та поєднувати код"
    ]
def build_sentence(benefit):
    return f"{benefit} є перевагою використання функцій!"
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
name_the_benefits_of_functions()
