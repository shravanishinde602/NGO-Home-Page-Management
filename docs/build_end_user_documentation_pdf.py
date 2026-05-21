from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


BASE_DIR = Path(__file__).resolve().parent
OUTPUT = BASE_DIR / "End_User_Documentation_Login_Registration_Module.pdf"


def stylesheet():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=29,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0B2545"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="DocSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1F4D78"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            parent=styles["Normal"],
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#555555"),
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#2E74B5"),
            spaceBefore=14,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Subtle",
            parent=styles["Normal"],
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#555555"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["Normal"],
            fontSize=10.5,
            leading=14,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Cell",
            parent=styles["Normal"],
            fontSize=9.5,
            leading=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CellBold",
            parent=styles["Cell"],
            fontName="Helvetica-Bold",
        )
    )
    return styles


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawCentredString(
        LETTER[0] / 2,
        0.45 * inch,
        "End User Documentation - Login Registration Module | Page {}".format(doc.page),
    )
    canvas.restoreState()


def para(text, styles, style="Body"):
    return Paragraph(text, styles[style])


def bullets(items, styles):
    return ListFlowable(
        [ListItem(para(item, styles), leftIndent=14) for item in items],
        bulletType="bullet",
        start="-",
        leftIndent=18,
        bulletFontName="Helvetica",
        bulletFontSize=9,
    )


def numbers(items, styles):
    return ListFlowable(
        [ListItem(para(item, styles), leftIndent=14) for item in items],
        bulletType="1",
        leftIndent=18,
        bulletFontName="Helvetica",
        bulletFontSize=9,
    )


def key_value_table(rows, styles):
    data = [
        [para("Item", styles, "CellBold"), para("Details", styles, "CellBold")],
    ]
    for label, value in rows:
        data.append([para(label, styles, "CellBold"), para(value, styles, "Cell")])

    table = Table(data, colWidths=[1.75 * inch, 4.55 * inch], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F4F7")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DADCE0")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def section(story, title, styles):
    story.append(Paragraph(title, styles["Section"]))


