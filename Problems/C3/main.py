import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
         a=10
         while(a>0):
             self.response.write("seat No: 1234 <br>")
             self.response.write("dept: IT <br>")
             self.response.write("<br>")
             a-=1
        
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
