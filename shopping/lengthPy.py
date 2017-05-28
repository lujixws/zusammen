def just_right(strVar):
    print(len(str(strVar)))
    if len(str(strVar)) < 5:
        return "Your string is too short"
    elif len(str(strVar)) > 5:
        return "your string is too long"
    else:
        return True
    
just_right("saeedd")