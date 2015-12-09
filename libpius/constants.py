# vim:shiftwidth=2:tabstop=2:expandtab:textwidth=80:softtabstop=2:ai:

import os

VERSION = '2.2.1'
MODE_INTERACTIVE = 0
MODE_CACHE_PASSPHRASE = 1
MODE_AGENT = 2
HOME = os.environ.get('HOME')
GNUPGHOME = os.environ.get('GNUPGHOME', os.path.join(HOME, '.gnupg'))
DEFAULT_GPG_PATH = '/usr/bin/gpg2'
DEFAULT_KEYRING = os.path.join(GNUPGHOME, 'pubring.gpg')
DEFAULT_TMP_DIR = '/tmp/pius_tmp'
DEFAULT_OUT_DIR = '/tmp/pius_out'
DEFAULT_MAIL_HOST = 'localhost'
DEFAULT_MAIL_PORT = 587
PIUS_HOME = os.path.join(HOME, '.pius')
PIUS_RC = os.path.join(PIUS_HOME, 'piusrc')

# Note the line with the email address on it below is intentionally
# shorter than the rest to give it space to grow and still be < 80.
DEFAULT_MIME_EMAIL_TEXT = '''Hello,

Attached is a copy of your PGP key (0x%(keyid)s) signed by my key
(0x%(signer)s).

If your key has more than one UID, than this key only has the UID associated
with this email address (%(email)s) signed and you will receive
additional emails containing signatures of the other UIDs at the respective
email addresses.

Please take the attached message and decrypt it and then import it.
Something like this should work:

   gpg --import %(file)s

(In mutt ctrl-k will do this.)

Then, don't forget to send it to a keyserver:

   gpg --keyserver pool.sks-keyservers.net --send-key %(keyid)s

If you have any questions, let me know.


Generated by PIUS (http://www.phildev.net/pius/).
'''

DEFAULT_NON_MIME_EMAIL_TEXT = '''Hello,

Attached is a copy of your PGP key (0x%(keyid)s) signed by my key
(0x%(signer)s).

If your key has more than one UID, than this key only has the UID associated
with this email address (%(email)s) signed and you will receive
additional emails containing signatures of the other UIDs at the respective
email addresses.

Please take the attached message and decrypt it and then import it.
Something like this should work:

   gpg -d %(file)s | gpg --import

Then, don't forget to send it to a keyserver:

   gpg --keyserver pool.sks-keyservers.net --send-key %(keyid)s

If you have any questions, let me know.


Generated by PIUS (http://www.phildev.net/pius/).
'''

CERT_LEVEL_INFO = '''Each certification level means something specific and is a
public statement by you about this UID on this key. The following definitions
are taken from the GnuPG man page.

0   means you make no particular claim as to how carefully you verified the
    key.

1   means you believe the key is owned by the person who claims to own it but
    you could not, or did not verify the key at all. This is useful for a
    "persona" verification, where you sign the key of a pseudonymous user.

2   means you did casual verification of the key. For example, this could mean
    that you verified the key fingerprint and checked the user ID on the key
    against a photo ID.

3   means you did extensive verification of the key. For example, this could
    mean that you verified the key fingerprint with the owner of the key in
    person, and that you checked, by means of a hard to forge document with a
    photo ID (such as a passport) that the name of the key owner matches the
    name in the user ID on the key, and finally that you verified (by exchange
    of email) that the email address on the key belongs to the key owner.

Note that the examples given above for levels 2 and 3 are just that: examples.
In the end, it is up to you to decide just what "casual" and "extensive" mean to
you.'''

