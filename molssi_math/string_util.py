"""
Misc. string processing functions
"""

def title_case(sentence):
    """
    :param sentence:
        sentence tp be converted
    :return: ret: string
    :example: >>> titlecase("This iS tHe")
        This Is The
    """

    return ' '.join([i.capitalize() for i in sentence.split()])