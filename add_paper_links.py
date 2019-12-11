import os
import csv


"""
TO USE:
    1) Download the camera ready papers from CMT and place in assets/papers
    2) Filter to only the accepted papers in CMT and download submissions as TSV
    3) Set ACCEPTED_PAPERS_TSV variable to the path to the downloaded TSV
    4) Run python add_paper_links.py

"""

ACCEPTED_PAPERS_TSV = os.path.expanduser("~/Downloads/accepted_papers_sosp19.tsv")

assets_dir = "assets/papers"

paper_files = os.listdir(assets_dir)


def get_asset(paper_id):
    asset = list(filter(lambda x: x.startswith(f"{paper_id}\\"), paper_files))
    assert len(asset) <= 1
    if len(asset) == 1:
        return os.path.join(assets_dir, asset[0])
    return None


with open(ACCEPTED_PAPERS_TSV, "r", newline='') as f:
    with open("acceptedpapers.md", "w") as mdfile:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            paper_id = row["Paper ID"]
            title = row["Paper Title"]
            author_names = row["Author Names"]
            authors = row["Authors"].replace("*", "")
            asset = get_asset(paper_id)
            if asset is not None:
                entry = f"[**{title}**]({asset}): {authors}\n\n"
            else:
                entry = f"**{title}**: {authors}\n\n"
            mdfile.write(entry)
