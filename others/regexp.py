import re

text = "hello fady \n byebye"
find = r"h[a-z]*o\b"  # r'' make sure string is being treated as raw string
replace = "welcome"
# sub for search & replace in text return new text
out1 = re.sub(find, replace, text)
print(out1)
out2 = re.search(find, text)  # if  there more than one match only first one will return
print(out2)
out3 = re.findall(find, text)
print(out3)
# TODO
# re.escape()
# re.fullmatch()
# re.compile()
# re.split()
# re.subn()
# re.template()

out, num = re.subn(
    pattern=find, repl=replace, string=text
)  # return output , number of pattern founded
print(out, "->", num)
