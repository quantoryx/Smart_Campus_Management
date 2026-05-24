from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
import zipfile


OUTPUT_FILE = Path("smart_campus_report_draft.docx")


def make_run(text, bold=False, italic=False, size=None):
    text = escape(text)
    preserve = ' xml:space="preserve"' if "  " in text or text[:1] == " " or text[-1:] == " " else ""

    properties = []
    if bold:
        properties.append("<w:b/>")
    if italic:
        properties.append("<w:i/>")
    if size is not None:
        properties.append(f'<w:sz w:val="{size}"/>')

    run_properties = f"<w:rPr>{''.join(properties)}</w:rPr>" if properties else ""
    return f"<w:r>{run_properties}<w:t{preserve}>{text}</w:t></w:r>"


def make_paragraph(
    text="",
    *,
    align=None,
    bold=False,
    italic=False,
    size=None,
    page_break_before=False,
):
    paragraph_properties = []
    if align:
        paragraph_properties.append(f'<w:jc w:val="{align}"/>')

    ppr = f"<w:pPr>{''.join(paragraph_properties)}</w:pPr>" if paragraph_properties else ""
    runs = []

    if page_break_before:
        runs.append('<w:r><w:br w:type="page"/></w:r>')

    if text:
        runs.append(make_run(text, bold=bold, italic=italic, size=size))

    if not runs:
        runs.append("<w:r/>")

    return f"<w:p>{ppr}{''.join(runs)}</w:p>"


