
list=['1','2','3','a','b','c']
# print("in (%s)" % "'%s',".join(list))
print("in (%s)" % ','.join(["'%s'" % item for item in list]))
