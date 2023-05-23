import webapp2

class MainPage(webapp2.RequestHandler):
   def get(self):
       for i in range(6):
           self.response.write("Name: abcd <br>")
           self.response.write("seat No: 12345 <br>")
           self.response.write("Dept: IT <br>")
           self.response.write('<br>')
           
app = webapp2.WSGIApplication([('/', MainPage)],debug=True)


