from app.conf.params import (
    FROM_ADDR,
    PASSWORD,
    PATH,
    SMTP_PORT,
    SMTP_SERVER,
    SUBJECT,
    TO_ADDRS,
    USERNAME,
)
from app.utils.content_provider import get_random_entry
from app.utils.email_client import HTMLEmailSender
from app.utils.template_renderer import make_html_body

if __name__ == "__main__":
    # Get a random entry from the file
    en, en_pron, de, en_phrase, de_phrase = get_random_entry(PATH)

    # Generate the HTML content using the html template
    html_body = make_html_body(en, en_pron, en_phrase, de, de_phrase)

    # Instantiate the HTML email sender
    sender = HTMLEmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    sender.send_email(FROM_ADDR, TO_ADDRS, SUBJECT, html_body)
