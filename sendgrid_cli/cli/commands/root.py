"""CLI entrypoint 'sendgrid' command"""

import click
import os

from sendgrid_cli.sendgrid_cli import send_email
from sendgrid_cli.utils import check_api_key, split_into_list


@click.command()
@click.argument(
    "to_addresses",
    type=click.STRING,
    default=os.getenv("SENDGRID_TO_ADDRESSES"),
)
@click.argument(
    "from_address",
    type=click.STRING,
    default=os.getenv("SENDGRID_FROM_ADDRESS"),
)
@click.argument("title", type=click.STRING, default=os.getenv("SENDGRID_TITLE"))
@click.option(
    "--body",
    "-b",
    "body",
    type=click.STRING,
    help="Body of your email.",
    default=os.getenv("SENDGRID_BODY"),
)
@click.option(
    "--attachments",
    "-a",
    "attachments",
    type=click.STRING,
    help="Attachments for you email, single attachment or list: file1,file2,file3",
    default=os.getenv("SENDGRID_ATTACHMENTS"),
)
@click.option(
    "--sendgrid_api_key",
    "-api",
    "api_key",
    type=click.STRING,
    help="Your sendgrid API key.",
    default=os.getenv("SENDGRID_API_KEY"),
)
@click.option(
    "--content_type",
    "content_type",
    type=click.STRING,
    default=os.getenv("SENDGRID_CONTENT_TYPE"),
)
def sendgrid_cli(to_addresses, from_address, title, body, attachments, api_key, content_type):
    """CLI entrypoint and base command"""

    check_api_key(api_key)

    to_addresses = split_into_list(to_addresses)

    attachments = split_into_list(attachments)

    send_email(to_addresses, from_address, title, body, attachments, api_key, content_type)
