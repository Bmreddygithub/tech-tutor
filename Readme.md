pip3 install -r requirements.txt

create a api key @ https://console.groq.com
its free 

create a env .env to save the key 

.env

GROQ_API_KEY=your_api_key_here


run> python3 main.py

to run the test cases :

>  python3 test_cases/runtime_error.py >test1.log
>  python3 test_cases/logic_error.py >test2.log 
>  python3 test_cases/syntax_error.py  >test3.log 
>  python3 test_cases/index_error.py  >test4.log 
>  python3 test_cases/type_error.py  >test5.log 
