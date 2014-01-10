import gpglib
import subprocess
import gpglib
import uIntToString

def verify(file_name):
    if not file_name:
        print ("Please enter a VAIDA file to validate")
        return

    success, fingerprint, absolute_video_path, date_uint, uid = gpglib.untar_verify_vaida(file_name)

    expiration_date = uIntToString.uIntToString(date_uint)

    if not success:
        print ("Verification of VAIDA file failed!")
        return
    
    name = uid.split("<")[0].strip()

    print ("Key fingerprint: " + fingerprint)
    print ("Key expiration date: " + expiration_date)

    subprocess.call(['vlc', absolute_video_path])

    looks_like = "Does this look like " + name
    sounds_like = "Does this sound like " + name
    matching_fingerprints = "Do the key fingerprints match"
    matching_expiration = "Do the key expiration dates match"

    tests = [looks_like, sounds_like, matching_fingerprints, matching_expiration]

    for test in tests:
        while True:
            answer = input (test + "? [yes/no] ")
            if answer == "yes":
                break
            elif answer == "no":
                print ("Verification failed")
                return
            else:
                print ("Please answer 'yes' or 'no'")
    
    print ("Verified")
    try:
        gpglib.add_tmp_to_keyring()
    except GPGException as e:
        print (str(e))
    else:
        print ("Added to keyring")

#print ("Verify loaded")
