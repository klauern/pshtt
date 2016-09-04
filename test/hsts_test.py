
# A test suite for the HSTS parser in hsts.py.
#
# Intended to precisely meet the RFC 6797 specification:
# http://tools.ietf.org/html/rfc6797

CASES = [

# Observed in many places.
{
  'name': 'gold standard',
  'header': "max-age=31536000; includeSubDomains; preload",
  'valid': True,
  'enabled': True,
  'max_age': 31536000,
  'include_subdomains': True,
  'preload': True
},

# Not observed.
{
  'name': 'allow quoted strings',
  'header': "max-age=\"31536000\"; includeSubDomains; preload",
  'valid': True,
  'enabled': True,
  'max_age': 31536000,
  'include_subdomains': True,
  'preload': True
},

# Observed at one time on uspsoig.gov.
{
  'name': 'mixed case includesubdomains',
  'header': "max-age=63072000; includeSubdomains; preload",
  'valid': True,
  'enabled': True,
  'max_age': 63072000,
  'include_subdomains': True,
  'preload': True
},

# Not observed.
{
  'name': 'extra semicolon',
  'header': "max-age=63072000; includeSubdomains; preload;",
  'valid': True,
  'enabled': True,
  'max_age': 63072000,
  'include_subdomains': True,
  'preload': True
},

# Observed in many places.
{
  'name': '0 max age (disable HSTS)',
  'header': "max-age=0",
  'valid': True,
  'enabled': False,
  'max_age': 0,
  'include_subdomains': False,
  'preload': False
},

# Not observed.
{
  'name': '0 max age with other directives',
  'header': "max-age=0; includeSubDomains; preload",
  'valid': True,
  'enabled': False,
  'max_age': 0,
  'include_subdomains': True,
  'preload': True
},

# Observed in many places.
{
  'name': '1 day max-age',
  'header': "max-age=86400",
  'valid': True,
  'enabled': True,
  'max_age': 86400,
  'include_subdomains': False,
  'preload': False
},

# Observed in several places.
{
  'name': 'preload without subdomains, no space',
  'header': "max-age=31536000;preload",
  'valid': True,
  'enabled': True,
  'max_age': 31536000,
  'include_subdomains': False,
  'preload': True
},

# Observed at one time on jamesmadison.gov.
{
  'name': 'bare includesubdomains not allowed',
  'header': "includeSubDomains",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
},

# Observed at one time on www.whitehouse.gov.
{
  'name': 'underscored subdomains policy not allowed',
  'header': "max-age=3600;include_subdomains",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
},

# Observed at one time on www.tedcruz.org.
{
  'name': 'comma between directives not allowed',
  'header': "max-age=15552000, includeSubDomains",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
},

# Not observed.
{
  'name': 'missing equals sign not allowed',
  'header': "max-age3600; includeSubDomains",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
},

# Not observed.
{
  'name': 'single quotes not allowed',
  'header': "max-age='31536000'; includeSubDomains; preload",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
},

# Not observed.
{
  'name': 'lone double quote not allowed',
  'header': "max-age=\"31536000; includeSubDomains; preload",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
},

# Not observed.
{
  'name': 'quoted directive name not allowed',
  'header': "\"max-age\"=31536000; includeSubDomains; preload",
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
}
]

# Garbage headers that all should get the same negative result.
GARBAGE = [
  "312384761283746",
  0, None, "", "-1",
  "$!#@%!#}"
]

GARBAGE_RESULT = {
  'valid': False,
  'enabled': None,
  'max_age': None,
  'include_subdomains': None,
  'preload': None
}

class HstsTest():

  def test_basic_cases():
    for case in CASES:
      pass

  def test_garbage():
    for garb in GARBAGE:
      pass

