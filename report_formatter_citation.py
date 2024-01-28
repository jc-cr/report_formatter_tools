import re

class BibTeXEntry:
    def __init__(self, entry):
        self.entry = entry
        self.fields = self._parse_entry()

    def _parse_entry(self):
        fields = {}
        lines = self.entry.split('\n')
        for line in lines:
            match = re.match(r'\s*(\w+)\s*=\s*{(.+)}\s*,?', line)
            if match:
                fields[match.group(1)] = match.group(2)
        return fields

    def get_main_author(self):
        authors = self.fields.get('author', 'NAN')
        main_author = authors.split(' and ')[0] if ' and ' in authors else authors
        return main_author

class IEEEFormatter:
    @staticmethod
    def format(entry):
        title = entry.fields.get('title', 'NAN')
        main_author = entry.get_main_author()
        authors = main_author + " et al." if main_author != entry.fields.get('author', '') else main_author
        year = entry.fields.get('year', 'NAN')
        affiliation = 'NAN'  # BibTeX entry does not contain affiliation information

        return f"{title}, {authors}, {year}, {affiliation}"

def main(bibtex_input):
    entry = BibTeXEntry(bibtex_input)
    formatted_entry = IEEEFormatter.format(entry)
    print(formatted_entry)

# Example BibTeX input
bibtex_input = """
@misc{jouppi2017indatacenter,
      title={In-Datacenter Performance Analysis of a Tensor Processing Unit}, 
      author={Norman P. Jouppi and Cliff Young and Nishant Patil and David Patterson and Gaurav Agrawal and Raminder Bajwa and Sarah Bates and Suresh Bhatia and Nan Boden and Al Borchers and Rick Boyle and Pierre-luc Cantin and Clifford Chao and Chris Clark and Jeremy Coriell and Mike Daley and Matt Dau and Jeffrey Dean and Ben Gelb and Tara Vazir Ghaemmaghami and Rajendra Gottipati and William Gulland and Robert Hagmann and C. Richard Ho and Doug Hogberg and John Hu and Robert Hundt and Dan Hurt and Julian Ibarz and Aaron Jaffey and Alek Jaworski and Alexander Kaplan and Harshit Khaitan and Andy Koch and Naveen Kumar and Steve Lacy and James Laudon and James Law and Diemthu Le and Chris Leary and Zhuyuan Liu and Kyle Lucke and Alan Lundin and Gordon MacKean and Adriana Maggiore and Maire Mahony and Kieran Miller and Rahul Nagarajan and Ravi Narayanaswami and Ray Ni and Kathy Nix and Thomas Norrie and Mark Omernick and Narayana Penukonda and Andy Phelps and Jonathan Ross and Matt Ross and Amir Salek and Emad Samadiani and Chris Severn and Gregory Sizikov and Matthew Snelham and Jed Souter and Dan Steinberg and Andy Swing and Mercedes Tan and Gregory Thorson and Bo Tian and Horia Toma and Erick Tuttle and Vijay Vasudevan and Richard Walter and Walter Wang and Eric Wilcox and Doe Hyun Yoon},
      year={2017},
      eprint={1704.04760},
      archivePrefix={arXiv},
      primaryClass={cs.AR}
}
"""

main(bibtex_input)
