import os
from loja import app
import os

def main():
      port = int(os.environ.get("PORT", 5000))
      app.run(host="0.0.0.0", port=port)

if __name__ =="__main__":         
      main()
    
    
    