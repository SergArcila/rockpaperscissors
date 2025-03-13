from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "SOME_RANDOM_SECRET_KEY"

def check_winner():
    user_score = session.get("user_score", 0)
    comp_score = session.get("comp_score", 0)
    if user_score >= 10:
        return "You reached 10 points! You win!"
    elif comp_score >= 10:
        return "Computer reached 10 points! You lose!"
    return None

@app.route("/", methods=["GET"])
def index():
    user_score = session.get("user_score", 0)
    comp_score = session.get("comp_score", 0)
    winner_message = check_winner()

    return render_template(
        "index.html",
        user_score=user_score,
        comp_score=comp_score,
        winner_message=winner_message
    )

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.form.get("choice")
    
    if user_choice == "quit":
        session["user_score"] = 0
        session["comp_score"] = 0
        return redirect(url_for("index"))
    
    # Convert to int
    try:
        user_choice = int(user_choice)
    except ValueError:
        return redirect(url_for("index"))
    
    # Computer's random choice
    comp_choice = random.randint(1, 3)
    
    user_score = session.get("user_score", 0)
    comp_score = session.get("comp_score", 0)

    # Determine round result
    if user_choice == comp_choice:
        result_msg = "It's a tie!"
    elif (user_choice == 1 and comp_choice == 3) \
         or (user_choice == 2 and comp_choice == 1) \
         or (user_choice == 3 and comp_choice == 2):
        result_msg = "You win this round!"
        user_score += 1
    else:
        result_msg = "Computer wins this round!"
        comp_score += 1

    # Update scores
    session["user_score"] = user_score
    session["comp_score"] = comp_score

    winner_message = check_winner()

    return render_template(
        "result.html",
        result_msg=result_msg,
        user_choice=user_choice,
        comp_choice=comp_choice,
        user_score=user_score,
        comp_score=comp_score,
        winner_message=winner_message
    )

if __name__ == "__main__":
    # Listen on port 5000 (default). For production on Railway, you'd do:
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    #app.run(debug=True)
