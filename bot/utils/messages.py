from aiogram_dialog.widgets.text import Const, Format, Multi


def letter() -> Multi:
    messages = []
    messages.append(Format('<b>{title}</b>'))
    messages.append(Format('<pre>{text}</pre>'))
    return Multi(*messages, sep='\n')


def letter_saved() -> Const:
    return Const('✅ Письмо сохранено.\n')
