github = "~/GitHub/brendancooley.github.io/"
github_source = "~/GitHub/website"

cv_path = "~/Dropbox\ \(Princeton\)/5_CV/Cooley_cv.pdf"

def task_build():
	yield {
		'name': "building...",
		'actions': ['cp -a ' + cv_path + " static/docs",
					'rm -rf public/',
					'hugo',
					'rm -rf ' + github + "*",
					'cp -a public/ ' + github,
					'cp -a . ' + github_source],
	}