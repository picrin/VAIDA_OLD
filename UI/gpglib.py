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
tmp_home = 'tmpgpg/'

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
    print dir(signed)
    print signed.stderr
    with open(video_filepath + ".signature", "wb") as signed_video:
        signed_video.write(signed.data)

    #result_file = open(video_filepath + ".sig","wb")
    #result_file.write(signed.data)
    #result_file.close()

def create_vaida(video_filepath, passphrase, keyid):
    #TODO slashes -> windows
    binary = sign_video(video_filepath, passphrase, keyid)
    with tarfile.open(name=hvideo_filepath.split("/")[-1] + ".vaida.tar", mode='w', fileobj=None, bufsize=10240) as tar:
        gpg = gnupg.GPG(gnupghome = true_gpg_path)
        armored_key = gpg.export_keys(keyid)
        with open ("pubkey", "wb") as pubkey:
            pubkey.write(gpg.export_keys(keyid))
        tar.add(video_filepath, arcname = video_filepath.split("/")[-1])
        tar.add("pubkey")
        tar.add(video_filepath + ".signature", arcname = video_filepath.split("/")[-1] + ".signature")
import shutil
import os

def verify_vaida(vaida_path):
    if os.path.isdir(tmp_home):
        shutil.rmtree(tmp_home)

    gpg = gnupg.GPG(gnupghome = tmp_home)
    with tarfile.open(name = vaida_path, mode = "r") as tar:
        print tar.getnames()
        tar.extractall(tmp_home)
        with open(tmp_home + "pubkey", "rb") as pubkey:
            imported = gpg.import_keys(pubkey.read())
        print dir(imported)
        verification = gpg.verify_file(open(tmp_home + tar.getnames()[2], "rb"), tmp_home + tar.getnames()[0])
        print verification.valid
        print verification.stderr
        #print dir(verification)
    return (verification.valid, imported.fingerprints[0])

def add_pub_keyring():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    with open(tmp_home + "pubkey", "rb") as pubkey:
        trusted = gpg.import_keys(pubkey.read())
    print dir(trusted)
    print trusted.stderr
    if os.path.isdir(tmp_home):
        shutil.rmtree(tmp_home)
    return "success!"
print public_keys_details()
#create_vaida("/home/picrin/programming/VAIDA/Honey_Sample_G.avi", "dirty loondry boundry. stash/", u"D98029C596F20E5D")
#print verify_vaida("/home/picrin/programming/VAIDA/backend/Honey_Sample_G.avi.vaida.tar")
#add_pub_keyring()
#print public_keys_details()
#print private_keys_details()
#generate_gpg_key("Hugh McGrade (do not trust)", "hmg (do not trust)", "hugh@mcgrade.ac.uk (do not trust)", "dirty loondry boundry. stash/")

