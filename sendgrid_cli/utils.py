import click


def check_api_key(api_key):
    if not api_key:
        click.secho("No SendGrid API key provided, cannot send email", fg="red")


def split_into_list(list_to_split):
    if list_to_split:
        try:
            list_to_split = list_to_split.split(",")
        except:
            list(list_to_split)

    return list_to_split
