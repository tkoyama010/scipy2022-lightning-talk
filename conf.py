# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------
import os

# -- Project information -----------------------------------------------------
project = "Scipy2022 lightning talk"
copyright = "2022, "
author = "Tetsuo Koyama"
version = ""
release = "0.1"

# # -- pyvista configuration ---------------------------------------------------
# import pyvista
# 
# # Manage errors
# pyvista.set_error_output_file("errors.txt")
# # Ensure that offscreen rendering is used for docs generation
# pyvista.OFF_SCREEN = True  # Not necessary - simply an insurance policy
# # Preferred plotting style for documentation
# pyvista.set_plot_theme("document")
# pyvista.global_theme.window_size = [1024, 768]
# pyvista.global_theme.font.size = 22
# pyvista.global_theme.font.label_size = 22
# pyvista.global_theme.font.title_size = 22
# pyvista.global_theme.return_cpos = False
# pyvista.set_jupyter_backend(None)
# # Save figures in specified directory
# pyvista.FIGURE_PATH = os.path.join(os.path.abspath("./images/"), "auto-generated/")
# if not os.path.exists(pyvista.FIGURE_PATH):
#     os.makedirs(pyvista.FIGURE_PATH)
# 
# # necessary when building the sphinx gallery
# pyvista.BUILDING_GALLERY = True
# os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'
# 
# # SG warnings
# import warnings
# 
# warnings.filterwarnings(
#     "ignore",
#     category=UserWarning,
#     message="Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.",
# )


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_revealjs",
    "sphinxcontrib.budoux",
    "sphinxcontrib.gtagjs",
    "sphinxcontrib.oembed",
    "sphinxemoji.sphinxemoji",
#   "jupyter_sphinx",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
locale_dirs = ["_locales"]
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "_sections"]
pygments_style = None

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_theme_options = {
    "revealjs_theme": "league",
}
html_static_path = ["_static"]

# -- Options for Reveal.js output ---------------------------------------------
revealjs_static_path = ["_static"]
revealjs_style_theme = "moon"
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "center": True,
    "transition": "slide",
}
revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs4/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs4/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs4/plugin/math/math.js",
    },
]
revealjs_css_files = [
    "revealjs4/plugin/highlight/zenburn.css",
    "custom.css",
]
revealjs_notes_from_comments = True

# -- Options for HTMLHelp output ---------------------------------------------
htmlhelp_basename = "sphinx-revealjsdoc"

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}
latex_documents = [
    (
        master_doc,
        "sphinx-revealjs.tex",
        "sphinx-revealjs Documentation",
        "Kazuya Takei",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, "sphinx-revealjs", "sphinx-revealjs Documentation", [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        master_doc,
        "sphinx-revealjs",
        "sphinx-revealjs Documentation",
        author,
        "sphinx-revealjs",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_exclude_files = ["search.html"]

# -- Options for extensions --------------------------------------------------
todo_include_todos = True

if "GTAGJS_IDS" in os.environ:
    gtagjs_ids = os.environ["GTAGJS_IDS"].split(",")

budoux_targets = ["h1", "h2", "h3"]
