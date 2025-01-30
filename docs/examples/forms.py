"""FrankenUI Forms Example built with MonsterUI (original design by ShadCN)"""


from fasthtml.common import *
from monsterui.all import *
from fasthtml.svg import *

app, rt = fast_app(hdrs=Theme.blue.headers())

def HelpText(c):
    return P(c,cls=TextPresets.muted_sm)

def heading():
    return Div(cls="space-y-5")(
            H2("Settings"),
            P("Manage your account settings and set e-mail preferences.", cls=TextT.muted + TextT.lg),
            DividerSplit())

sidebar_items = ["Profile", "Account", "Appearance", "Notifications", "Display"]

sidebar = NavContainer(*map(lambda x: Li(A(x)),sidebar_items),
                uk_switcher="connect: #component-nav; animation: uk-animation-fade",
                cls=(NavT.secondary,"space-y-4 p-4 w-1/5"))


def FormSectionDiv(*c, cls='space-y-2', **kwargs): return Div(*c, cls=cls, **kwargs)
def profile_form():
    content = (FormSectionDiv(
            LabelInput("Username", placeholder='sveltecult', id='username'),
            HelpText("This is your public display name. It can be your real name or a pseudonym. You can only change this once every 30 days.")),
        FormSectionDiv(
            LabelUkSelect(Option("Select a verified email to display", value="", selected=True, disabled=True),
                     *map(Option,('m@example.com', 'm@yahoo.com', 'm@cloud.com')),  
                     label="Email", id="email"),
            HelpText("You can manage verified email addresses in your email settings.")),
        FormSectionDiv(
            LabelTextArea("Bio", id="bio", placeholder="Tell us a little bit about yourself"),
            HelpText("You can @mention other users and organizations to link to them."),
            Div("String must contain at least 4 character(s)", cls="text-destructive")),
        FormSectionDiv(
            FormLabel("URLs"),
            HelpText("Add links to your website, blog, or social media profiles."),
            Input(value="https://www.franken-ui.dev"),
            Input(value="https://github.com/sveltecult/franken-ui"),
            Button("Add URL")))
    
    return UkFormSection('Profile', 'This is how others will see you on the site.', button_txt='Update profile', *content)

def account_form():
    content = (
        FormSectionDiv(
            LabelInput("Name", placeholder="Your name", id="name"),
            HelpText("This is the name that will be displayed on your profile and in emails.")),
        FormSectionDiv(
            LabelInput("Date of Birth", type="date", placeholder="Pick a date", id="date_of_birth"),
            HelpText("Your date of birth is used to calculate your age.")),
        FormSectionDiv(
            LabelUkSelect(*Options("Select a language", "English", "French", "German", "Spanish", "Portuguese", selected_idx=1, disabled_idxs={0}),
                          label='Language', id="language"),
            HelpText("This is the language that will be used in the dashboard.")))
    
    return UkFormSection('Account', 'Update your account settings. Set your preferred language and timezone.', button_txt='Update profile', *content)

