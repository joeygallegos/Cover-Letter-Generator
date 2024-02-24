from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
import markdown2

def generate_cover_letter(job_title, company_name):
    # Open the Markdown file
    with open("letter.md", "r") as f:
        # Read the contents of the file
        markdown_content = f.read().format(job_title=job_title, company_name=company_name)

    # Convert markdown to HTML using markdown2
    html_text = markdown2.markdown(markdown_content, extras={'breaks': {'on_newline': True, 'on_backslash': True}})
    print(html_text)

    # Generate PDF
    doc = SimpleDocTemplate(f"Cover Letter for {company_name}.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.leading = 14
    style.bulletIndent = 6
    style.spaceAfter = 10
    flowables = [Paragraph(html_text, style)]
    doc.build(flowables)

if __name__ == "__main__":
    job_title = input("Enter the job title: ")
    company_name = input("Enter the company name: ")
    generate_cover_letter(job_title, company_name)
