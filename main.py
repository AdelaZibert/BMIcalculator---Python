#!/usr/bin/env python
#-*-coding: utf-8 -*-

import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("index.html")
        return self.response.write(template.render())

    def post(self):
        h = float(self.request.get("h"))
        w = float(self.request.get("w"))

        bmi = w/((h/100)*(h/100))
        message = "Your BMI is %.1f" % bmi

        if bmi > 24.9:
            weight = "You're too heavy!"
        elif bmi < 18:
            weight = "You're too skinny!"
        else:
            weight = "Your weight is healthy!"

        template = jinja_env.get_template("index.html")
        return self.response.write(template.render({"bmi": message, "weight": weight}))


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler)
], debug=True)