def build_document_xml():
    paragraphs = [
        make_paragraph("DAYANANDA SAGAR COLLEGE OF ENGINEERING", align="center", bold=True, size=30),
        make_paragraph(
            "(An Autonomous Institute affiliated to VTU, Belagavi, Approved by AICTE)",
            align="center",
            size=22,
        ),
        make_paragraph(
            "Shavige Malleshwara Hills, Kumaraswamy Layout, Bengaluru - 560111",
            align="center",
            size=22,
        ),
        make_paragraph("Department of Computer Science and Engineering", align="center", bold=True, size=24),
        make_paragraph(),
        make_paragraph("Report", align="center", bold=True, size=28),
        make_paragraph("On", align="center", size=24),
        make_paragraph('"SMART CAMPUS INFORMATION SYSTEM APPLICATION"', align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph("Submitted by", align="center", bold=True, size=24),
        make_paragraph("[Name of Student] ([USN])", align="center", size=24),
        make_paragraph("First Year / Second Semester B.E. (CSE)", align="center", size=24),
        make_paragraph("Academic Year 2025-2026", align="center", size=24),
        make_paragraph(),
        make_paragraph("Under the guidance of", align="center", bold=True, size=24),
        make_paragraph("[Faculty In-charge Name]", align="center", size=24),
        make_paragraph("Department of CSE, DSCE", align="center", size=24),
        make_paragraph(),
        make_paragraph("Draft Report Copy", align="center", italic=True, size=22),
        make_paragraph(
            "This draft can be updated with student name, USN, guide name, screenshots, and final page numbering.",
            align="center",
            size=20,
        ),
        make_paragraph(page_break_before=True),
        make_paragraph("CERTIFICATE", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph(
            'This is to certify that the application entitled "SMART CAMPUS INFORMATION SYSTEM APPLICATION" '
            "is a bonafide work carried out by [Name] [USN] during the Python Programming Laboratory sessions "
            "in the academic year 2025-2026.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "The report is submitted in partial fulfillment of the laboratory requirements for the Smart Campus "
            "mini project integration.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph("Faculty In-charge: ____________________", size=22),
        make_paragraph("Head of Department: ____________________", size=22),
        make_paragraph("Date: ____________________", size=22),
        make_paragraph(page_break_before=True),
        make_paragraph("CONTENTS", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph("1. Abstract", size=22),
        make_paragraph("2. Technologies Used", size=22),
        make_paragraph("3. Introduction", size=22),
        make_paragraph("4. Methodology", size=22),
        make_paragraph("5. Results", size=22),
        make_paragraph("6. Conclusion", size=22),
        make_paragraph("7. References", size=22),
        make_paragraph(page_break_before=True),
        make_paragraph("ABSTRACT", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph(
            "The Smart Campus Information System is a Python-based mini project developed to simplify routine "
            "academic administration tasks such as student registration, course enrollment, academic record "
            "maintenance, searching and sorting of student data, fee calculation, file storage, directory "
            "scanning, and performance analysis.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "The application integrates all laboratory programs into a single menu-driven console system. "
            "It reduces manual work, improves accuracy, and demonstrates how fundamental Python concepts such "
            "as conditional statements, loops, functions, lists, dictionaries, sets, file handling, exception "
            "handling, and data analytics libraries can be combined to solve a real campus management problem.",
            size=22,
        ),
        make_paragraph(page_break_before=True),
        make_paragraph("TECHNOLOGIES USED", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph("1. Python 3 for application development.", size=22),
        make_paragraph("2. Built-in modules: csv and os.", size=22),
        make_paragraph("3. Data structures: lists, dictionaries, tuples, and sets.", size=22),
        make_paragraph("4. Functional concepts: user-defined functions and modular programming.", size=22),
        make_paragraph("5. Exception handling for invalid paths and empty folders.", size=22),
        make_paragraph("6. NumPy for numerical analysis.", size=22),
        make_paragraph("7. Pandas for tabular data processing.", size=22),
        make_paragraph("8. Matplotlib for chart generation and performance visualization.", size=22),
        make_paragraph(page_break_before=True),
        make_paragraph("INTRODUCTION", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph(
            "Educational institutions manage a large amount of student-related information every day. "
            "When registration, course allocation, records, and performance tracking are handled manually, "
            "the process becomes slow and error-prone. A simple software-based system can organize this "
            "information more effectively and help administrative staff work with better accuracy.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "The Smart Campus Information System was designed as an integrated laboratory application to address "
            "these needs. It combines the concepts learned in Python Programming Laboratory and presents them "
            "through a single dashboard. The project shows how Python can be used not only for basic programs "
            "but also for building a practical academic support application.",
            size=22,
        ),
        make_paragraph(page_break_before=True),
        make_paragraph("METHODOLOGY", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph(
            "The development of the Smart Campus Information System followed a modular approach. Each lab program "
            "was first implemented as an individual feature and later integrated into one consolidated system.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "1. Student Registration and Grade Evaluation: The program accepts student details such as name, age, "
            "and marks. Conditional statements are used to assign grades and performance remarks.",
            size=22,
        ),
        make_paragraph(
            "2. Course Enrollment Management: A loop-based module allows the administrator to add up to five "
            "courses for a student. Invalid entries are skipped using validation and control statements.",
            size=22,
        ),
        make_paragraph(
            "3. Student Records Management: Student details are stored using a list of dictionaries. This helps "
            "in managing multiple records in a structured way.",
            size=22,
        ),
        make_paragraph(
            "4. Event Participation Analysis: Sets are used to compare students participating in different campus "
            "events and to identify common and unique participants.",
            size=22,
        ),
        make_paragraph(
            "5. Sorting and Searching: Student IDs are arranged using Bubble Sort and Selection Sort. Linear "
            "Search and Binary Search are used to locate a required ID efficiently.",
            size=22,
        ),
        make_paragraph(
            "6. Fee Calculation: User-defined functions are used to compute tuition, hostel, and transportation "
            "charges and generate the total fee for each student.",
            size=22,
        ),
        make_paragraph(
            "7. File Handling: Student academic records are written to and read from a CSV file. The stored data "
            "is processed to calculate average marks and identify the top-performing student.",
            size=22,
        ),
        make_paragraph(
            "8. Directory Scanning: The os module and exception handling are used to display folder structures and "
            "handle missing directories or empty folders safely.",
            size=22,
        ),
        make_paragraph(
            "9. Performance Analytics: NumPy, Pandas, and Matplotlib are used to analyze subject-wise marks and "
            "generate charts for performance comparison.",
            size=22,
        ),
        make_paragraph(
            "10. Main Dashboard Integration: All modules are connected through a single menu-driven application "
            "so that the user can access every feature from one interface.",
            size=22,
        ),
        make_paragraph(page_break_before=True),
        make_paragraph("RESULTS", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph(
            "The final integrated application was implemented successfully as a Python console program named "
            '"smart_campus.py". The system allows the user to register students, evaluate grades, enroll courses, '
            "display records, analyze event participation, sort and search student IDs, calculate fees, manage "
            "academic record files, scan directories, and perform performance analytics.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "During testing, the program compiled successfully and the menu-driven flow worked as intended. "
            "The analytics module produces subject-wise summaries and saves graphical output files such as "
            '"average_scores.png" and "student_performance_comparison.png".',
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "The result demonstrates that all individual lab exercises can be integrated into one practical mini "
            "project. The application is suitable as a draft academic prototype for smart campus data handling.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "Suggested additions for the final submission: insert screenshots of program execution, add actual "
            "student details on the cover page, and update faculty information and examiner signatures.",
            size=22,
        ),
        make_paragraph(page_break_before=True),
        make_paragraph("CONCLUSION", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph(
            "The Smart Campus Information System successfully brings together the important programming concepts "
            "covered in the Python laboratory. It shows how a problem can be broken into smaller modules and then "
            "integrated into a complete working application.",
            size=22,
        ),
        make_paragraph(),
        make_paragraph(
            "The project improves the efficiency of handling academic data and provides a clear demonstration of "
            "core Python skills including decision making, looping, data structures, functions, file handling, "
            "exception handling, and data analytics. With additional user interface enhancements and database "
            "integration, the same system can be extended into a more advanced campus management solution.",
            size=22,
        ),
        make_paragraph(page_break_before=True),
        make_paragraph("REFERENCES", align="center", bold=True, size=28),
        make_paragraph(),
        make_paragraph("1. Python Programming Laboratory Manual, Dayananda Sagar College of Engineering.", size=22),
        make_paragraph("2. Python Software Foundation. Python 3 Documentation. https://docs.python.org/3/", size=22),
        make_paragraph("3. NumPy Documentation. https://numpy.org/doc/", size=22),
        make_paragraph("4. Pandas Documentation. https://pandas.pydata.org/docs/", size=22),
        make_paragraph("5. Matplotlib Documentation. https://matplotlib.org/stable/users/index.html", size=22),
    ]

    body = "".join(paragraphs)
    sect = (
        '<w:sectPr>'
        '<w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="720" w:footer="720" w:gutter="0"/>'
        "</w:sectPr>"
    )

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}{sect}</w:body>"
        "</w:document>"
    )


def build_content_types_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


def build_rels_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


def build_core_xml():
    created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Smart Campus Information System Application Draft Report</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{created}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{created}</dcterms:modified>
</cp:coreProperties>
"""


def build_app_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
"""


def create_docx():
    with zipfile.ZipFile(OUTPUT_FILE, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", build_content_types_xml())
        docx.writestr("_rels/.rels", build_rels_xml())
        docx.writestr("docProps/core.xml", build_core_xml())
        docx.writestr("docProps/app.xml", build_app_xml())
        docx.writestr("word/document.xml", build_document_xml())


if __name__ == "__main__":
    create_docx()
    print(f"Created {OUTPUT_FILE.resolve()}")
