# with open ("readpdf_i_o.pdf", "r")  as f:
#     f_contents = f.readlines ()
# for line in f_contents:
#     words = line.split ()
#     print(f_contents)


# with open ("pythonFiles_i_o.pdf", "r")  as p:
#     p_contents = p.readlines ()
# for lines in p_contents:
#     word = lines.split ()
#     print (p_contents)

with open('pythonFiles_i_o.pdf','r') as f:
    f_cont=f.read()
    print(f_cont)