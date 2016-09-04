
# A complete parser for HSTS headers.
#
# Intended to precisely meet the RFC 6797 specification:
# http://tools.ietf.org/html/rfc6797
#
# RFC 6797 allows HSTS to be extended with non-standard directives.
# This parser has special support for the "preload" directive extension.
#
# However, "preload readiness" is not assessed, as that requires
# information besides that which is contained in the HSTS header.

# Hsts.parse(header) returns a dict with 5 values:
#
# 'valid' (True, False) -
#    Whether the header is a valid HSTS policy.
# 'enabled' (True, False, None) -
#    Whether HSTS is enabled for this domain.
#    If header is invalid, set to None.
# 'max_age' (int, None) -
#    The integer value of max-age.
#    If header is invalid, set to None.
# 'include_subdomains' (True, False, None) -
#    Whether the policy has an 'includeSubDomains' directive.
#    If header is invalid, set to None.
# 'preload' (True, False, None) -
#    Whether the policy has a 'preload' directive.
#    If header is invalid, set to None.

class Hsts():

    def parse(header):
        pass
