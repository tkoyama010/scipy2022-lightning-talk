# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile revealjs

revealjs:
	@$(SPHINXBUILD) -M revealjs "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -D language="ja"
	mv $(BUILDDIR)/revealjs/main.html $(BUILDDIR)/revealjs/main-ja.html
	@$(SPHINXBUILD) -M revealjs "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	mv $(BUILDDIR)/revealjs/main.html $(BUILDDIR)/revealjs/main-en.html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
