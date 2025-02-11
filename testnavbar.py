from fasthtml.common import *
from monsterui.all import *
hdrs = Theme.blue.headers(mode='light')
app, rt = fast_app(hdrs=hdrs, live=True)
@rt
def index():
    return Title('Hello World'), Container(
        H2(A('Pretty URL', href='', cls=AT.primary)),
        P('I love monsterui!'),
        A('Go to Google', href='https://google.com', cls=AT.classic),
        Card('A Fancy Card :)')
    )


serve()