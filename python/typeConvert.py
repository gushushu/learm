#!/usr/bin/env python3

def convert():

	content 	=	input("please input content(!q exit):")

	if content == '!q':
		
		exit()


	type_method 	=	input("please input type method:")

	eval_str	= 	"%s('%s')" % (type_method, content)

	content_type	= 	type(content)

	print("your input content type is \t%s" % content_type)

	print("your eval chars is %s\t" % eval_str)

	return eval_str


if __name__ == "__main__":

	while True:

		try:
			
			eval_str	=	convert()	

			convert_result	=	eval(eval_str)

			
			print("content convert result is:\t%s" % convert_result)

		except Exception:
			
			print("type convert exception")
			


