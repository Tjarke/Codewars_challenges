'''
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"

If a character provided is not in the opposing alphabet, simply leave it as be.


'''


class Cipher(object):
    def __init__(self, map1, map2):
        self.encoder_dict = {}
        self.decoder_dict = {}
        for i in range(len(map1)):
            self.encoder_dict[map1[i]] =  map2[i]
            self.decoder_dict[map2[i]] =  map1[i]
    pass    

    def encode(self, s):
        output = ''
        for i in s:
            try:
                output += self.encoder_dict[i]
            except:
                output += i
        return output
    
    def decode(self, s):
        output = ''
        for i in s:
            try:
                output += self.decoder_dict[i]
            except:
                output += i
        return output


