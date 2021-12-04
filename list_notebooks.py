#!/usr/bin/env python
import os

from dotenv import load_dotenv
from evernote.api.client import EvernoteClient

    
if __name__ == '__main__':
    load_dotenv()
    client = EvernoteClient(
        token=os.environ["EVERNOTE_PERSONAL_TOKEN"],
        sandbox=True
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
