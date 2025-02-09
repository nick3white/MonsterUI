from fasthtml.common import *
import fasthtml.common as fh
from monsterui.all import *
from monsterui.foundations import *

# scrollspy_css = ".navbar a.uk-active { text-decoration: underline; }"
# .monster-navbar.navbar-underline a.uk-active { border-bottom: 2px solid currentColor; }

scrollspy_style=Style('''
.monster-navbar.navbar-bold a {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.monster-navbar.navbar-bold a.uk-active {
    transform: scale(1.15) ;
    font-weight: bold;
    text-shadow: 0 0 12px rgba(var(--p-rgb), 0.4);
    letter-spacing: 0.02em;
    color: hsl(var(--p) / 1);
}
.monster-navbar.navbar-underline a.uk-active { position: relative; }
.monster-navbar.navbar-underline a.uk-active::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 100%;
    height: 2px;
    background: currentColor;
    animation: slideIn 0.3s ease forwards;
}
@keyframes slideIn {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
}
''')

class ScrollspyT(VEnum):
    underline = 'navbar-underline'
    bold = 'navbar-bold'

app, rt = fast_app(hdrs=(Theme.blue.headers(highlightjs=True), Style(scrollspy_style)))





def NavBar(*c,
           right_cls='space-x-4',
           mobile_cls='space-y-4',
           brand=H3("Title"), # Brand/logo component for left side
           sticky:bool=False, # Whether to stick to the top of the page while scrolling
           uk_scrollspy_nav:bool|str=False, # Whether to use scrollspy for navigation
           cls='p-4', # Classes for navbar
           scrollspy_cls=ScrollspyT.underline, # Scrollspy class (usually ScrollspyT.*)
           menu_id=None, # ID for menu container (used for mobile toggle)
           ):
    "Creates a responsive navigation bar with mobile menu support"
    if menu_id is None: menu_id = unqid()
    sticky_cls = 'sticky top-4 bg-base-100/80 backdrop-blur-sm z-50' if sticky else ''
    if uk_scrollspy_nav == True: uk_scrollspy_nav = 'closest: a; scroll: true'

    mobile_icon = A(UkIcon("menu", width=30, height=30), cls="md:hidden", data_uk_toggle=f"target: #{menu_id}; cls: hidden")
    return Div(
        Div(
            DivFullySpaced(
                brand, # Brand/logo component for left side
                mobile_icon, # Hamburger menu icon
                Div(*c,cls=(stringify(right_cls),'hidden md:flex'), uk_scrollspy_nav=uk_scrollspy_nav)),# Desktop Navbar (right side)
            cls=('monster-navbar', stringify(cls), stringify(scrollspy_cls))
            ),
        DivCentered(*c, 
                    cls=(stringify(mobile_cls),'hidden md:hidden monster-navbar p-4', stringify(scrollspy_cls)), 
                    id=menu_id, uk_scrollspy_nav=uk_scrollspy_nav),
        cls=sticky_cls)


@rt
def basic():
    "Basic navbar with brand and links"
    return NavBar(
        *map(A, ["Home", "About", "Contact"]),
        brand=H3("MyApp", href="/"),)

@rt 
def login():
    "Navbar with brand and login button"
    return NavBar(
        Button("Login", cls=ButtonT.primary),
        brand=DivHStacked(
            UkIcon('rocket', height=24),
            Strong("RocketApp", cls=TextT.lg)))

@rt
def search():
    "Navbar with search functionality"
    return NavBar(
        Input(placeholder="Search...", cls="input-sm"),
        UkIconLink('search', button=True, cls=ButtonT.ghost),
        brand=H3("SearchApp")
    )

@rt
def admin():
    "Dark themed navbar with avatar"
    return NavBar(
        *map(A, ["Dashboard", "Settings"]),
        DiceBearAvatar("John Doe", h=6, w=6),
        brand=H3("AdminApp"),
        cls="bg-neutral text-neutral-content p-4"
    )

@rt
def ecommerce():
    "E-commerce style navbar"
    return NavBar(
        *map(A, ["Categories", "Deals"]),
        UkIconLink('shopping-cart', button=True),
        Button("Sign Up", cls=ButtonT.primary),
        brand=DivHStacked(
            UkIcon('shopping-bag', height=24),
            Strong("ShopApp", cls=TextT.lg)
        )
    )

@rt
def minimal():
    "Minimal navbar with just icons"
    return NavBar(
        UkIconLink('home', button=True, cls=ButtonT.ghost),
        UkIconLink('bell', button=True, cls=ButtonT.ghost),
        UkIconLink('settings', button=True, cls=ButtonT.ghost),
        brand=UkIcon('zap', height=24)
    )

@rt
def index():
    "Shows all navbar examples"
    return Div(
        H1("Navbar Examples"),
        Div(H2("Basic Navbar"), basic()),
        Div(H2("Login Navbar"), login()),
        Div(H2("Search Navbar"), search()),
        Div(H2("Admin Navbar"), admin()),
        Div(H2("E-commerce Navbar"), ecommerce()),
        Div(H2("Minimal Navbar"), minimal()),
        cls='space-y-8'
    )



