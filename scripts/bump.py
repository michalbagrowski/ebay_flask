v = open("VERSION","r")
version = v.read().strip().split('.')
version[2] = str(int(version[2])+1)
v.close()


new_version = '.'.join(version)
v = open("VERSION","w")
v.write(new_version)
v.close()
