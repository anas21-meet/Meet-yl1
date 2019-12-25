encoder_caesar={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
encoder_caesar=[]
def ciphering():
	x=input()
	print(x)
	encoder_caesar.append(x)
	for i in encoder_caesar:
		print(encoder_caesar)
ciphering()

