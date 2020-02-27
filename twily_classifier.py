from textblob.classifiers import NaiveBayesClassifier


def trainer():
    train = [
        ("i am good", "pos"),
        ("fine thanks", "pos"),
        ("doing ok", "pos"),
        ("thank you", "pos"),
        ("i am crappy", "neg"),
        ("omg", "neg"),
        ("wtf", "neg"),
        ("no thanks", "pos"),
        ("do you have information on the SDK", "pos"),
        ("not good", "neg"),
        ("you are awesome", "pos"),
        ("i don't know", "neg"),
        ("ass hole", "neg"),
        ("fucker", "neg"),
        ("it didn't answer my question", "neg"),
        ("screw you", "neg"),
        ("you rule", "pos"),
        ("fuck you", "neg"),
        ("i want to talk to a rep", "neg"),
        ("give me info on twilio whatsapp", "pos"),
        ("get me your boss", "neg"),
        ("help me with", "pos"),
        ("get me a rep", "neg"),
        ("you're kind", "pos"),
        ("what do you know", "neg"),
        ("i need assistance with", "pos"),
        ("this is crap", "neg"),
        ("contact us", "pos"),
        ("the python helper library", "pos"),
        ("live help", "neg"),
        ("tutorial", "pos"),
        ("no", "neg"),
        ("twilio api for whatsapp", "pos"),
        ("twilio autopilot", "pos"),
        ("what is twilio whatsapp api", "pos"),
        ("is that so", "neg"),
        ("you suck", "neg"),
        ("yes", "pos"),
        ("this is not working", "neg")
            ]

    return NaiveBayesClassifier(train)


if __name__ == "__main__":
    """ you could make the testing a bit more flexible if you allow 
    the string to be passed as an argument. Then you can show the positive 
    and negative probabilities of several example sentences."""
    
    classy = trainer().prob_classify("I didn't find this helpful")
    print(f'Probability of being negative: {round(classy.prob("neg"), 2)}')
