keys = [{'algo': u'1',
  'date': u'1382820481',
  'dummy': u'',
  'expires': u'',
  'fingerprint': u'4ADB422E9F865E81F0F9CA708510C999F3A490F0',
  'keyid': u'8510C999F3A490F0',
  'length': u'1024',
  'ownertrust': u'',
  'subkeys': [],
  'trust': u'',
  'type': u'sec',
  'uids': [u'Uauaua (asdfasdf) <Krzystof@Bulik.pl>']}]
def sanitise_keys(keys):
    sanitised_all = {}
    for key in keys:
        sanitised_key = {}
        sanitised_key['date'] = key['date']
        sanitised_key['expires'] = key['expires']
        sanitised_key['fingerprint'] = key['fingerprint']
        sanitised_key['length'] = key['length']
        sanitised_key['keyid'] = key['keyid']
        sanitised_key['uid'] = key['uids'][0]
        sanitised_all[key['keyid']] = sanitised_key
    return sanitised_all

def user_to_key_dict(sanitised_keys):
    user_key = {}
    for key in sanitised_keys:
        user_key[key]['uid'] = 



print sanitise_keys(keys)


