# LinkedInScrapUsingAPI
Proxyurl is used to scrape data of person from LinkedIn without logging into LinkedIn

The response will be in json format which we can parse according to our requirements.

Steps:
1. Search for https://nubela.co/proxycurl/

![image](https://github.com/user-attachments/assets/bf45c963-1231-4815-9c23-3d1727cd1b1d)

2. Scroll down in page, you'll see the box to enter your mail id to get free trial API.
3. Enter the creds and proceed, follow the instructions.
4. Once account is created, you'll see API key and 10 credits.

![image](https://github.com/user-attachments/assets/dc854600-1d03-4762-a0bb-a3011616f270)

5. Now copy your API and scroll down in Data Freshness box, you'll see "Make pulling fresh data the default for Person Profile Endpoint?". Click on the same to get the endpoint.
6. In right half, you'll see Shell and Python, select Python there.

![image](https://github.com/user-attachments/assets/ab95c337-1d03-4da6-9714-e05c9ad58c35)

7. Copy the same Python code to your IDE (Eg: Visual Studio Code), in params keep only 'linkedin_profile_url' and remove rest of the parameters.
8. Give proper api_key which you have copied in step 5, give proper 'linkedin_profile_url' value and run your code.
9. You'll get json output containing all the information about the 'linkedin_profile_url' you have passed, you can parse the data and use it in your desired way by storing in Dataframe or excel file.
