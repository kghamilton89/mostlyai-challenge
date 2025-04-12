import pypandoc

pypandoc.convert_file("documentation-snippet.md", "pdf", outputfile="documentation-snippet.pdf")
print("✅ PDF created: output.pdf")
