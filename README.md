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

```
{
  "success": False,
  "error": 400,
  "message": "bad request"
}
```

The API will return three error types:
- 400: Bad request
- 404: Resource not found
- 422: Not processable
- 405: Method not allowed
- 500: Internal server error

### Endpoints

#### GET /categories

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns an object with the keys:
  - categories, that contains an object of id: category_string key: value pairs.
  - success, that contains a boolean value
  - total_categories, that contains total number of categories returned

Sample: curl http://127.0.0.1:5000/categories
```
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
```

#### GET '/questions?page=${integer}'

- Fetches a paginated set of questions, a total number of questions, all categories and current category string.
- Request Arguments: page - integer
- Returns: An object with a success value, 10 paginated questions, total questions, object including all categories, and current category string

Sample: curl http://127.0.0.1:5000/questions
```
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
```

#### GET '/categories/${id}/questions'

- Fetches questions for a cateogry specified by id request argument
- Request Arguments: id - integer and page - integer
- Returns: An object with questions for the specified category, total questions, and current category string.

sample: curl http://12.0.0.1:5000/categories/{category_id}/questions
```
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
```

#### POST '/questions'

General
- Sends a post request in order to add a new question.
- Request Body:
```
{
    'question':  'Heres a new question string',
    'answer':  'Heres a new answer string',
    'difficulty': 1,
    'category': 3,
}
```
- Returns an object with a single key `success`

sample: curl -X POST -H "Content-Type:application/json" -d '{"question":"Name of the country?", "answer":"South Africa", "difficulty":"3", "category":"3"}' http://localhost:5000/questions

```
{
  "success": true
}
```

#### POST '/questions/search'

- Sends a post request in order to search for a specific question by search term
- Request Body:
```
{
    'searchTerm': 'this is the term the user is looking for'
}
```
- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string

sample: curl -X POST -d '{"search":"organ"}' -H "Content-Type:application/json" http://localhost:5000/questions/search
```
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
```

#### POST '/quizzes'

- Sends a post request in order to get the next question
- Request Body:
```
{
    'previous_questions': [1, 4, 20, 15]
    quiz_category': 'current category'
 }
```
- Request Arguments: None
- Returns: a single new question object

sample: curl -X POST -H "Content-Type:application/json" -d '{"quiz_category":{"type":"Science", "id":"1"}}' http://localhost:5000/quizzes
```
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
```

#### DELETE '/questions/${id}'

- Deletes a specified question using the id of the question.
- Request Arguments: `id` - integer
- Returns an object with a single key `success`, that contains a boolean value

sample: curl -X DELETE http://127.0.0.1:5000/questions/2
```
{
  "success": true
}    
```

## Deployment N/A

## Authors
Clinton Manakane

## Acknowledgements 
The ALX fullstack students(including: Iroatu Prince, Adebajo Oluwadamilola) on slack
