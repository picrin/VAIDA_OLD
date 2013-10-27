import gnupg, tarfile

def sanitise_keys(keys):
    sanitised_all = {}
    for key in keys:
        sanitised_key = {}
        sanitised_key['date'] = key['date']
        sanitised_key['expires'] = key['expires']
        sanitised_key['fingerprint'] = key['fingerprint']
        sanitised_key['length'] = key['length']
        sanitised_key['uid'] = key['uids'][0]
        sanitised_all[key['keyid']] = sanitised_key
    return sanitised_all

def user_to_key_dict(private_keys):
    user_key = {}
    for key in private_keys:
        user_key[key['uids'][0]] = key['keyid']
    return user_key

#print sanitise_keys(keys)

true_gpg_path = '~/.gnupg'
tmp_home = '~/.tmpgpg'
def generate_gpg_key(real_name, nickname, email, passphrase, key_length = 2048, key_type = "RSA", expire_date = "1y"):
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return gpg.gen_key(gpg.gen_key_input(key_type = key_type, key_length = key_length, name_real = real_name, name_comment = nickname, name_email = email, expire_date = expire_date, passphrase = passphrase))

def private_keys_users():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return user_to_key_dict(gpg.list_keys(True))

def private_keys_details():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return sanitise_keys(gpg.list_keys(True))

def public_keys_details():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return sanitise_keys(gpg.list_keys(False))

def sign_video(video_filepath, passphrase, keyid):
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    with open(video_filepath, "rb") as stream:
        signed = gpg.sign_file(stream, keyid = keyid, passphrase = passphrase, detach = True)
    print (dir(signed))
    print (signed.stderr)
    with open(video_filepath + ".signature", "wb") as signed_video:
        signed_video.write(signed.data)

    #result_file = open(video_filepath + ".sig","wb")
    #result_file.write(signed.data)
    #result_file.close()

def create_vaida(video_filepath, passphrase, keyid):
    binary = sign_video(video_filepath, passphrase, keyid)
    tar = tarfile.open(name=video_filepath + ".vaida.tar", mode='w', fileobj=None, bufsize=10240)
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    armored_key = gpg.export_keys(keyid)
    with open ("pubkey", "wb") as pubkey:
        pubkey.write(gpg.export_keys(keyid))
    tar.add(video_filepath)
    tar.add("pubkey")
    tar.add(video_filepath + ".signature")

def verify_vaida(digitally_signed_video, digital_signature):
    with open(digitally_signed_video, "rb") as stream:
        verified = gpg.verify_file(stream)
    return verified


#print public_keys_details()

print (private_keys_details())

create_vaida("/home/picrin/programming/VAIDA/Honey_Sample_G.avi", "adam@kurkiewicz.pl", u"60A1E2E80B77E71B")
#print private_keys_users()


#generate_gpg_key("Adam Kurkiewicz", "picrin", "adam@kurkiewicz.pl", "lubie_placki")

