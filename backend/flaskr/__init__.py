from lib2to3.pytree import type_repr
import os
from unicodedata import category
from urllib import response
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [q.format() for q in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    #CORS(app, resources={r"*/*": {"origins": "*"}})
    CORS(app)

    # The after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response

    # An endpoint to handle GET requests for all available categories.
    @app.route("/categories")
    def get_categories():
        select_categories = Category.query.order_by(Category.id).all()
        categories = {cat.id:cat.type for cat in select_categories}

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': categories,
            'total_categories': len(Category.query.all())
        })

    """
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    """
    @app.route("/questions")
    def get_questions():
        select_questions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, select_questions)

        select_categories = Category.query.order_by(Category.id).all()
        categories = {cat.id:cat.type for cat in select_categories}

        if len(current_questions) == 0:
            abort(404)

        response = jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'current_category': 'Sports',
            'categories': categories
        })

        return response

    # An endpoint to DELETE question using a question ID
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            q = Question.query.filter(Question.id==question_id).one_or_none()

            if q is None:
                abort(404)
            
            q.delete()

            return jsonify({
                'success': True
                })  
        except:
            abort(404)
        
        
    # An endpoint to POST a new question
    @app.route("/questions", methods=["POST"])
    def add_question():
        body = request.get_json()

        question = body.get("question", None)
        answer = body.get("answer", None)
        difficulty = body.get("difficulty", None)
        category = body.get("category", None)

        if question is None or answer is None:
            abort(422)
        
        try:
            q = Question(
                    question=question,
                    answer=answer,
                    difficulty=difficulty,
                    category=category
                )
            q.insert()

            return jsonify({
                'success': True
                })
        
        except:
            abort(422)

    # POST endpoint to get questions based on a search term.
    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        #search = request
        body = request.get_json()
        search = body.get("search", None)

        select_questions = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search))).all()
        current_questions = paginate_questions(request, select_questions)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(select_questions),
            'current_category': 'Sports',
        })
    
    # A GET endpoint to get questions based on category.
    @app.route("/categories/<int:category_id>/questions", methods=["GET"])
    def questions_by_category(category_id):
        current_category = Category.query.filter(Category.id == category_id).one_or_none()
        if current_category is None:
            abort(404)
        else:
            try:
                select_questions = Question.query.order_by(Question.id).filter(Question.category==category_id).all()
                current_questions = paginate_questions(request, select_questions)

                select_categories = Category.query.order_by(Category.id).all()
                categories = [cat.format() for cat in select_categories]

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(select_questions),
                    'current_category': current_category.format(),
                    'categories': categories
                })
            except:
                abort(404)

    # A POST endpoint to get questions to play the quiz.
    @app.route("/quizzes", methods=["POST"])
    def quizzes ():
        try:
            body = request.get_json()
            previous_questions = body.get("previous_questions", [])
            quiz_category = body.get("quiz_category", 0)

            print(previous_questions, quiz_category)

            if quiz_category == 0 or quiz_category['id'] == 0:
                questions = Question.query.all()
                questions = [q.format() for q in questions]

                return jsonify({
                        'success': True,
                        'question': questions[random.randint(0, len(questions) - 1)]
                    })
            else:
                questions = Question.query.filter(Question.category == quiz_category['id']).all()

                questions = [q.format() for q in questions]

                for ques in questions:
                    while ques['id'] not in previous_questions:
                        print({
                            'success': True,
                            'question': ques
                        })
                        return jsonify({
                            'success': True,
                            'question': ques
                        })
                    
            return jsonify({
                        'success': True,
                        'question': None
                    })
        except:
            abort(404)

    
    # Error handlers for all expected errors
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 404,'success': False,'message': 'resource not found'}), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({"success": False, "error": 422, "message": "unprocessable"}),422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"success": False, "error": 405, "message": "method not allowed"}), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"success": False, "error": 500, "message": "internal server error"}), 500
         
    return app

