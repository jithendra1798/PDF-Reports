# Importing a function which creates PDF when given the list of strings in prescribed format as input
from ruler import draw_pdf_ruler
def space(text,font):
    text.setFont("Helvetica", 8)
    text.textLine('')
    text.setFont(font, 15)
def scorecard(L,key):

    #############################################################
    # Details of the Document
    file_name = '../Reports/Report'+key+'.pdf'  # Name of output PDF
    document_title = 'Report Card'
    title = L[0]
    sub_title1 = 'Bio Data'
    sub_title2 = 'Exam Details'
    student_image = f"../images/{L[3][1]+'.png'}" # Full name of student    image = f"images/'{L[3][1]}.png'"
    logo_image = f"../images/logo.png"
    
    #############################################################
    # Making a directory for reports if it doesn't exists
    my_folder='../Reports'
    import os
    if not os.path.exists(my_folder):
        os.makedirs(my_folder)
    #############################################################
    # 0) Creating Empty PDF document 
    from reportlab.pdfgen import canvas 

    pdf = canvas.Canvas(file_name)
    pdf.setTitle(document_title)
    
    draw_pdf_ruler(pdf) # Draw rules to empty pdf


    #############################################################
    # 1) Title of the PDF
    pdf.setFont('Helvetica-Bold', 24)
    pdf.drawCentredString(300, 770, title)

    #############################################################
    # 2) Sub Title-1 (Bio Data)
    from reportlab.lib.colors import HexColor
    pdf.setFillColor(HexColor('#3572a5'))
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290,730, sub_title1)
    
    #############################################################
    # 3) Printing Bio-data
    from reportlab.lib import colors

    text = pdf.beginText(80, 700)
    text.setFillColor(colors.black)
    text.setFont("Helvetica-Bold", 15)
    for line in L[1:11]:
        text.textLine(line[0])
        space(text,"Helvetica-Bold")
    pdf.drawText(text)
    
    text = pdf.beginText(250, 700)
    text.setFillColor(colors.darkblue)
    text.setFont("Helvetica-Bold", 15)
    for line in L[1:11]:
        text.textLine(':  '+line[1])
        space(text,"Helvetica-Bold")
    pdf.drawText(text)
    
    #############################################################
    # 4) Printing studet image
    x=550
    y=750
    pdf.drawImage(student_image, x-148, y-148, width=147, height=147, mask=None, preserveAspectRatio=False, anchor='c')
    
    #############################################################
    # 5) Printing logo image
    x=550
    y=200
    pdf.drawImage(logo_image, x-148, y-148, width=147, height=127, mask=None, preserveAspectRatio=False, anchor='c')

    #############################################################
    # 6) Sub Title-2 (Exam Data)
    pdf.setFillColor(HexColor(0xff8100))
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290,400, sub_title2)
    
    #############################################################
    # 7) Printing Exam-data
    
    text = pdf.beginText(80, 380)
    text.setFont("Helvetica-Bold", 12)
    text.setFillColor(colors.black)
    
    line=L[-1]  #Final result
    text.setFillColor(colors.indigo)
    text.textLine(line)
    pdf.drawText(text)
    
    line=L[11]      # Exam date
    text.textLine('')
    text.setFillColor(colors.black)
    text.setFont("Helvetica-Bold", 10)
    text.textLine(line[0]+line[1])
    
    # Printing Marks and Answers
    text.setFillColor(colors.brown)
    text.setFont("Courier-Bold", 10)
    text.textLine('')
    for i in range(0,5,2):
        for line in L[12:18]:
            text.textLine(line[0]+line[1][len(line[1])*i//5:len(line[1])*(i+2)//5])
        text.textLine('')
    
    # Final Marks
    text.setFillColor(colors.green)
    text.textLine('')
    text.setFont("Helvetica-Bold", 20)
    line = L[18][0]+L[18][1]
    text.textLine(line)
    
    # Note on Outcome shortcuts
    text.setFillColor(colors.red)
    text.setFont("Times-Roman", 10)
    text.textLine('')
    line = '** Note on Outcome(C/IC/NA) : [C - Correct], [IC - Incorrect], [NA - Not Answered]'
    text.textLine(line)
    pdf.drawText(text)
    
    #############################################################
    # ) Saving the report card to storage
    pdf.save()
