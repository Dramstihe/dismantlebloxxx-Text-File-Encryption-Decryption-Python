<h2>Encryption/Decryption Script</h2>
<p>This script allows you to encrypt and decrypt a text file using the Fernet encryption method from the cryptography module.</p>
<h3>Requirements</h3>
<ul>
  <li>Python 3</li>
  <li>cryptography module</li>
</ul>
<h3>Usage</h3>
<p>To use the script, you need to specify the file path of the text file you want to encrypt/decrypt, and the file path where you want to save the encryption/decryption key. You also need to specify the path where you want to save the key for the encryption, please make sure that the key is stored in a safe place, if you lose the key you will not be able to decrypt the file.</p>
<h4>Encryption</h4>
<p>To encrypt the file, run the script with the following command:</p>
<pre>
python encrypt.py -f path/to/textfile.txt -k path/to/keyfile.key
</pre>
<p>This command will encrypt the contents of "textfile.txt" and save the encryption key to "keyfile.key". The original text file will be overwritten with the encrypted data.</p>
<h4>Decryption</h4>
<p>To decrypt the file, you will need the key that was used to encrypt the file. Run the script with the following command:</p>
<pre>
python decrypt.py -f path/to/textfile.txt -k path/to/keyfile.key
</pre>
<p>This command will decrypt the contents of "textfile.txt" using the key stored in "keyfile.key". The decrypted data will be saved to the original text file.</p>
<h3>Notes</h3>
<ul>
  <li>Make sure to keep the key safe, without it you will not be able to decrypt the file</li>
  <li>The script will overwrite the original text file with the encrypted or decrypted data.</li>
</ul>
