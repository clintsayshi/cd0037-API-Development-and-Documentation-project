# A Game of Trivia

This project is a web application version of a Trivia game. Users are able to view questions, their answers, view questions by category, search questions, add new questions and play the game. It serves as practice for Udacity students taking the Full Stack Developer course part 3: API Development and Documentation. By completing this project I got to learned and applied skills of structuring and implementing well formatted API endpoints that leverage knowledge of HTTP and API development practices.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 
## Getting started
### Pre-requisites and Local development

Developers using this project should already have python3, pip and node installed on their local machine.

### Backend

From the backend folder run `pip install requirements/txt`. All required packages are included in the requirements file.

To run the application run the commands:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

### Frontend

From the frontend folder, run the following commands to start the client:
```
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on localhost:3000. 

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality. 

## API reference

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling

Errors are returned as JSON objects in the following format:

`
    {
        "success": False,
        "error": 400,
        "message": "bad request"
    }
`

The API will return three error types:
- 400: Bad request
- 404: Resource not found
- 422: Not processable
- 405: Method not allowed

### Endpoints

#### GET /categories

General
    - Returns a list of category objects, success value, and total number of categories
    - Results are paginated in groups of 8. Include a request argument to choose page number, starting from 1.
Sample: curl http://127.0.0.1:5000/categories

`
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true, 
  "total_categories": 6
}
`

#### GET /questions

General
- Returns a list of questions objects, success value, total number of questions, current category and categories
- Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
Sample: curl http://127.0.0.1:5000/questions
`
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": "Sports", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 20
}
`

#### GET /categories/{category_id}/questions

General
- Returns a list of question objects with a categgory that matches {category_id}, success value, total number of questions returned, current category and categories.
- The results are paginated in groups of 10. Include a request argument to choose page number starting from 1.
sample: curl http://12.0.0.1:5000/categories/{category_id}/questions
`
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "current_category": {
    "id": 1,
    "type": "Science"
  },
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}
`

#### POST /questions

General
- Adds a new question using the submitted question, answer, difficulty, and category.
- Returns a success value.
sample: curl -X POST -H "Content-Type:application/json" -d '{"question":"Name of the country?", "answer":"South Africa", "difficulty":"3", "category":"3"}' http://localhost:5000/questions

`
{
  "success": true
}
`

#### POST /questions/search

Genereal
- Returns a list of question objects, success value, and total number of the questions that match a search term.
- The results are paginated in groups of 10. Include a request argument to choose page number starting from 1.
sample: curl -X POST -d '{"search":"organ"}' -H "Content-Type:application/json" http://localhost:5000/questions/search
`
{
  "current_category": "Sports",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    }
  ],
  "success": true,
  "total_questions": 1
}
`

#### POST /quizzes

General
- Returns a random question object and success value
- It takes a list of previous questions and a category
sample: curl -X POST -H "Content-Type:application/json" -d '{"quiz_category":{"type":"Science", "id":"1"}}' http://localhost:5000/quizzes
`
{
  "success": True,
  "question": 
    {
     "id": 20,
     "question": "What is the heaviest organ in the human body?", 
     "answer": "The Liver", 
     "category": 1, 
     "difficulty": 4
    }
}   
`

#### DELETE /questions/{question_id}

General
- Deletes the question of the given ID if it exists.
- Returns the id of the question, and a success value.
sample: curl -X DELETE http://127.0.0.1:5000/questions/2
` 
{
  "success": true
}    
`

## Deployment N/A

## Authors
Clinton Manakane

## Acknowledgements 
The ALX fullstack chat on slack