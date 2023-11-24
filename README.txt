Using python 2.7.......

To run the test webserver, run the following command:

python testserver.py


Navigate to: http://localhost:8080/index.html?contenttype=text/html

------------------
STEPS [by karthik]:
1.upload all the files [shared by Richard] in the node which you want to run the Cross Origin iFrame test
2.Run the Web-Server by below command in same node
python testserver.py
3.open the localhost page in the same node in a Firefox browser
http://localhost:8080/index.html?contenttype=text/html
4.open the Network inspect tools
5.Click on the Buttons required
6.Copy the GET url of that request
7.use the copied URL in a Catchpoint test properties [as test URL/ script]
8.Enable/Disable the Cross-Origin-iFrame option
9.verify the results between Chrome and Playwright.
10.test will pass if option is not selected, test will fails if option is selected.
