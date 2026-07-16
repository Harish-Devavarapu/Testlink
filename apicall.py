from flask import Flask, request

app = Flask(__name__)

# -----------------------------
# Cricket Player Database
# -----------------------------
players = [
    {
        "name": "MS Dhoni",
        "country": "India",
        "innings": 297,
        "runs": 10773,
        "highest_score": 183,
        "average": 50.57
    },
    {
        "name": "Virat Kohli",
        "country": "India",
        "innings": 302,
        "runs": 14181,
        "highest_score": 183,
        "average": 57.88
    },
    {
        "name": "Rohit Sharma",
        "country": "India",
        "innings": 273,
        "runs": 11168,
        "highest_score": 264,
        "average": 48.76
    },
    {
        "name": "Kumar Sangakkara",
        "country": "Sri Lanka",
        "innings": 380,
        "runs": 14234,
        "highest_score": 169,
        "average": 41.98
    },
    {
        "name": "Ricky Ponting",
        "country": "Australia",
        "innings": 365,
        "runs": 13704,
        "highest_score": 164,
        "average": 42.03
    },
    {
        "name": "Steve Smith",
        "country": "Australia",
        "innings": 170,
        "runs": 5800,
        "highest_score": 164,
        "average": 43.28
    },
    {
        "name": "Shane Watson",
        "country": "Australiaa",
        "innings": 190,
        "runs": 5757,
        "highest_score": 185,
        "average": 40.54
    },
    {
        "name": "Chris Gayle",
        "country": "West Indies",
        "innings": 294,
        "runs": 10480,
        "highest_score": 215,
        "average": 37.83
    },
    {
        "name": "AB de Villiers",
        "country": "South Africa",
        "innings": 218,
        "runs": 9577,
        "highest_score": 176,
        "average": 53.50
    }
]


# -----------------------------
# Home Page
# -----------------------------
@app.route('/')
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>Cricket Player Statistics</title>

        <style>

            body{
                font-family:Arial;
                background:#f4f4f4;
                text-align:center;
            }

            .container{

                width:450px;
                margin:auto;
                margin-top:80px;
                background:white;
                padding:30px;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;

            }

            input{

                width:90%;
                padding:10px;
                margin:10px;
                font-size:16px;

            }

            button{

                background:green;
                color:white;
                padding:10px 25px;
                font-size:16px;
                border:none;
                border-radius:5px;
                cursor:pointer;

            }

            button:hover{

                background:darkgreen;

            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>🏏 Cricket Player Statistics</h1>

            <form action="/player" method="GET">

                <input
                type="text"
                name="name"
                placeholder="Enter Player Name"
                required>

                <input
                type="text"
                name="country"
                placeholder="Enter Country"
                required>

                <br><br>

                <button type="submit">

                    Search Player

                </button>

            </form>

        </div>

    </body>

    </html>
    """


# -----------------------------
# Search Player
# -----------------------------
@app.route('/player')
def player():

    name = request.args.get("name")
    country = request.args.get("country")

    for p in players:

        if p["name"].lower() == name.lower() and p["country"].lower() == country.lower():

            return f"""

            <html>

            <head>

            <title>Player Details</title>

            <style>

            body{{
                font-family:Arial;
                background:#eef2f3;
                text-align:center;
            }}

            .card{{
                width:500px;
                margin:auto;
                margin-top:70px;
                background:white;
                padding:25px;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }}

            h2{{
                color:green;
            }}

            p{{
                font-size:20px;
            }}

            a{{
                text-decoration:none;
                color:blue;
            }}

            </style>

            </head>

            <body>

            <div class="card">

            <h2>🏏 Player Details</h2>

            <p><b>Player Name :</b> {p["name"]}</p>

            <p><b>Country :</b> {p["country"]}</p>

            <p><b>Innings :</b> {p["innings"]}</p>

            <p><b>Runs :</b> {p["runs"]}</p>

            <p><b>Highest Score :</b> {p["highest_score"]}</p>

            <p><b>Batting Average :</b> {p["average"]}</p>

            <br>

            <a href="/">⬅ Search Another Player</a>

            </div>

            </body>

            </html>

            """

    return """

    <html>

    <body style="font-family:Arial;text-align:center;margin-top:100px;">

    <h2 style="color:red;">❌ Player Not Found</h2>

    <br>

    <a href="/">Go Back</a>

    </body>

    </html>

    """


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)