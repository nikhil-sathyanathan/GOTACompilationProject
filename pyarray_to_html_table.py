def array2htmltable(data):
    
    
    q = """\n\nCopy the HTML code below into a new website page:
    
    <!DOCTYPE html>
<html>
  <head>
    <style>
    </style>
  </head>
  <body>\n"""
    
    
    q += "<table>\n<tr><th>Name</th><th>Section</th><th>Project Title</th><th>Media</th><th>Description</th><th>Email</th></tr>\n"
    for i in [(data[0:1], 'td'), (data[1:], 'td')]:
        q += "\n".join(
            [
                "<tr>%s</tr>" % str(_mm) 
                for _mm in [
                    "".join(
                        [
                            "<%s>%s</%s>" % (i[1], str(_q), i[1]) 
                            for _q in _m
                        ]
                    ) for _m in i[0]
                ] 
            ])+"\n"
    q += """</table>
    </body>
</html>"""
    return q



