# Function for printing the borders of the PDF
def draw_pdf_ruler(pdf):
    pdf.line(550, 800, 550, 50)	#Right Vertical line
    pdf.line(551, 801, 551, 51)
    pdf.line(50, 50, 550, 50)	# Bottom Horizontal line
    pdf.line(51, 51, 551, 51)
    pdf.line(50, 800, 550, 800)	# Upper Horizontal line
    pdf.line(51, 801, 551, 801)
    pdf.line(50, 750, 550, 750)	# Lower horizontal line of title
    pdf.line(51, 751, 551, 751)
    pdf.line(50, 800, 50, 50)	# Left Vertical line
    pdf.line(51, 801, 51, 51)
    # Image borders
    pdf.line(400, 600, 550, 600)	# Bottom Horizontal line
    pdf.line(400, 601, 550, 601)
    pdf.line(400, 600, 400, 750)	# Left Vertical line of title
    pdf.line(401, 600, 401, 750)
    pdf.line(50, 425, 550, 425)	# Middle Horizontal line
    pdf.line(51, 426, 551, 426)
    #Logo borders
    pdf.line(400, 180, 550, 180)	# Upper Horizontal line of logo
    pdf.line(400, 181, 550, 181)
    pdf.line(400, 50, 400, 180)	# Left vertical line of logo
    pdf.line(401, 50, 401, 180)

