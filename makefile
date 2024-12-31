file: 
	git add .
	git commit -m "small update"
	git push origin main

all: 
	git add .
	git commit -m "$(filter-out $@,$(MAKECMDGOALS))" # adding message 
	git push origin main