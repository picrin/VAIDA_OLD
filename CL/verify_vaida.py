import gpglib
import subprocess
import gpglib

def verify_vaida(file_name):
    if not file_name:
        print ("Please enter a VAIDA file to validate")
        return

    success, fingerprint, absolute_video_path, date_uint, uid = untar_verify_vaida(file_name)

    expiration_date = uIntToString,uIntToString(date_uint)

    if not success:
        print ("Verification of VAIDA file failed!")
        return
    
    name = uid.split("<")[0].strip()
        
    subprocess.call(['vlc', absolute_video_path])

    print ("Key fingerprint: " + fingerprint)
    print ("Key expiration date: " + expiration_date)

    looks_like = "Does this look like " + name + "?"
    sounds_like = "Does this sound like " + name + "?"
    matching_fingerprints = "Do the key fingerprints match?"
    matching_expiration = "Do the key expiration dates match?"

    tests = [looks_like, sounds_like, matching_fingerprints, matching_expirations]

    for test in tests:
        answer = input (test + "? [yes/no] ")
        if answer == "yes":
            break
        elif answer == "no":
            print ("Verification failed")
            return
        else:
            print ("Invalid answer")

#print ("Verify loaded")
