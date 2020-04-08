import markovify

def speak():
    with open("speeches.csv",encoding='UTF-8') as f:
        text = f.read()
    model = markovify.Text(text)
    return model.make_short_sentence(100)
