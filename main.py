import requests
import reqs
import pdf

resource_ids = [reqs.get_resource_id_from_item(publication) for publication in reqs.get_publications()]
pdf_links = [reqs.get_pdf_link(id) for id in resource_ids]

with open('out/tmp.pdf', 'wb') as pdf_file:
    bytes = requests.get(pdf_links[0]).content
    pdf_file.write(bytes)
text_content = pdf.extract_text_from_pdf('tmp.pdf')
