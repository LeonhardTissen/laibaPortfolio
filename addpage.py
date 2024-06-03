from flask import Flask, render_template, request
import os

app = Flask(__name__)

categories = {
	"worktype": [
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
	"niches": [
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
		{
			"tag": "food",
			"display": "Food"
		},
		{
			"tag": "pets",
			"display": "Pets"
		}
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
			"display": "Adapty.io",
			"tag": "adaptyio"
		},
		{
			"display": "Simple Holistic Wellbeing",
			"tag": "simple_holistic_wellbeing"
		},
		{
			"display": "Stanton Financial Co.",
			"tag": "stanton_financial"
		},
		{
			"display": "Jetsetter Journals",
			"tag": "jetsetter_journals"
		},
		{
			"display": "Premier Dental",
			"tag": "premier_dental"
		},
	]
}

@app.route("/")
def index():
	niches = categories["niches"]
	recruiters = categories["recruiters"]
	business = categories["business"]
	worktype = categories["worktype"]

	subdirectories = os.walk("src/assets/imgs/works_src").__next__()[1]
	subdirectories = [f"/{subdirectory}/" for subdirectory in subdirectories if subdirectory != ""]
	subdirectories.insert(0, "/")

	return render_template("index.html.j2", niches=niches, recruiters=recruiters, business=business, worktype=worktype, subdirectories=subdirectories)

@app.route("/add_post", methods=["POST"])
def add_post():
	# Add post to database
	formdata = request.form
	niches = formdata.getlist("niches")
	niches_display = [category["display"] for category in categories["niches"] if category["tag"] in niches]
	business = formdata.getlist("business")
	business_display = [category["display"] for category in categories["business"] if category["tag"] in business]
	recruiter = formdata.get("recruiter")
	recruiter_display = [category["display"] for category in categories["recruiters"] if category["tag"] == recruiter][0]
	worktype = formdata.get("worktype")
	worktype_display = [category["display"] for category in categories["worktype"] if category["tag"] == worktype][0]
	location = formdata.get("location")
	# Save image there
	full_location = 'src/assets/imgs/works_src' + location
	os.makedirs(full_location, exist_ok=True)
	image = request.files["image"]
	image.save(os.path.join(full_location, image.filename))
	os.system(f"python optimize.py")
	absolute_image_path = f"./assets/imgs/works{location}{image.filename.split('.')[0]}.jpg"


	title = formdata.get("title")
	url = formdata.get("url")

	tags = niches + business + [recruiter, worktype]
	display = niches_display + business_display + [recruiter_display, worktype_display]

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

	print(html)
	html_with_tabs = html.replace("\n", "\n\t\t\t\t")

	with open('src/index.ejs', 'r') as file:
		file_contents = file.read()

	with open('src/index.ejs', 'w') as file:
		com = "<!-- ADD.PY INSERT -->" 
		new_file_contents = file_contents.replace(com, f"{com}\n\t\t\t\t{html_with_tabs}")
		file.write(new_file_contents)

	return "Post added successfully!"

if __name__ == "__main__":
	app.run(port=5000, debug=True)