def build_pdf():
    styles = stylesheet()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        rightMargin=1 * inch,
        leftMargin=1 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.8 * inch,
        title="End User Documentation - Login Registration Module",
        author="Student Project",
    )

    story = [
        Paragraph("End User Documentation", styles["DocTitle"]),
        Paragraph("Login and Registration Module", styles["DocSubtitle"]),
        Paragraph("Student Project User Guide", styles["Meta"]),
        key_value_table(
            [
                ("Module Name", "Login and Registration Module"),
                ("Project Type", "Django web application"),
                ("Database Used", "SQLite"),
                ("GitHub Repository", "https://github.com/shravanishinde602/login-registration"),
                ("Live Website URL", "https://login-registration-gt85.onrender.com/"),
                ("Main Users", "Normal users and admin users"),
                ("Main Purpose", "Users can register, log in, open a dashboard, and log out."),
            ],
            styles,
        ),
        Spacer(1, 10),
    ]

    section(story, "1. Introduction", styles)
    story.append(
        para(
            "This document explains how to use the Login and Registration module created in Django. "
            "The website allows a user to create an account, log in, view a dashboard page, and log out. "
            "The admin can manage user accounts from the Django admin panel.",
            styles,
        )
    )

    section(story, "2. User Roles", styles)
    story.append(
        key_value_table(
            [
                ("Visitor", "Can open the home page and click Login or Register."),
                ("Registered User", "Can log in, view the dashboard, and log out."),
                ("Administrator", "Can use the admin panel to manage users."),
            ],
            styles,
        )
    )

    section(story, "3. Website Flow", styles)
    story.append(para("The basic flow of the website is:", styles, "Subtle"))
    story.append(
        numbers(
            [
                "Open the home page.",
                "Click Register and create a new account.",
                "After registration, go to the Login page.",
                "Enter the username and password.",
                "After login, the dashboard page opens.",
                "Click Logout to end the session.",
            ],
            styles,
        )
    )

    section(story, "4. Home Page", styles)
    story.append(para("The home page is the first page of the website. Any user can open it without logging in.", styles))
    story.append(para("Available actions:", styles, "Subtle"))
    story.append(bullets(["Login: opens the login page for existing users.", "Register: opens the registration page for new users."], styles))

    section(story, "5. User Registration", styles)
    story.append(
        para(
            "A new user can create an account using the Register page. The password is saved securely using Django's authentication system.",
            styles,
        )
    )
    story.append(para("Registration fields:", styles, "Subtle"))
    story.append(bullets(["Username", "Email", "Password"], styles))
    story.append(para("Registration steps:", styles, "Subtle"))
    story.append(
        numbers(
            [
                "Click Register from the home page or navigation bar.",
                "Enter username, email, and password.",
                "Submit the form.",
                "If the details are correct, the account is created and the Login page opens.",
            ],
            styles,
        )
    )

    section(story, "6. User Login", styles)
    story.append(
        para(
            "An existing user can log in with username and password. If the details are correct, the dashboard page opens.",
            styles,
        )
    )
    story.append(para("Login steps:", styles, "Subtle"))
    story.append(
        numbers(
            [
                "Open the Login page.",
                "Enter the registered username.",
                "Enter the password.",
                "Click Login.",
                "If the credentials are valid, the dashboard opens.",
            ],
            styles,
        )
    )
    story.append(para("Error handling:", styles, "Subtle"))
    story.append(bullets(["If the username or password is wrong, an error message is shown.", "The user can stay on the Login page and try again."], styles))

    story.append(PageBreak())
    section(story, "7. Dashboard Page", styles)
    story.append(
        para(
            "The dashboard is a protected page. Only logged-in users can open it. If a user is not logged in, the website sends the user to the Login page.",
            styles,
        )
    )
    story.append(para("Dashboard content:", styles, "Subtle"))
    story.append(bullets(["Welcome message with the username.", "Logout button.", "Admin panel button for admin or staff users."], styles))

    section(story, "8. Logout", styles)
    story.append(para("The logout option ends the current login session and sends the user back to the Login page.", styles))
    story.append(para("Logout steps:", styles, "Subtle"))
    story.append(numbers(["Click Logout from the dashboard or navigation bar.", "The active session is ended.", "The Login page opens."], styles))

    section(story, "9. Admin Panel", styles)
    story.append(para("The admin can manage users from Django's built-in admin panel. To use it, a superuser account is required.", styles))
    story.append(
        key_value_table(
            [
                ("Admin URL", "/admin/"),
                ("Required Account", "Superuser or staff account"),
                ("Main Use", "View, add, edit, and delete users"),
            ],
            styles,
        )
    )
    story.append(para("Admin tasks:", styles, "Subtle"))
    story.append(
        bullets(
            [
                "View registered users.",
                "Add new users manually.",
                "Edit user details such as username, email, staff status, and permissions.",
                "Delete users when required.",
            ],
            styles,
        )
    )

    section(story, "10. Data Storage", styles)
    story.append(para("The project uses Django's built-in User model. User records are stored in the SQLite database table named auth_user.", styles))
    story.append(para("Important user data:", styles, "Subtle"))
    story.append(bullets(["Username", "Email address", "Encrypted password", "Staff and admin status"], styles))

    section(story, "11. Security Notes", styles)
    story.append(
        bullets(
            [
                "Passwords are not stored as plain text.",
                "Dashboard access is restricted to logged-in users.",
                "Logout ends the active user session.",
                "Admin access should be given only to trusted users.",
            ],
            styles,
        )
    )

    section(story, "12. Troubleshooting", styles)
    story.append(
        key_value_table(
            [
                ("Cannot log in", "Check that the username and password are correct."),
                ("Registration fails", "Check all required fields and make sure the email is not already registered."),
                ("Dashboard redirects to login", "The user is not logged in or the session has expired."),
                ("Admin panel access denied", "The account may not have staff or superuser permissions."),
                ("Bad Request on deployed site", "Check the deployed ALLOWED_HOSTS setting."),
            ],
            styles,
        )
    )

    section(story, "13. End User Summary", styles)
    story.append(
        para(
            "This module completes the basic authentication flow of the website. A user can register, log in, "
            "open the dashboard, and log out. The admin can manage users through the Django admin panel.",
            styles,
        )
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
