# def html_list(list_items):
#     HTML_string = "<ul>\\n"
#     for item in list_items:
#         HTML_string += "<li>{}</li>\\n".format(item)
#     HTML_string += "</ul>"
#     return HTML_string
#

#starbox

def starbox(height, width):
    height=6
    width=6
    print('*'*width)
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")
    print ('*' * width)

starbox(13,12)