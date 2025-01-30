"Scrollspy Example" 

from fasthtml.common import *
from monsterui.all import *

# Using the "slate" theme with Highlight.js enabled
hdrs = Theme.slate.headers(highlightjs=True)
app, rt = fast_app(hdrs=hdrs)

################################
### Example Data and Content ###
################################
products = [
    {"name": "Laptop", "price": "$999", "img": "https://picsum.photos/400/100?random=1"},
    {"name": "Smartphone", "price": "$599", "img": "https://picsum.photos/400/100?random=2"}
]

code_example = """
# Python Code Example
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
                    """
testimonials = [
    {"name": "Alice", "feedback": "Great products and excellent customer service!", "img": "https://picsum.photos/100?random=11"},
    {"name": "Bob", "feedback": "Fast shipping and amazing quality!", "img": "https://picsum.photos/100?random=12"},
    {"name": "Charlie", "feedback": "Amazing experience! Will definitely buy again.", "img": "https://picsum.photos/100?random=13"},
    {"name": "Diana", "feedback": "Affordable prices and great variety!", "img": "https://picsum.photos/100?random=14"},
    {"name": "Edward", "feedback": "Customer support was very helpful.", "img": "https://picsum.photos/100?random=15"},
    {"name": "Fiona", "feedback": "Loved the design and quality!", "img": "https://picsum.photos/100?random=16"}
]


# Team members
team = [
    {"name": "John Doe", "role": "CEO", "img": "https://picsum.photos/100?random=1"},
    {"name": "Jane Smith", "role": "CTO", "img": "https://picsum.photos/100?random=2"},
    {"name": "Josh Patterson", "role": "AI Researcher", "img": "https://picsum.photos/100?random=3"},
    {"name": "Jason Liu", "role": "ML Engineer", "img": "https://picsum.photos/100?random=4"},
    {"name": "Hamel Husain", "role": "Data Scientist", "img": "https://picsum.photos/100?random=5"},
    {"name": "Shreya Shankar", "role": "Software Engineer", "img": "https://picsum.photos/100?random=6"},
    {"name": "Luke Johnson", "role": "Product Manager", "img": "https://picsum.photos/100?random=7"},
    {"name": "Greg Thomas", "role": "Backend Developer", "img": "https://picsum.photos/100?random=8"},
    {"name": "Emily Davis", "role": "UX Designer", "img": "https://picsum.photos/100?random=9"},
    {"name": "Robert Brown", "role": "DevOps Engineer", "img": "https://picsum.photos/100?random=10"},
    {"name": "Laura Wilson", "role": "Security Analyst", "img": "https://picsum.photos/100?random=11"},
    {"name": "Michael Carter", "role": "Full Stack Developer", "img": "https://picsum.photos/100?random=12"},
    {"name": "Sophie Martin", "role": "Cloud Architect", "img": "https://picsum.photos/100?random=13"},
    {"name": "Daniel White", "role": "Blockchain Expert", "img": "https://picsum.photos/100?random=14"},
    {"name": "Olivia King", "role": "AI Ethics Researcher", "img": "https://picsum.photos/100?random=15"}
]


def ProductCard(p):
    return Card(Img(src=p["img"], alt=p["name"], style="width:100%"), H4(p["name"], cls="mt-2"), P(p["price"], cls=TextT.bold+TextT.sm), Button("Details", cls=(ButtonT.primary, "mt-2")))

def TestimonialCard(t):
    return Card(Img(src=t["img"], cls="rounded-circle", width="50", height="50"), H4(t["name"], cls="mt-2"), P(t["feedback"]), cls="p-3 shadow-sm rounded")

def TeamCard(m): return Card(Img(src=m["img"], alt=m["name"], style="width:50px;border-radius:50%"), H4(m["name"], cls="mt-2"), P(m["role"]))

################################
### Navigation and Scrollspy ###
################################

scrollspy_links = (
                Li(A("Welcome",      href="#welcome-section")),
                Li(A("Products",     href="#products-section")),
                Li(A("Testimonials", href="#testimonials-section")), 
                Li(A("Team",         href="#team-section")),
                Li(A("Code Example", href="#code-section")))
@rt
def index():
    return Container(
        NavBar(
            nav_links=scrollspy_links,
            title=DivLAligned(H3("Scrollspy Demo!"),UkIcon('rocket',height=30,width=30)),
            sticky=True, uk_scrollspy_nav=True),
        NavContainer(
            *scrollspy_links,
            uk_scrollspy_nav=True,
            sticky=True,
            cls=(NavT.primary,'pt-20 px-5 pr-10')),
        Container(
            # Notice the ID of each section corresponds to the `scrollspy_links` dictionary
            # So in scollspy `NavContainer` the `href` of each `Li` is the ID of the section
            Section(H1("Welcome to the Store!"), P("Explore our products and enjoy dynamic code examples."),id="welcome-section"),
            Section(H2("Products"), Grid(*[ProductCard(p) for p in products], cols_lg=2),                   id="products-section"),
            Section(H2("Testimonials"), Grid(*[TestimonialCard(t) for t in testimonials], cols_lg=2),       id="testimonials-section"),
            Section(H2("Our Team"), Grid(*[TeamCard(m) for m in team], cols_lg=2),                          id="team-section"),
            Section(H2("Code Example"), CodeBlock(code_example, lang="python"),                             id="code-section")), 
            cls=(ContainerT.xl,'uk-container-expand'))

serve()