"MonsterUI Scrollspy Example application" 

import random

# Using the "slate" theme with Highlight.js enabled
# hdrs = Theme.slate.headers(highlightjs=True)
# app, rt = fast_app(hdrs=hdrs)

################################
### Example Data and Content ###
################################
products = [
    {"name": "Laptop", "price": "$999"},
    {"name": "Smartphone", "price": "$599"}
]

code_example = """
# Python Code Example
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b:
        return a / b
    return "Cannot divide by zero!"

def fibonacci(n):
    if n <= 0:
        return "Fibonacci sequence starts from 1"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")  # When in doubt, divide by zero
    print(f"Fibonacci(5) = {fibonacci(5)}")

if __name__ == "__main__":
    main()
"""
testimonials = [
    {"name": "Alice", "feedback": "Great products and excellent customer service!"},
    {"name": "Bob", "feedback": "Fast shipping and amazing quality!"},
    {"name": "Charlie", "feedback": "Amazing experience! Will definitely buy again."},
    {"name": "Diana", "feedback": "Affordable prices and great variety!"},
    {"name": "Edward", "feedback": "Customer support was very helpful."},
    {"name": "Fiona", "feedback": "Loved the design and quality!"}
]

# Team members
team = [
    {"name": "Isaac Flath", "role": "CEO"},
    {"name": "Benjamin Clavié", "role": "AI Researcher"},
    {"name": "Alexis Gallagher", "role": "ML Engineer"},
    {"name": "Hamel Husain", "role": "Data Scientist"},
    {"name": "Austin Huang", "role": "Software Engineer"},
    {"name": "Benjamin Warner", "role": "Product Manager"},
    {"name": "Jonathan Whitaker", "role": "UX Designer"},
    {"name": "Kerem Turgutlu", "role": "DevOps Engineer"},
    {"name": "Curtis Allan", "role": "DevOps Engineer"},
    {"name": "Audrey Roy Greenfeld", "role": "Security Analyst"},
    {"name": "Nathan Cooper", "role": "Full Stack Developer"},
    {"name": "Jeremy Howard", "role": "CTO"},
    {"name": "Wayde Gilliam", "role": "Cloud Architect"},
    {"name": "Daniel Roy Greenfeld", "role": "Blockchain Expert"},
    {"name": "Tommy Collins", "role": "AI Ethics Researcher"}
]


def ProductCard(p):
    return Card(
        PicSumImg(w=500, height=100, id=random.randint(1, 20)),
        DivFullySpaced(H4(p["name"]), P(Strong(p["price"], cls=TextT.sm))), 
        Button("Details", cls=(ButtonT.primary, "w-full")))

def TestimonialCard(t):
    return Card(
        DivLAligned(PicSumImg(w=50, h=50, cls='rounded-full', id=random.randint(1, 20)), H4(t["name"])), 
        P(Q((t["feedback"]))))


def TeamCard(m): 
    return Card(
        DivLAligned(
            PicSumImg(w=50, h=50, cls='rounded-full', id=random.randint(1, 20)), 
            Div(H4(m["name"]), P(m["role"]))),
        cls='p-3')

################################
### Navigation and Scrollspy ###
################################

scrollspy_links = (
                A("Welcome",      href="#welcome-section"),
                A("Products",     href="#products-section"),
                A("Testimonials", href="#testimonials-section"), 
                A("Team",         href="#team-section"),
                A("Code Example", href="#code-section"))



@rt
def scrollspy():
    def _Section(*c, **kwargs): return Section(*c, cls='space-y-3', **kwargs)
    return Container(
        NavBar(
            *scrollspy_links,
            brand=DivLAligned(H3("Scrollspy Demo!"),UkIcon('rocket',height=30,width=30)),
            sticky=True, uk_scrollspy_nav=True,
            scrollspy_cls=ScrollspyT.bold),
        NavContainer(
            *(map(Li,scrollspy_links)),
            uk_scrollspy_nav=True,
            sticky=True,
            cls=(NavT.primary,'pt-20 px-5 pr-10')),
        Container(
            # Notice the ID of each section corresponds to the `scrollspy_links` dictionary
            # So in scollspy `NavContainer` the `href` of each `Li` is the ID of the section
            DivCentered(
                H1("Welcome to the Store!"), 
                Subtitle("Explore our products and enjoy dynamic code examples."), 
                id="welcome-section"),
            _Section(H2("Products"),
                     Grid(*[ProductCard(p) for p in products], cols_lg=2),                   
                     id="products-section"),
            _Section(H2("Testimonials"), 
                     Slider(*[TestimonialCard(t) for t in testimonials]),       
                     id="testimonials-section"),
            _Section(H2("Our Team"), 
                     Grid(*[TeamCard(m) for m in team], cols_lg=2, cols_max=3),                          
                     id="team-section"),
            _Section(H2("Code Example"), 
                     CodeBlock(code_example, lang="python"),                             
                     id="code-section")), 
            cls=(ContainerT.xl,'uk-container-expand'))


@rt
def theme():
    return ThemePicker()
serve()