

import sys,os

def lister(root,*excludedirs):
	for(thisdir,subsdir,fileshere) in os.walk(root):
		print('\n[' + thisdir + ']')
		for fname in fileshere:
			path = os.path.join(thisdir,fname)
			print('\t' + path)

		#从subsdir中删除无需遍历的子目录
		for excludedir in excludedirs:
			for subdir in subsdir:
				if excludedir.lower() == subdir.lower():
						subsdir.remove(subdir)

if __name__ == '__main__':

	#收集命令行参数指定的，无需遍历的目录，存储在exdirs中
	exdirs = []
	for i in range(2,len(sys.argv)):
		exdirs.append(sys.argv[i])

	#argv[1]==>待遍历目录
	#exdirs ==>无需遍历的子目录
	lister(sys.argv[1],*exdirs)