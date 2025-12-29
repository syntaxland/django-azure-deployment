# core/views.py
from django.http import HttpResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                font-family: sans-serif;
            }
            .message {
                padding: 20px;
                border: 1px solid #ccc;
                text-align: center;
            }
            .dashboard-link {
                color: #0066cc;          /* blue */
                text-decoration: none;
                font-weight: bold;
            }
            .dashboard-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="message">
            <h1>Welcome To Power Platform Demo!</h1>
            <h3>
                <a href="/dashboard/" class="dashboard-link">
                    Go to Dashboard
                </a>
            </h3>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
