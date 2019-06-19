import os
path = os.getcwd()
list_files =os.listdir(path)

def leading_zero():
	number_digit=len(str(len(list_files)))

	for filename in list_files:
		prefix = filename[:-4].split('_')
		extension=filename[-4:]
		prefix[-1]=prefix[-1].zfill(number_digit)
		new_filename = "_".join(prefix)+extension

		os.rename(filename,new_filename)


def generate_txt(num):
	content="Hello world"
	for item in range(num):
	    with open("hello_world_%s.txt" % item, "w") as f:
	        f.write(content)


# generate_txt(10001)

leading_zero()
