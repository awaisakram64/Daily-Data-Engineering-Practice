from lxml import html

# Sample HTML string
doc = '''
<html>
    <body>
        <div id="content">
            <h1>Welcome to XPath World</h1>
            <p>XPath allows you to navigate and extract data from XML or HTML documents.</p>
        </div>
    </body>
</html>
'''

# Parse the HTML string
tree = html.fromstring(doc)

# Use XPath to extract the text from the <h1> tag
header_text = tree.xpath('//h1/text()')[0]

# Print the extracted text
print(header_text)