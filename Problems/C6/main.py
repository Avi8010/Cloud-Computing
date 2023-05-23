import webapp2
class MainPage(webapp2.RequestHandler):
      def get(self):
          a,b=0,1
          for i in range(1,9):
             self.response.write(str(a)+"<br>")
             a,b=b,a+b
app=webapp2.WSGIApplication([('/',MainPage)], debug=True)
