# standard library
import base64


# pip
import click
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment
from python_http_client import HTTPError
from pathlib import Path


def add_attachments(mail, attachments):

    for attachment in attachments:
        with open(attachment, "rb") as f:
            file_data = f.read()
        attachment = Attachment(
            base64.b64encode(file_data).decode(), attachment, "application/pdf"
        )
        mail.add_attachment(attachment)


def send_email(to_addresses, from_address, title, body, attachments, api_key, content_type):

    try:
        body_file_path = Path(body)
        if body_file_path.exists():
            with open(body_file_path, 'r') as file:
                body = file.read()
    except:
        pass

    sg = sendgrid.SendGridAPIClient(api_key=api_key)

    for address in to_addresses:
        mail = Mail(
            Email(from_address),
            To(address),
            title,
            Content(content_type or "text/plain", body),
        )

        if attachments:
            add_attachments(mail, attachments)

        try:
            response = sg.client.mail.send.post(request_body=mail.get())
            click.secho(
                f"Sent email..." f"\nFROM:\t{from_address}" f"\nTO:\t{address}",
                fg="green",
            )
        except HTTPError as err:
            print(
                "Encountered error(s) when sending email"
                f" ({err.status_code} {err.reason}):"
            )

            for error in err.to_dict["errors"]:
                print(f"*\t{error['message']}")
