import sublime
import sublime_plugin

import json
import pathlib


def hl(length=80):
    """Horizontal line."""
    return ";; " + ("-" * length)


class PgClojureDocsSearchCommand(sublime_plugin.WindowCommand):
    """
    Command to search for examples in ClojureDocs.
    """

    def run(self):
        clojuredocs = None

        try:

            with open(
                pathlib.PurePath(sublime.packages_path(), "ClojureDocs", "clojuredocs.json")
            ) as file:
                clojuredocs = json.load(file)

        except:
            clojuredocs = {}

        quick_panel_items = []

        for v in clojuredocs.get("vars"):
            arglists = ["[" + arg + "]" for arg in v.get("arglists", [])]
            arglists = " ".join(arglists)

            quick_panel_items.append(
                sublime.QuickPanelItem(
                    v.get("ns", "") + "/" + v.get("name", ""),
                    details=arglists,
                ),
            )

        def on_done(index):
            if index != -1:
                v = clojuredocs.get("vars")[index]

                var_name = ";; " + v.get("ns") + "/" + v.get("name") + " "

                arglists = ["[" + arg + "]" for arg in v.get("arglists", [])]
                arglists = " ".join(arglists)
                arglists = arglists + "\n;;\n" if arglists else ""

                docstring = v.get("doc") if v.get("doc") else ""
                docstring = "\n".join([";; " + line for line in docstring.split("\n")])

                examples = v.get("examples") or []
                examples = [
                    example.get("body") for example in examples if example.get("body")
                ]
                examples = "\n\n".join(examples)

                see_alsos = v.get("see-alsos") or []
                see_alsos = [
                    ";; " + see_also["to-var"]["ns"] + "/" + see_also["to-var"]["name"]
                    for see_also in see_alsos
                ]
                see_alsos = "\n".join(see_alsos)

                content = var_name
                content = content + arglists
                content = content + docstring
                content = content + "\n" + hl() + "\n\n"
                content = content + examples

                if see_alsos:
                    content = content + "\n\n\n" + hl() + "\n\n"
                    content = content + ";; See also:\n;;\n"
                    content = content + see_alsos

                view = self.window.new_file()
                view.set_name("ClojureDocs")
                view.set_scratch(True)
                view.set_read_only(False)
                view.assign_syntax("scope:source.clojure")
                view.settings().set("line_numbers", False)
                view.settings().set("gutter", False)
                view.settings().set("is_widget", False)
                view.run_command(
                    "append",
                    {
                        "characters": content,
                    },
                )
                view.set_read_only(True)

        self.window.show_quick_panel(
            quick_panel_items,
            on_done,
        )
