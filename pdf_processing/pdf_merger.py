import PyPDF2
import sys

def get_input():
    if len(sys.argv) < 2:
        return "[!]Please enter files to be merged as arguements."
    else:
        for args in sys.argv:
            args = str(args)
            return(sys.argv[1:])


def merge_pdf(list = []):
    if list:
        merger = PyPDF2.PdfFileMerger()
        for pdf in list:
            try:
                merger.append(pdf)
            except FileNotFoundError:
                return "[!]File not found. Recheck The FileName."
            except AttributeError:
                return "[!]Enter a string as the Filename."
        merger.write('merged.pdf')
        return "File Merge Successful."
    else:
        return "[!]Please enter a list."

print(merge_pdf(get_input()))