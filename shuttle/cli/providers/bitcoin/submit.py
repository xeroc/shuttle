#!/usr/bin/env python
# coding=utf-8

import json
import sys


from shuttle.cli import click
from shuttle.providers.bitcoin.utils import submit_transaction_raw


@click.command("submit", options_metavar="[OPTIONS]",
               short_help="Select Bitcoin transaction raw submitter.")
@click.option("-r", "--raw", type=str, required=True, help="Set signed Bitcoin transaction raw.")
def submit(raw):
    try:
        click.echo(
            json.dumps(
                submit_transaction_raw(tx_raw=raw),
                indent=4
            )
        )
    except UnicodeDecodeError:
        click.echo(click.style("Error: {}")
                   .format("invalid bitcoin signed transaction raw"), err=True)
        sys.exit()
    except Exception as exception:
        click.echo(click.style("Error: {}")
                   .format(str(exception)), err=True)
        sys.exit()
