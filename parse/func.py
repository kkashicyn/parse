def write_to_html(data, file_name):
    # create html document
    html_doc_begin = "<html><body><table>"
    html_inner = ""
    for item in data:
        html_inner += "<tr><td>"+item['title']+"</td><td>"+item['country']+"</td>"
        for review in item['reviews']:
            html_inner+="<td>"+review+"</td>"
        html_inner +="</tr>"
    html_doc_end = "</table></body></html>"

    html = html_doc_begin + html_inner + html_doc_end

    # save html document    
    with open(file_name, 'w') as f:
        f.write(html)         