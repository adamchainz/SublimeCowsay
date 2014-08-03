# coding=utf-8
import sublime
import sublime_plugin
import subprocess


class CowsayTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()

        if len(sel) != 1 or sel[0].size() == 0:
            return

        text = view.substr(sel[0])

        cursor = min(sel[0].a, sel[0].b)

        text = cowsayize(text)

        view.erase(edit, sel[0])
        view.insert(edit, cursor, text)
        sel.clear()
        sel.add(sublime.Region(cursor, cursor + len(text)))


def cowsayize(string):
    command = ['cowsay', string]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    return out.decode('utf-8')
