import os
import gnupg
from pprint import pprint
import subprocess
import tarfile

#print gpg.export_keys(key)


#print 'public keys:'
#print dir(public_keys[0]['uids'])

video_filepath = ""
passphrase = ""
keyid = u'B137CC291B3AE62A'

gpg = gnupg.GPG(gnupghome = '~/.gnupg')
private_keys = gpg.list_keys(True)
print private_keys

#print dir(generate_gpg_key())
#sign_video(video_filepath, "", u"B137CC291B3AE62A")
#print dir(verify_vaida("Honey_Sample_G.avi.sig", ""))

#print verify_vaida("Honey_Sample_G.avi.sig", "").valid
#print verify_vaida("Honey_Sample_G.avi.sig", "").username

#print verify_vaida("Honey_Sample_G.avi.sig", "").
print gpg.export_keys(u'60A1E2E80B77E71B')


