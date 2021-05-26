# fampay
prerequisite - should have Docker installed in your system.
1. First go to the folder which contains Dockerfile then run this command - sudo docker build . -t fampay
2. After running this command run this - sudo docker run -it -p 8000:8000 fampay
3. Now you can run the application on localhost at 8000 port.
4. url for list api is - /api/get_list/ and for search - /api/serach/
