joshcrypt
=========

Encryption program for a university module

Usage:
	python joshcrypt.py [-h] [-e] [-d] keyword inputFile outputFile
Flags:
	[-h]  – Help. This flag will generate help from the command line.
	[-e] – Encrypt. Use this flag to encrypt the inputFile.
	[-d] – Decrypt. Use this flag to decrypt the inputFile.
Arguments:
	Keyword – The keyword used to encrypt the file.
	inputFile – The Filename to save the encrypted/decrypted file as.

This program needs to be run from the command line; cmd.exe or any terminal emulator will suffice.
To start the encryption process a user must type:

	python joshcrypt.py –e “keyword” “inputfile” “outputfile”

Keyword is the password used for the document.
Inputfile is the file that you want to be encrypted.
Outputfile is the file that you want the encrypted file to be saved as.

To start the decryption process a user must type:

	python joshcrypt.py –d “keyword” “inputfile” “outputfile”

Keyword is the password used for the document.
Inputfile is the file that you want to be decrypted.
Outputfile is the file that you want the plain text file to be saved as.

