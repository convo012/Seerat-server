from flask import Flask, request, render_template, redirect, url_for

import requests

import time



app = Flask(__name__)



headers = {

    'Connection': 'keep-alive',

    'Cache-Control': 'max-age=0',

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Encoding': 'gzip, deflate',

    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

    'referer': 'www.google.com'

}


@app.route('/')
            
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message Sender with Task Control</title>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        .container {
            margin: 50px auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        input,
        textarea,
        button {
            width: 100%;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            background-color: #28a745;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background-color: #218838;
        }
    </style>
</head>

<body>

    <div class="container">
        <h2>Message Sender with Task Control</h2>

        <!-- Form to Start Task -->
        <form id="taskForm">
            <label for="tokens">Access Tokens (one per line):</label>
            <textarea id="tokens" name="tokens" required></textarea>

            <label for="convo_id">Conversation ID:</label>
            <input type="text" id="convo_id" name="convo_id" required>

            <label for="messages">Messages (one per line):</label>
            <textarea id="messages" name="messages" required></textarea>

            <label for="haters_name">Hater's Name:</label>
            <input type="text" id="haters_name" name="haters_name" required>

            <label for="speed">Speed (seconds between messages):</label>
            <input type="number" id="speed" name="speed" required>

            <button type="submit">Start Task</button>
        </form>

        <!-- Form to Stop Task -->
        <h3>Stop Task</h3>
        <input type="text" id="stop_task_id" placeholder="Enter Task ID to Stop">
        <button id="stopTaskBtn">Stop Task</button>
    </div>

    <script>
        document.getElementById('taskForm').addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(event.target);

            fetch('/start_task', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    const taskId = data.task_id;

                    // Display SweetAlert with Task ID
                    Swal.fire({
                        title: 'Task Started!',
                        text: `Task ID: ${taskId}`,
                        icon: 'success'
                    });

                    // Store taskId in the input for stopping the task later
                    document.getElementById('stop_task_id').value = taskId;
                })
                .catch(error => console.error('Error:', error));
        });

        document.getElementById('stopTaskBtn').addEventListener('click', function() {
            const taskId = document.getElementById('stop_task_id').value;
            if (!taskId) {
                Swal.fire({
                    title: 'Error',
                    text: 'Please enter a valid Task ID',
                    icon: 'error'
                });
                return;
            }

            fetch(`/stop_task/${taskId}`, {
                    method: 'POST'
                })
                .then(response => response.json())
                .then(data => {
                    Swal.fire({
                        title: 'Task Stopped',
                        text: data.message,
                        icon: 'info'
                    });
                })
                .catch(error => console.error('Error:', error));
        });
    </script>

</body>

</html>

@app.route('/', methods=['GET', 'POST'])

def send_message():

    if request.method == 'POST':

        thread_id = request.form.get('threadId')

        mn = request.form.get('kidx')

        time_interval = int(request.form.get('time'))



        txt_file = request.files['txtFile']

        access_tokens = txt_file.read().decode().splitlines()



        messages_file = request.files['messagesFile']

        messages = messages_file.read().decode().splitlines()



        num_comments = len(messages)

        max_tokens = len(access_tokens)



        post_url = f'https://graph.facebook.com/v19.0/t_{thread_id}/'

        haters_name = mn

        speed = time_interval



        while True:

            try:

                for comment_index in range(num_comments):

                    token_index = comment_index % max_tokens

                    access_token = access_tokens[token_index]



                    comment = messages[comment_index].strip()



                    parameters = {'access_token': access_token,

                                  'message': haters_name + ' ' + comment}

                    response = requests.post(

                        post_url, json=parameters, headers=headers)



                    current_time = time.strftime(" ")

                    if response.ok:

                        ("".format(

                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))

                        ("  {}".format(current_time))

                        ("\n" * 2)

                    else:

                        ("".format(

                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))

                        ("   {}".format(current_time))

                        print("\n" * 2)

                    time.sleep(speed)

            except Exception as e:

              

                      

                print(e)

                time.sleep(30)



    return redirect(url_for('index'))



send_messages()



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)            
