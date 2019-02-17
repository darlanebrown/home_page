print('hello world')
top_template=open('templates/top.html').read()
bottom_template=open('templates/bottom.html').read()

middle_template=open('templates/content_index.html').read()
index_html = top_template + middle_template + bottom_template
open("docs/index.html",'w+').write(index_html)

middle_template=open('templates/content_bio.html').read()
bio_html = top_template + middle_template + bottom_template
open("docs/bio.html",'w+').write(index_html)

