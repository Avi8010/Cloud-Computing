import webapp2

class MainPage(webapp2.RequestHandler):
      def get(self):
          a=10
          for i in range(1,11):
               self.response.write(str(a) + " X " + str(i) + " = " + str(i*10)+"<br>")
               
               
app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
