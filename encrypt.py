import os, sys
import base64


for root, dirs, files in os.walk('./'):
	for file in files:
		the_file=file
		if the_file=="decrypt.py" or the_file=="encrypt.py":
			continue
		f=open(the_file,"rb")
		plain_data=f.read()
		f.close()

		en_data = plain_data
		en_data = base64.b64encode(en_data)

		f=open(the_file,"wb")
		f.write(en_data)
		f.close()

    
print("Done!")
sys.exit() 