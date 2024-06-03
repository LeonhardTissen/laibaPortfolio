import os

class color:
	red: str = "\033[91m"
	green: str = "\033[92m"
	yellow: str = "\033[93m"
	blue: str = "\033[94m"
	purple: str = "\033[95m"
	white: str = "\033[97m"

# Categories are split into writing, marketing, business, and recruiters
# - tag is used internally for searching
# - display is visible to the user
# Feel free to extend the categories

categories = {
	"writing": [
		{
			"tag": "seo_writing",
			"display": "SEO Writing"
		},
		{
			"tag": "script_writing",
			"display": "YouTube Script Writing"
		},
		{
			"tag": "blog_writing",
			"display": "Blog Writing"
		}
	],
	"marketing": [
		{
			"tag": "b2b",
			"display": "B2B"
		},
		{
			"tag": "tech",
			"display": "Tech"
		},
		{
			"tag": "travel",
			"display": "Travel"
		},
		{
			"tag": "health",
			"display": "Health"
		},
		{
			"tag": "wellness",
			"display": "Wellness"
		},
		{
			"tag": "lifestyle",
			"display": "Lifestyle"
		},
	],
	"business": [
		{
			"display": "Legal Business",
			"tag": "legal_business"
		},
		{
			"display": "Business",
			"tag": "business"
		},
		{
			"display": "Personal Finance",
			"tag": "personal_finance"
		},
		{
			"display": "Personal Finance (taxes)",
			"tag": "personal_finance"
		},
	],
	"recruiters": [
		{
			"display": "Adapty.io"
		},
		{
			"display": "Simple Holistic Wellbeing"
		},
		{
			"display": "Stanton Financial Co."
		},
		{
			"display": "Jetsetter Journals"
		},
		{
			"display": "Premier Dental"
		},
	]
}

def prefer_display(item):
	# Input is just a string
	if isinstance(item, str):
		return item
	# Prefer display over tag
	if "display" in item:
		return item["display"]
	if "tag" in item:
		return item["tag"]
	return 'Unknown'

# Ask the user to pick a choice from an array
def choice_picker(text, array):
	print(f"{color.purple}{text}:")

	for index, item in enumerate(array):
		print(f"{color.blue}{index + 1}. {prefer_display(item)}")
	
	print(f"{color.yellow}Enter the number with your choice (e.g. 1)")

	choice = get_input()
	
	if not choice:
		return None
	
	return array[int(choice) - 1]

# Ask the user to pick multiple choices from an array
def multiple_choice_picker(text, array):
	print(f"{color.purple}{text}:")

	for index, item in enumerate(array):
		print(f"{color.blue}{index + 1}. {prefer_display(item)}")
	
	print(f"{color.yellow}Enter the numbers with your choice (e.g. 123)")

	choice = get_input()
	
	if not choice:
		return []
	
	choices = []
	for index in choice:
		choices.append(array[int(index) - 1])

	return choices

def get_input():
	return input(f"{color.white}> ").strip()



def pick_image():
	print(f"{color.purple}Drag an image file to the terminal and press Enter.")

	file_path = get_input()

	if not file_path:
		print(f"{color.red}No file path provided. Exiting...")
		exit()
	
	if not os.path.exists(file_path.replace("'", "")):
		print(f"{color.red}File does not exist. Exiting...")
		exit()

	return file_path

def get_image():
	image_src_path = pick_image()

	# Get subdirectories
	subdirectories = os.walk("src/assets/imgs/works_src").__next__()[1]
	subdirectories = [f"/{subdirectory}/" for subdirectory in subdirectories if subdirectory != ""]
	subdirectories.insert(0, "/")

	subdirectory = choice_picker("Choose a subdirectory to put image in", subdirectories)

	if not subdirectory:
		print(f"{color.red}No subdirectory chosen. Exiting...")
		exit()
	
	os.system(f"cp {image_src_path} src/assets/imgs/works_src{subdirectory}")

	os.system("python3 optimize.py")

	# Return the image path
	return f"src/assets/imgs/works{subdirectory}{os.path.basename(image_src_path).split('.')[0]}.jpg"

def get_url():
	print(f"{color.purple}Enter the URL:")

	url = get_input()

	if not url:
		print(f"{color.red}No URL provided. Exiting...")
		exit()

	url = url.replace("https://", "//").replace("http://", "//")

	return url

def get_title():
	print(f"{color.purple}Enter the title:")

	title = get_input()

	if not title:
		print(f"{color.red}No title provided. Exiting...")
		exit()

	return title

def build_html(tags, display, image, url, title):
	absolute_image_path = image.replace("src/", "./")
	html = f"""
<a class="work" data-categories="{" ".join(tags)}" href="{url}">
	<div class="img-container">
		<img loading="lazy" src="<%= require('{absolute_image_path}') %>">
	</div>
	<div class="work-text">
		<h2>{title}</h2>
		<p>{" • ".join(display)}</p>
	</div>
</a>
	"""
	return html	


###################################################################################################
print(f"{color.yellow}<< Starting >>")
###################################################################################################



image = get_image()
writing_categories = multiple_choice_picker("Choose writing category", categories["writing"])
marketing_categories = multiple_choice_picker("Choose marketing category", categories["marketing"])
business_categories = multiple_choice_picker("Choose business category", categories["business"])
recruiter = choice_picker("Choose recruiter", categories["recruiters"])
url = get_url()
title = get_title()

tags = []
display = []
for category in [writing_categories, marketing_categories, business_categories]:
	for item in category:
		if "display" in item:
			display.append(item["display"])
		if "tag" in item:
			tags.append(item["tag"])

if recruiter:
	display.append(recruiter["display"])

html = build_html(tags, display, image, url, title)
html_with_tabs = html.replace("\n", "\n\t\t\t\t")

with open('src/index.ejs', 'r') as file:
	file_contents = file.read()

with open('src/index.ejs', 'w') as file:
	com = "<!-- ADD.PY INSERT -->" 
	new_file_contents = file_contents.replace(com, f"{com}\n\t\t\t\t{html_with_tabs}")
	file.write(new_file_contents)




print(html)

###################################################################################################
print(f"{color.green}Done!")
###################################################################################################
