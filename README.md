Goals of this project
1. Be able to upload a giant online order summary to save items to a database
2. be able to manually add or remove items
3. be able to add recipe links or upload ingredient lists to see if you have the items

Future to dos
1. View past orders
2. track item price changes, rate of item use, most popular recipes
3. Be able to view oldest ingredients
4. save recipes
5. show what recipes you can make with what you have
6. Cost prediction on missing ingredients

Tech Stack:
1. django backend
2. no front end frameworks

Current task:
Implement uploading a PDF to the server

Subtasks
1. FT from the user where they try to upload a PDF
2. UT to simulate going to the file upload page and getting 200
3. UT to check that PDF files get saved
4. UT to check that none pdf files do not get saved
5. UT to check that saving PDF returns a 201 status
6. UT to check that UT returns 400 on non-pdf files