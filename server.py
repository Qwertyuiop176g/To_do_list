import logging
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

tasks = []
filepath = os.path.abspath("tasks.txt")

@app.route('/tasks', methods=['GET'])
def gettasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def addtask():
    task = request.json.get('task')
    if task:
        tasks.append(task)
        app.logger.debug(f"Added task: {task}")
        return jsonify({'status': 'success'}), 201
    return jsonify({'status': 'error'}), 400

@app.route('/tasks', methods=['DELETE'])
def removetask():
    task = request.json.get('task')
    if task in tasks:
        tasks.remove(task)
        app.logger.debug(f"Removed task: {task}")
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 404

@app.route('/tasks/save', methods=['POST'])
def savetasks():
    try:
        dir_name = os.path.dirname(filepath)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(filepath, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        app.logger.debug("Tasks saved to tasks.txt")
        return jsonify({'status': 'success'})
    except Exception as e:
        app.logger.error(f"Error saving tasks: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/tasks/load', methods=['GET'])
def loadtasks():
    try:
        if not os.path.exists(filepath):
            app.logger.error("tasks.txt file not found")
            return jsonify({'status': 'error', 'message': 'tasks.txt file not found'}), 404
        
        with open(filepath, "r") as file:
            tasks.clear()
            for line in file:
                tasks.append(line.strip())
        app.logger.debug("Tasks loaded from tasks.txt")
        return jsonify({'status': 'success'})
    except Exception as e:
        app.logger.error(f"Error loading tasks: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
