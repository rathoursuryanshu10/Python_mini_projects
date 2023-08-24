import pikepdf as pk
old_pdf=pk.Pdf.open("python3tutorial.pdf")
no_extr=pk.Permissions(extract=False)
old_pdf.save("protected_pdf.pdf",encryption=pk.Encryption(user="123",owner="ABC",allow=no_extr))
