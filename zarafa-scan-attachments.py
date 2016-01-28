#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import zarafa
from MAPICore import *
from six import BytesIO

import clamd


def opt_args():
    parser = zarafa.parser('skpcubeC')
    parser.add_option("--all", dest="all", action="store_true",
                      default=False, help="run program for all users")
    parser.add_option("--autoremove", dest="autoremove", action="store_true", default=False,
                      help="remove infected attachments")
    return parser.parse_args()


def scanmail(clam, email, autoremove):
    for attachment in email.attachments():
        result = clam.instream(BytesIO(attachment.data))
        if result['stream'][0] == 'FOUND':
            print '\t\tVirus found: [%s] [%s] [%s]' % (email.subject, result['stream'][0], result['stream'][1])
            if autoremove:
                delete(email, attachment)


def delete(email, attachment):
    print '\t\tAutoremoving attachment: [%s] [%s]' % (email.subject, attachment.name)
    email.mapiobj.DeleteAttach(int(attachment.number), 0, None, 0)
    email.mapiobj.SaveChanges(KEEP_OPEN_READWRITE)


def main():
    options, args = opt_args()
    if not (len(options.users) or options.all):
        print 'Run `zarafa-scan-attachments.py --help` for parameters'
        return

    clam = clamd.ClamdUnixSocket()

    if not clam.ping():
        print "No ClamAV Daemon connection"
    else:
        conn = zarafa.Server(options=options)
        for user in conn.users():
            print 'Scanning user [%s]' % user.name
            for folder in user.store.folders():
                print '\tScanning folder [%s]' % folder.name
                for item in folder.items():
                    scanmail(clam, item, options.autoremove)


if __name__ == '__main__':
    main()
