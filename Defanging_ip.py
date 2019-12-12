def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    print(address)
    print(address.replace( '.','[.]' ))

defangIPaddr("1.1.1.1")