# Requires Python 2.7 as Python 3.0+ contains bugs with the array.array() function.
import argparse
import array
import sys

# Opens file as a byte array.
def getBlock(fileName):
    f = open(fileName, "rb")
    blockArray = array.array('b', f.read())
    f.close
    return blockArray

# Converts bytes to string and writes it to a file.
def writeBlocks(blocks, fileName):
    f = open(fileName, "wb")
    string = blocks.tostring()
    f.write(blocks)
    f.close()

# Generates a key. 
# Converts the key into a byte array, creates another byte array of the key but reversed. 
# Xor the bytes together to generate the final key.
def genKey(key):
    a = array.array('b', key)
    b = a[::-1]
    for x in range(len(a)):
        a[x] = a[x] ^ b[x]
    return a

# Xor the bytes of the key with the bytes of the file.
# Loops through the key and adds the times it has looped to the end of the key
def encrypt(blocks, key):
    i = 0
    r = 0
    for block in range(len(blocks)):
        blocks[block] = blocks[block] ^ key[i]
        if i == len(key) - 1:
            i = 0
            r += 1
            key = genKey(key.tostring() + str(r))
        else:
            i += 1
    return blocks

def decrypt(blocks, key):
    i = 0
    r = 0
    for block in range(len(blocks)):
        blocks[block] = blocks[block] ^ key[i]
        if i == len(key) - 1:
            i = 0
            r += 1
            key = genKey(key.tostring() + str(r))
        else:
            i += 1
    return blocks

# Sets up the command line arguments
# Calls functions to encrypt the file.    
def main():
    parser = argparse.ArgumentParser(description="Encrypt and Decrypt a file.")
    parser.add_argument("-e", action = "store_true", default = False, dest = "edFlag", help = "Encrypt File")
    parser.add_argument("-d", action = "store_false", default = False, dest = "edFlag", help = "Decrypt File")
    parser.add_argument("keyword", action = "store", help = "Keyword used to encrypt or decrypt file")
    parser.add_argument("inputFile", action = "store", help = "Filename to be encrypted/decrypted")
    parser.add_argument("outputFile", action = "store", help = "Filename to save the encrypted/decrypted file as")
    args = parser.parse_args()
    
    if len(args.keyword) < 10 or len(args.keyword) > 40:
        print "Password needs to be greater than 10 characters and less than 40"
        sys.exit(1)

    if args.edFlag:
        print "ENCRYPTING"
        key = genKey(args.keyword)
        blocks = getBlock(args.inputFile)
        encrypted = encrypt(blocks, key)
        writeBlocks(encrypted, args.outputFile)
    else:
        print "DECRYPTING"
        key = genKey(args.keyword)
        blocks = getBlock(args.inputFile)
        decrypted = decrypt(blocks, key)
        writeBlocks(decrypted, args.outputFile)

if __name__ == '__main__':
    main()