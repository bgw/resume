.PHONY: all clean

all: resume.pdf

%.pdf: %.tex
	latexmk --pdf $<

clean:
	rm -f *.aux *.fdb_latexmk *.log *.out *.pdf
