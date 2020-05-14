x = ['sdsd', '', '']
dirs = {len(x[0]) > 0 : x[0], len(x[0]) < 0 : 0}.get(True, 99)
print(dirs)

