def reverse_dict(dict):
    # swap keys and values within dict and return dict
    reverse_dict = { v : k for k, v in dict.items()}
    return reverse_dict
