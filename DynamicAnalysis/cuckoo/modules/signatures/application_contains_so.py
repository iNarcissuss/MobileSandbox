# Copyright (C) Check Point Software Technologies LTD.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.
import os

from lib.cuckoo.common.abstracts import Signature




class Hidden_Payload(Signature):
    name = "application_contains_so"
    description = "Application Contains Shared Object Files (Static)"
    severity = 2
    categories = ["android"]
    authors = ["idanr1986"]
    minimum = "0.5"

    def run(self):
        try:
            for file in self.results["apkinfo"]["files_flaged"]["so"]:
                self.add_match(None,file["name"], file)
            return self.has_matches()

        except:
            return False