def appearance_form():
    content = (
        FormSectionDiv(
            LabelUkSelect(*Options('Select a font family', 'Inter', 'Geist', 'Open Sans', selected_idx=2, disabled_idxs={0}),
            label='Font Family', id='font_family'), 
            HelpText("Set the font you want to use in the dashboard.")),
        FormSectionDiv(
            FormLabel("Theme"),
            HelpText("Select the theme for the dashboard."),
            Grid(A(id="theme-toggle-light", cls="block cursor-pointer items-center rounded-md border-2 border-muted p-1 ring-ring")(
                    Div(cls="space-y-2 rounded-sm bg-[#ecedef] p-2")(
                        Div(cls="space-y-2 rounded-md bg-white p-2 shadow-sm")(
                            Div(cls="h-2 w-[80px] rounded-lg bg-[#ecedef]"),
                            Div(cls="h-2 w-[100px] rounded-lg bg-[#ecedef]")),
                        Div(cls="flex items-center space-x-2 rounded-md bg-white p-2 shadow-sm")(
                            Div(cls="h-4 w-4 rounded-full bg-[#ecedef]"),
                            Div(cls="h-2 w-[100px] rounded-lg bg-[#ecedef]")),
                        Div(cls="flex items-center space-x-2 rounded-md bg-white p-2 shadow-sm")(
                            Div(cls="h-4 w-4 rounded-full bg-[#ecedef]"),
                            Div(cls="h-2 w-[100px] rounded-lg bg-[#ecedef]")))),
                A(id="theme-toggle-dark", cls="block cursor-pointer items-center rounded-md border-2 border-muted bg-popover p-1 ring-ring")(
                    Div(cls="space-y-2 rounded-sm bg-slate-950 p-2")(
                        Div(cls="space-y-2 rounded-md bg-slate-800 p-2 shadow-sm")(
                            Div(cls="h-2 w-[80px] rounded-lg bg-slate-400"),
                            Div(cls="h-2 w-[100px] rounded-lg bg-slate-400")),
                        Div(cls="flex items-center space-x-2 rounded-md bg-slate-800 p-2 shadow-sm")(
                            Div(cls="h-4 w-4 rounded-full bg-slate-400"),
                            Div(cls="h-2 w-[100px] rounded-lg bg-slate-400")),
                        Div(cls="flex items-center space-x-2 rounded-md bg-slate-800 p-2 shadow-sm")(
                            Div(cls="h-4 w-4 rounded-full bg-slate-400"),
                            Div(cls="h-2 w-[100px] rounded-lg bg-slate-400")))),
            cols_max=2,cls=('max-w-md','gap-8'))))
    
    return UkFormSection('Appearance', 'Customize the appearance of the app. Automatically switch between day and night themes.', button_txt='Update preferences', *content)


notification_items = [
    {"title": "Communication emails", "description": "Receive emails about your account activity.", "checked": False, "disabled": False},
    {"title": "Marketing emails", "description": "Receive emails about new products, features, and more.", "checked": False, "disabled": False},
    {"title": "Social emails", "description": "Receive emails for friend requests, follows, and more.", "checked": True, "disabled": False},
    {"title": "Security emails", "description": "Receive emails about your account activity and security.", "checked": True, "disabled": True}]

def notifications_form():
    def RadioLabel(label): return DivLAligned(Radio(name="notification", checked=(label=="Nothing")), FormLabel(label))

    def NotificationCard(item):
        return Card(
            Div(cls="space-y-0.5")(
                FormLabel(item['title'], cls=TextPresets.bold_sm),
                HelpText(item['description'])),
        )
    content = Div(
        FormSectionDiv(
            FormLabel("Notify me about"),
            *map(RadioLabel, ["All new messages", "Direct messages and mentions", "Nothing"])),
        Div(
            H4("Email Notifications", cls="mb-4"),
            Grid(*map(NotificationCard, notification_items), cols=1)),
            LabelCheckboxX("Use different settings for my mobile devices", id="notification_mobile"),
            HelpText("You can manage your mobile notifications in the mobile settings page."))
    
    return UkFormSection('Notifications', 'Configure how you receive notifications.', 
                         *content, button_txt="Update notifications")

def display_form():
    content = (
        Div(cls="space-y-2")(
            Div(cls="mb-4")(
                Span("Sidebar", cls="text-base font-medium"),
                HelpText("Select the items you want to display in the sidebar.")),
            *[Div(CheckboxX(id=f"display_{i}", checked=i in [0, 1, 2]),FormLabel(label))
              for i, label in enumerate(["Recents", "Home", "Applications", "Desktop", "Downloads", "Documents"])]))
    return UkFormSection('Display', 'Turn items on or off to control what\'s displayed in the app.', button_txt='Update display', *content)

@rt
def index():
    return Title("Forms Example"),Container(
        heading(),
        Div(cls="flex gap-x-12")(
            sidebar,
                Ul(id="component-nav", cls="uk-switcher max-w-2xl")(
                    Li(cls="uk-active")(profile_form(),
                    *map(Li, [account_form(), appearance_form(), notifications_form(), display_form()])))))

serve()
