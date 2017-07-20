import sys,os

def lister(root):
	for(thisdir,subsdir,fileshere) in os.walk(root):
		print('\n[' + thisdir + ']')
		for fname in fileshere:
			path = os.path.join(thisdir,fname)
			print('\t' + path)

if __name__ == '__main__':
	lister(sys.argv[1])