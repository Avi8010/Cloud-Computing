import webapp2

class MainPage(webapp2.RequestHandler):
      def get(self):
          a=5
          for i in range(1,11):
               self.response.write(str(a) + " X " + str(i) + " = " + str(i*5)+"<br>")
               
               
app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
               
