import gnupg
import shutil
import os
import tarfile
from platform import system

def sanitise_keys(keys):
    sanitised_all = {}
    for key in keys:
        sanitised_key = {}
        sanitised_key['date'] = key['date']
        sanitised_key['expires'] = key['expires']
        sanitised_key['fingerprint'] = key['fingerprint']
        sanitised_key['length'] = key['length']
        sanitised_key['uid'] = key['uids'][0] # Ignoring rest of array
        sanitised_all[key['keyid']] = sanitised_key
    return sanitised_all

def _user_to_key_dict(private_keys):
    user_key = {}
    print (private_keys)
    for key in private_keys:
        #print (key)
        #dict_uids = key['uids']
        #print dict_uids
        #dict_key = dict_uids[0]
        #print dict_key
        user_key[key['uids'][0]] = key['keyid']
    return user_key



#print sanitise_keys(keys)

# expanduser?
#true_gpg_path = '''~/.gnupg'
#tmp_home = ''#'tmpgpg/'

current_os = system()
if current_os == "Windows":
    true_gpg_path = os.path.join(os.environ['APPDATA'], 'gnupg')
    tmp_home = os.path.join(os.environ['APPDATA'], 'tmpgpg')
    #os.makedirs(tmp_home)
elif current_os == "Linux":
    true_gpg_path = os.path.join(os.environ['HOME'], '.gnupg')#os.path.expanduser('.gnupg')
    tmp_home = os.path.join(os.environ['HOME'], '.tmpgpg')#os.path.expanduser('tmpgpg')
    #os.makedirs(tmp_home)
else:
    # TODO Confirm
    true_gpg_path = os.path.expanduser('~/.gnupg')
    tmp_home = os.path.expanduser('tmpgpg/')
    #os.makedirs(tmp_home)

def generate_gpg_key(real_name, nickname, email, passphrase, key_length = 2048, key_type = "RSA", expire_date = "1y"):
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return gpg.gen_key(gpg.gen_key_input(key_type = key_type, key_length = key_length, name_real = real_name, name_comment = nickname, name_email = email, expire_date = expire_date, passphrase = passphrase))

def private_keys_users():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return _user_to_key_dict(gpg.list_keys(True))

def private_keys_details():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return sanitise_keys(gpg.list_keys(True))

def public_keys_details():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    return sanitise_keys(gpg.list_keys(False))

def tmp_public_keys_details():
    gpg = gnupg.GPG(gnupghome = tmp_home)
    return sanitise_keys(gpg.list_keys(False))

def test_passphrase(keyid, passphrase):
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    with open(os.path.join(tmp_home, "tmp_signed"), "a+") as stream:
        signed = gpg.sign_file(stream, keyid = keyid, passphrase = passphrase, detach = False)
        print (signed.stderr)
        if "BAD_PASSPHRASE" in signed.stderr:
            return False
        else:
            return True

def _sign_video(video_filepath, passphrase, keyid):
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    with open(video_filepath, "rb") as stream:
        signed = gpg.sign_file(stream, keyid = keyid, passphrase = passphrase, detach = True)
    print (dir(signed))
    print (signed.stderr)
    if signed.stderr:
        # Failed
        pass
    signature_path = video_filepath + ".signature"
    with open(signature_path, "wb") as video_signature:
        video_signature.write(signed.data)
    return signature_path

    #result_file = open(video_filepath + ".sig","wb")
    #result_file.write(signed.data)
    #result_file.close()

def create_vaida(video_filepath, passphrase, keyid):
    #TODO slashes -> windows (throughout)
    signature_path = _sign_video(video_filepath, passphrase, keyid)
    with tarfile.open(name=video_filepath.split(os.path.sep)[-1] + ".vaida", mode='w', fileobj=None, bufsize=10240) as tar:
        gpg = gnupg.GPG(gnupghome = true_gpg_path)
        armored_key = gpg.export_keys(keyid)
        with open ("pubkey", "wb") as pubkey:
            pubkey.write(bytes(armored_key, 'UTF-8'))
        tar.add(video_filepath, arcname = "video")
        tar.add("pubkey", arcname = "pubkey")
        tar.add(signature_path, arcname = "signature")

def untar_verify_vaida(vaida_path):
    _clear_temp()
    gpg = gnupg.GPG(gnupghome = tmp_home)
    with tarfile.open(name = vaida_path, mode = "r") as tar:
        print (tar.getnames())
        tar.extractall(tmp_home)
        with open(os.path.join(tmp_home, "pubkey"), "rb") as pubkey:
            imported = gpg.import_keys(pubkey.read())
        print (dir(imported))
        verification = gpg.verify_file(open(os.path.join(tmp_home, tar.getnames()[2]), "rb"), os.path.join(tmp_home, tar.getnames()[0]))
        print (verification.valid)
        print (verification.stderr)
        #print dir(verification)
        
        dicto = tmp_public_keys_details()
        for key in dicto:
            expiration = dicto[key]["expires"]
    return (verification.valid, imported.fingerprints[0], os.path.abspath(os.path.join(tmp_home, "video")), expiration) 

def _clear_temp():
    if os.path.isdir(tmp_home):
        shutil.rmtree(tmp_home)

def add_tmp_to_keyring():
    gpg = gnupg.GPG(gnupghome = true_gpg_path)
    with open(tmp_home + "pubkey", "rb") as pubkey:
        trusted = gpg.import_keys(pubkey.read())
    print (dir(trusted))
    print (trusted.stderr)
    _clear_temp()

#create_vaida("/home/picrin/programming/VAIDA/Honey_Sample_G.avi", "dirty loondry boundry. stash/", u"D98029C596F20E5D")
#print verify_vaida("/home/picrin/programming/VAIDA/backend/Honey_Sample_G.avi.vaida.tar")
#add_pub_keyring()
#print public_keys_details()
#print private_keys_details()
#generate_gpg_key("Hugh McGrade (do not trust)", "hmg (do not trust)", "hugh@mcgrade.ac.uk (do not trust)", "dirty loondry boundry. stash/")
#create_vaida("/home/hugh/Documents/VAIDA/UI/video004.mp4", "dirty loondry boundry. stash/", u"62CDD87039635942")
#untar_verify_vaida("video004.mp4.vaida")
#print public_keys_details()
#print private_keys_details()
