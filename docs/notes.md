## NOTES


<details>
<Summary> Pycharm </Summary> 

- create new project
- create `/docs, /test, /reports` folders
- create `/<module-name>` folder
- in `<module-name>` folder create
  - __init__.py (can be empty initially)
  - main.py
  - in main.py reference <module-name>.main:app:
       ``` uvicorn.run("trade-assistant.main:app", host="127.0.0.1", port=8000)    ```
  - in `test_main.py` import main: `from <module-name>.main.py import app`
  - in terminal check it works `python -m trade-assistant.main`
    - check openAPI interface is working `http://127.0.0.1:8000/docs`
    - use postman to test (fastAPI expects data in the request body not in the URL, so postman used to send JSON string in the request)
  - check the unit tests work `python -m pytest --cov=trade_assistant --cov-report=xml --junitxml=reports/xunit-result.xml`
  - Add to GITHub
    - Menu: VCS  -> Enable Version Control Integration. Choose Git as the Version Control System and click OK
    - 

pen_spark


</details>

<details>
<Summary> Branching Model </Summary> 

- use GitFlow
- 

</details>


<details>
<Summary> GITHub </Summary> 

- setup repo with `master` branch
- make it 'public` so SonarCube can connect to it
- create `develop` branch
-
</details>



<details>
<Summary> SonarCloud </Summary> 

- generate token from Sonarcloud account
  - `My Account -> Security -> Generate Token`
  - Provide a name: `github-actions-token`
  - copy token
- add token to GitHub 
  - `Settings -> Secrets and Variables -> Repository Secrets -> New Repository Secret`
  - Name the secret SONAR_TOKEN and paste the token value from SonarCloud.
- 



</details>

<details>
<Summary> Code </Summary> 

- aaa
- bbb

</details>

<details>
<Summary> Postman </Summary> 

- download desktop version (so it can getto localhost easily)
  - post a URL 'http://127.0.0.1:8000/calculate`
  - under 'Body' select JSON and paste in:
    - `{
  "num1": 2,
  "num2": 5,
  "operation": "multiply"
}`

</details>
