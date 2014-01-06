import gpglib
import uIntToString
import re

def generate_key():
    real_name = input("Please enter your real name: ")
    nickname = input("Please enter your nickname: ")
    email = input("Please enter your email address: ")
    passphrase = input("Please enter a passphrase for your key: ")
    print ("App will now hang. Please provide entropy.")
    gpglib.generate_gpg_key(real_name, nickname, email, passphrase)
    print ("Key generation complete")

def extract_name_and_email(uid):
    result = re.search('(.*?)<(.*?)>', uid, flags=0)
    if not result:
        # Name and email not found
        return '',''
    return result.groups()

def generate():
    while True:
        generate_key_answer = input("Would you like to generate a new gpg key? [yes/no]")
        if generate_key_answer == "yes":
            # Generate
            generate_key()
            break
        elif generate_key_answer == "no":
            # Don't generate - continue
            break
    
    keys_list = []
    keys_dict = gpglib.private_keys_users()
    for key in keys_dict.keys():
        keys_list.append(key)
        print (str(len(keys_list) - 1) + ". " + key)

    while True:
        key_index_str = input("Please enter a key index [0-" + str(len(keys_list)-1) + "] ")
        if not str.isnumeric(key_index_str):
            print ("Please enter a numeric key index")
            continue
        key_index = int(key_index_str)
        if key_index >= len(keys_list) or key_index < 0:
            # Invalid selection
            print ("Key index out of range")
            continue
        else:
            # Key selected
            key_selection = keys_list[key_index]
            break
    
    key_id = keys_dict[key_selection]
    while True:
        passphrase = input ("Please enter the passphrase for " + key_selection + ": ")
        if gpglib.test_passphrase(key_id, passphrase):
            break
        else:
            print ("Incorrect passphrase")

    # Make VAIDA video
    key = gpglib.public_keys_details()[key_id]
    name, email = extract_name_and_email(key['uid'])
    key_expiry = key['expires']
    if key_expiry == '':
        expiry = "None"
    else:
        expiry = uIntToString.uIntToString(key_expiry)
    date = uIntToString.uIntToString(key['date'])
    fingerprint = key['fingerprint']

    print ("---")
    print ("---")
    print ("Details for making your VAIDA video")
    print ("Name: " + name)
    print ("Email: " + email)
    print ("Expiry: " + expiry)
    print ("Date: " + date)
    print ("Fingerprint: " + fingerprint)
    print ("---")
    print ("---")
    
    while True:
        fname = input("Please enter the location of your VAIDA video: ")
        try:
            vaida_path = gpglib.create_vaida(fname, passphrase, key_id)
            break
        except (IOError):
            # TODO
            print ("Please try again - file probably not found")

    print ("VAIDA created at " + vaida_path)
