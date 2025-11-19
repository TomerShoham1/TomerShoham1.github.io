import bibtexparser
import os

def create_publication_files(bib_file_path, output_dir):
    print(f"Starting to process {bib_file_path}")
    try:
        with open(bib_file_path, 'r', encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
    except Exception as e:
        print(f"Error reading or parsing the bib file: {e}")
        return

    print(f"Found {len(bib_database.entries)} entries in the bib file.")

    for entry in bib_database.entries:
        try:
            # Extract the necessary information
            title = entry.get('title', '')
            authors = entry.get('author', '')
            venue = entry.get('journal') or entry.get('booktitle', '')
            year = entry.get('year', '')
            paperurl = entry.get('url', '') # Assuming the URL is in the 'url' field
            codeurl = '' # No code URL in the bib file
            
            # Create the markdown file content
            md_content = f"""---
title: "{title}"
authors: "{authors}"
venue: "{venue}"
year: "{year}"
paperurl: "{paperurl}"
codeurl: "{codeurl}"
---
"""
            
            # Create the filename
            filename = f"{entry['ID']}.md"
            
            # Write the content to the file
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
            
            print(f"Successfully created {output_path}")

        except Exception as e:
            print(f"Error processing entry {entry.get('ID', 'Unknown')}: {e}")

if __name__ == '__main__':
    bib_file = 'C:/Users/97252/Dropbox/TomerShoham1.github.io/_publications/papers.bib'
    output_directory = 'C:/Users/97252/Dropbox/TomerShoham1.github.io/_publications_md'
    create_publication_files(bib_file, output_directory)
    print(f"Finished creating markdown files in {output_directory}")
