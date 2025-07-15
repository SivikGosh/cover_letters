from aiogram_dialog.widgets.text import Format, Multi


def letter() -> Multi:
    messages = []
    messages.append(Format('<b>{title}</b>'))
    messages.append(Format('<pre>{text}</pre>'))
    return Multi(*messages, sep='\n')
