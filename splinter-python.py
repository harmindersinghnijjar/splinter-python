# Import the Browser class from the splinter library
from splinter import Browser

# Create an instance of the Browser class
browser = Browser('chrome')

# Visit the google website
browser.visit('http://google.com')

# Fill out the search form with the desired query and submit it
browser.fill('q', 'splinter - python acceptance testing for web applications')
browser.find_by_name('btnK').click()

# Check if the official splinter website is present in the search results
if browser.is_text_present('splinter.readthedocs.io'):
    # If the website is present, print a success message
    print("Yes, the official website was found!")
else:
    # If the website is not present, print a message suggesting to improve SEO
    print("No, it wasn't found... We need to improve our SEO techniques")

# Close the browser
browser.quit()
