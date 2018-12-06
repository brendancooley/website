github = ~/GitHub/brendancooley.github.io/
github_source = ~/GitHub/website

post:
	rm -rf public/;
	hugo;
	rm -rf $(github)$`*;
	cp -a public/ $(github)$;
	cp -a . $(github_source)

.PHONY: post