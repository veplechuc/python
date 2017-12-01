"""
    comoons functions shared
"""

def banner(message, border='-'):
    """
        prints a banner
    :param message:
    :param border:
    :return:
    """
    line = border * len(message)
    print(message)
    print(line)
    return None
