import os
import gnupg
from pprint import pprint
import subprocess
gpg = gnupg.GPG(gnupghome='/home/picrin/.gnupg')

#print gpg.export_keys(key)
public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)
#print 'public keys:'
#print dir(public_keys[0]['uids'])
pprint(public_keys)
#print 'private keys:'
pprint(private_keys)

video_filepath = "Honey_Sample_G.avi"
passphrase = ""
keyid = u'B137CC291B3AE62A'
def sign_video(video_filepath, passphrase, keyid):
    stream = open(video_filepath, "rb")
    #print stream
    signed = gpg.sign_file(stream, keyid = keyid)
    stream.close()
    print dir(signed)
    print signed.stderr
    result_file = open(video_filepath + ".sig","w")
    result_file.write(signed.data)
    result_file.close()


def generate_gpg_key():
    return gpg.gen_key(gpg.gen_key_input(key_type = "RSA", key_length = 1024, name_real = "Uauaua", name_comment = "asdfasdf", name_email = "Krzystof@Bulik.pl"))

def verify_vaida(digitally_signed_video, digital_signature):
    with open(digitally_signed_video, "rb") as stream:
        verified = gpg.verify_file(stream)
    return verified

def add_untrusted_key():
    pass

#print dir(generate_gpg_key())
#sign_video(video_filepath, "", u"B137CC291B3AE62A")
#print dir(verify_vaida("Honey_Sample_G.avi.sig", ""))

#print verify_vaida("Honey_Sample_G.avi.sig", "").valid
#print verify_vaida("Honey_Sample_G.avi.sig", "").username

#print verify_vaida("Honey_Sample_G.avi.sig", "").
#print gpg.export_keys(u'B137CC291B3AE62A')
#generate_gpg_key()

print dir(gpg.import_keys("""-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.12 (GNU/Linux)

mI0EUmwURQEEAL8Hq+vt7Jv2fUjqRRZTyLOwGHd3eQgKoLg9WxfrOBcqkBE6ftKK
dSvuhFEXmkiCgNzUWQN77bkGjLtQD9Ra9NeuBvEnIokZ2xGv0wROTpRh1/7sMEeH
JBTfxjWRN+s74pV0rPbBW40W9PhqXh0+cIUB8Nf0t0trnSe/S6YjCUybABEBAAG0
MEJhcnRlayBGcmFuY3p5ayAodGVzdHVzZXIyKSA8QmFydGVrQEZyYW5jenlrLnBs
Poi4BBMBAgAiBQJSbBRFAhsvBgsJCAcDAgYVCAIJCgsEFgIDAQIeAQIXgAAKCRCx
N8wpGzrmKpTPA/45GD+cm5gvmmxtatQcPUFUZWZw08ML/l2kERDgwrLI88gOAtWd
bdMWEAHX5vN/FscirJ9QzS556q/mYRhbbuaUb2XzSYfntZ2tqtRZcXxkDsIxH+/S
mwo2FOJepw9KcpsYuu5wJCwS0T+p1b4T7gOG7p+CWG8gYrcFChX86/l9JQ==
=EIZC
-----END PGP PUBLIC KEY BLOCK-----""")
)

print gpg.import_keys("""-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.12 (GNU/Linux)

mI0EUmwURQEEAL8Hq+vt7Jv2fUjqRRZTyLOwGHd3eQgKoLg9WxfrOBcqkBE6ftKK
dSvuhFEXmkiCgNzUWQN77bkGjLtQD9Ra9NeuBvEnIokZ2xGv0wROTpRh1/7sMEeH
JBTfxjWRN+s74pV0rPbBW40W9PhqXh0+cIUB8Nf0t0trnSe/S6YjCUybABEBAAG0
MEJhcnRlayBGcmFuY3p5ayAodGVzdHVzZXIyKSA8QmFydGVrQEZyYW5jenlrLnBs
Poi4BBMBAgAiBQJSbBRFAhsvBgsJCAcDAgYVCAIJCgsEFgIDAQIeAQIXgAAKCRCx
N8wpGzrmKpTPA/45GD+cm5gvmmxtatQcPUFUZWZw08ML/l2kERDgwrLI88gOAtWd
bdMWEAHX5vN/FscirJ9QzS556q/mYRhbbuaUb2XzSYfntZ2tqtRZcXxkDsIxH+/S
mwo2FOJepw9KcpsYuu5wJCwS0T+p1b4T7gOG7p+CWG8gYrcFChX86/l9JQ==
=EIZC
-----END PGP PUBLIC KEY BLOCK-----""").imported

#popen = subprocess.Popen('sleep 10', shell=True)
#popen.wait()
