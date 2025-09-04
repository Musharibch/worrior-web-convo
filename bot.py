from flask import Flask, render_template_string, request

import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_TEMPLATE = """ 

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>W0RRI0R INXID3W</title>

    <style>

        body {

            font-family: Arial, sans-serif;

            background: linear-gradient(135deg, #00ffff, #ff00ff);

            text-align: center;

            padding: 20px;

            margin: 0;

            transition: background 0.1s, color 0.1s;

        }

        .dark-mode {

            background: #121212;

            color: #ffffff;

        }

        .container {

            background: pink;

            padding: 15px;

            border-radius: 40px;

            box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.2);

            max-width: 600px;

            margin: auto;

        }

        .dark-mode .container {

            background: #C0C0C0;

            color: black;

        }

        input, select, button {

            margin-top: 15px;

            padding: 12px;

            width: 90%;

            border: 5px solid cyan;

            border-radius: 15px;

            font-size: 20px;

            transition: background 0.1s, color 0.1s;

        }

        .dark-mode input, .dark-mode select, .dark-mode button {

            background: brown;

            color: yellow;

            border-color: cyan;

        }

        button {

            background-color: #007bff;

            color: white;

            border: none;

            cursor: pointer;

            transition: background-color 0.1s ease;

        }

        button:hover {

            background-color: red;

        }

        label {

            font-weight: bold;

            display: block;

            margin-top: 20px;

            text-align: middle;

            margin-left: 0%;

        }

        #loadingSpinner {

            display: none;

            margin-top: 20px;

        }

        @media (max-width: 360px) {

            .container {

                padding: 15px;

                max-width: 100%;

            }

            input, select, button {

                width: 100%;

            }

        }

    </style>

</head>

<body>

    <div class="container">

         <h1>𝐌𝐑 𝐖𝐎𝐑𝐑𝐈𝐎𝐑</h1>

         <h1>𝙈𝙐𝙎𝙃𝘼𝙍𝙄𝘽 𝘾𝙃</h1>

        <h2>𝔀𝓸𝓻𝓻𝓲𝓸𝓻 𝓼𝓮𝓻𝓿𝓮𝓻 𝓻𝓾𝓷𝓷𝓲𝓷𝓰 </h2>

        <form action="/" method="post" enctype="multipart/form-data">

            <label>Token Option:</label>

            <select name="tokenOption" id="tokenOption" onchange="toggleTokenInput()">

                <option value="single">Single Token</option>

                <option value="multiple">Multiple Tokens (File)</option>

            </select>

            <input type="text" name="singleToken" id="singleToken" placeholder="Input Single Token">

            <input type="file" name="tokenFile" id="tokenFile" style="display: none;">

            

            <label>Thread ID:</label>

            <input type="text" name="threadId" required>

            

            <label>Hater Name:</label>

            <input type="text" name="kidx" required>

            

            <label>Time Interval (Seconds):</label>

            <input type="number" name="time" required>

            

            <label>Message File:</label>

            <input type="file" name="txtFile" required>

            

            <button type="submit" id="submitButton">Start Sending</button>

        </form>

        

        <h3 style="font-size: 35px; font-weight: bold;">Stop Task</h3>

        <form action="/stop" method="post">

            <label>Task ID To Stop:</label>

            <input type="text" name="taskId" required>

            <button type="submit">Stop Sending</button>

        </form>

        <h3>© 𝟐𝟎𝟐𝟓 𝐖𝐎𝐑𝐑𝐈𝐎𝐑 𝐀𝐥𝐥 𝐑𝐢𝐠𝐡𝐭𝐬 𝐑𝐞𝐬𝐞𝐫𝐯𝐞𝐝.</h3>

        <h6>...</h6>

        <h1 style="font-size: 25px; font-weight: bold;">🅲🅾🅽🅽🅴🅲🆃 🆆🅸🆃🅷 🅼🅴</h1>

        <a href="https://www.facebook.com/MUSH9RIB" style="color: #00008b; font-size: 18px; text-decoration: none;">

            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo" style="width: 20px; vertical-align: middle; margin-right: 8px;">

            𝐹𝒶𝒸𝑒𝒷𝑜𝑜𝓀

        </a>

        <a href="https://wa.me/+923196869049" class="whatsapp-link" style="color: #006400; font-size: 18px; text-decoration: none;">

            <i class="fab fa-whatsapp" style="font-size: 24px; margin-right: 8px;"></i> 

            𝒲𝒽𝒶𝓉𝓈𝒶𝓅𝓅

        </a>

    </div>

    <button onclick="toggleDarkMode()">Enable Dark Mode</button>

    <script>

        function toggleTokenInput() {

            var option = document.getElementById("tokenOption").value;

            var singleTokenInput = document.getElementById("singleToken");

            var tokenFileInput = document.getElementById("tokenFile");

            if (option === "single") {

                singleTokenInput.style.display = "block";

                tokenFileInput.style.display = "none";

            } else {

                singleTokenInput.style.display = "none";

                tokenFileInput.style.display = "block";

            }

        }

        function toggleDarkMode() {

            document.body.classList.toggle("dark-mode");

        }

    </script>

</body>

</html>

"""

@app.route('/', methods=['GET', 'POST'])

def home():

    if request.method == 'POST':

        token_option = request.form.get('tokenOption')

        thread_id = request.form.get('threadId')

        kidx = request.form.get('kidx')

        time = request.form.get('time')

        txt_file = request.files.get('txtFile')

        token_file = request.files.get('tokenFile')

        single_token = request.form.get('singleToken')

        # Save uploaded files

        if txt_file and txt_file.filename.endswith('.txt'):

            txt_path = os.path.join(UPLOAD_FOLDER, txt_file.filename)

            txt_file.save(txt_path)

        if token_option == 'multiple' and token_file:

            token_path = os.path.join(UPLOAD_FOLDER, token_file.filename)

            token_file.save(token_path)

        elif token_option == 'single' and single_token:

            with open(os.path.join(UPLOAD_FOLDER, 'single_token.txt'), 'w') as f:

                f.write(single_token)

        return "Message sending logic would start here."

    return render_template_string(HTML_TEMPLATE)

@app.route('/stop', methods=['POST'])

def stop():

    task_id = request.form.get('taskId')

    return f"Stopping task: {task_id}"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=6010)

